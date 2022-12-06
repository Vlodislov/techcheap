<template>
  <div v-if="post" class="main-h">
    <h1>{{ post.title }}</h1>
    <hr/>
    <br/>
    <p><strong>{{ post.author.nickname }}</strong> {{ post.created_at.split('T')[0] }}</p>
    <h4><strong
        style="color: black;">{{ post.title }}</strong>
    </h4>
    <p>{{ post.description }}</p>
    <p>{{ post.content }}</p>

    <div v-if="user.id === post.author.id">
      <p>
        <router-link :to="{name: 'EditPost', params:{id: post.id}}" class="btn btn-outline-primary">Edit</router-link>
      </p>
      <p>
        <button @click="removePost()" class="btn btn-outline-secondary">Delete</button>
      </p>
    </div>
  </div>
</template>


<script>
import {mapGetters, mapActions} from 'vuex';

export default {
  name: 'Post',
  props: ['id'],
  async created() {
    try {
      await this.viewPost(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/posts');
    }
  },
  computed: {
    ...mapGetters({post: 'statePost', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewPost', 'deletePost']),
    async removePost() {
      try {
        await this.deletePost(this.id);
        this.$router.push('/posts');
      } catch (error) {
        console.error(error);
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