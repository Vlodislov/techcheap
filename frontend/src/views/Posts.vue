<template>
  <div>
    <section>
      <h1 class="main-h">Add new post</h1>
      <p class="main-h">Share your skills as soon as possible</p>
      <hr/>
      <br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control"/>
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Description:</label>
          <textarea
              name="content"
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

    <br/><br/>

    <section>
      <h1 class="main-h">Posts</h1>
      <p class="main-h">All the most interesting posts</p>
      <hr/>
      <br/>

      <div v-if="posts.length" style="margin: 0 70px 0 70px">
        <div v-for="post in posts" :key="post.id" class="notes">
          <div class="card" style="width: auto;">
            <div class="card-body">
              <ul>
                <p><strong>{{ post.author.nickname }}</strong> {{ post.created_at.split('T')[0] }}</p>
                <h4>
                  <router-link :to="{name: 'Post', params:{id: post.id}}"><strong
                      style="color: black; text-decoration: underline;">{{ post.title }}</strong>
                  </router-link>
                </h4>
                <p>{{ post.description }}</p>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';

export default {
  name: 'Posts',
  data() {
    return {
      form: {
        title: '',
        content: '',
        description: ''
      },
    };
  },
  created: function () {
    return this.$store.dispatch('getPosts');
  },
  computed: {
    ...mapGetters({posts: 'statePosts'}),
  },
  methods: {
    ...mapActions(['createPost']),
    async submit() {
      await this.createPost(this.form);
    },
  },
};
</script>
<style scoped>
.main-h {
  text-align: center;
  margin: 0 0 20px 0;
}
</style>
