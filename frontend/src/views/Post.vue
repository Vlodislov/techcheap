<template>
  <div>
    <div v-if="post" class="main-h">
      <h1>{{ post.title }}</h1>
      <hr/>
      <br/>
      <p><strong>{{ post.author.nickname }}</strong> {{ post.created_at.split('T')[0] }}</p>
      <h4><strong
          style="color: black;">{{ post.title }}</strong>
      </h4>
      <p>{{ post.description }}</p>
      <p style="word-break: break-all">{{ post.content }}</p>

      <div v-if="user.id === post.author.id">
        <p>
          <router-link :to="{name: 'EditPost', params:{id: post.id}}" class="btn btn-outline-primary">Edit</router-link>
        </p>
        <p>
          <button @click="removePost()" class="btn btn-outline-secondary">Delete</button>
        </p>
      </div>
    </div>

    <section>
      <h1 class="main-h">Add comment</h1>
      <hr/>
      <br/>

      <p><strong>Author: {{ user.nickname }}</strong></p>
      <form  @submit.prevent="submit">
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

    <section>
      <h1 class="main-h">Comments</h1>
      <hr/>
      <br/>

      <div v-if="comments.length" style="margin: 0 70px 0 70px">
        <div v-for="comment in comments" :key="comment.id" class="notes">
          <div v-if="comment.post.id === post.id">
            <div class="card" style="width: auto;">
              <div class="card-body">
                <ul>
                  <p><strong>{{ comment.author.nickname }}</strong> {{ comment.created_at.split('T')[0] }}</p>
                  <p>{{ comment.content }}</p>
                </ul>
                <ul>
                  <div v-if="user.id === comment.author.id">
                    <p>
                      <button @click="removeComment(comment.id)" class="btn btn-outline-secondary">Delete</button>
                    </p>
                  </div>
                </ul>
              </div>
            </div>
            <br/>
          </div>
        </div>
      </div>

    </section>

  </div>

</template>


<script>
import {mapGetters, mapActions} from 'vuex';

export default {
  name: 'Post',
  props: ['id'],
  data() {
    return {
      form: {
        content: '',
        post_id: 0,
      },
    };
  },
  async created() {
    try {
      await this.viewPost(this.id);
      await this.$store.dispatch('getComments');
    } catch (error) {
      console.error(error);
      this.$router.push('/posts');
    }
  },
  computed: {
    ...mapGetters({post: 'statePost', user: 'stateUser', comments: "stateComments"}),
  },
  methods: {
    ...mapActions(['viewPost', 'deletePost', 'deleteComment', 'createComment']),
    async submit() {
      console.log("THIS!!!!");
      console.log(this.post.id);
      this.form.post_id = this.post.id;
      await this.createComment(this.form);
      this.form.content = '';
    },
    async removePost() {
      try {
        await this.deletePost(this.id);
        this.$router.push('/posts');
      } catch (error) {
        console.error(error);
      }
    },
    async removeComment(comment_id) {
      try {
        await this.deleteComment(comment_id);
        window.location.reload();
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
<style scoped>
.main-h {
  text-align: center;
}
</style>