<template>
  <section>
    <h1 class="main-h">Edit post {{ note.title }}</h1>
    <p class="main-h">{{ note.author.nickname }} {{ note.created_at.split('T')[0] }}</p>
    <hr/>
    <br/>

    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="title" class="form-label">Title:</label>
        <input type="text" name="title" v-model="form.title" class="form-control"/>
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description:</label>
        <textarea
            name="description"
            v-model="form.description"
            class="form-control"
        ></textarea>
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">Content:</label>
        <textarea
            name="content"
            v-model="form.content"
            class="form-control"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-outline-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';

export default {
  name: 'EditPost',
  props: ['id'],
  data() {
    return {
      form: {
        title: '',
        content: '',
        description: '',
      },
    };
  },
  created: function () {
    this.GetPost();
  },
  computed: {
    ...mapGetters({note: 'statePost'}),
  },
  methods: {
    ...mapActions(['updatePost', 'viewPost']),
    async submit() {
      try {
        let note = {
          id: this.id,
          form: this.form,
        };
        await this.updatePost(note);
        this.$router.push({name: 'Post', params: {id: this.note.id}});
      } catch (error) {
        console.log(error);
      }
    },
    async GetPost() {
      try {
        await this.viewPost(this.id);
        this.form.title = this.note.title;
        this.form.content = this.note.content;
        this.form.description = this.note.description;
      } catch (error) {
        console.error(error);
        this.$router.push('/posts');
      }
    }
  },
};
</script>
<style scoped>
.main-h {
  text-align: center;
}
</style>
