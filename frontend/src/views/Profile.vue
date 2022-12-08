<template>
  <div>
  <section>
    <h1 class="main-h">Profile</h1>
    <hr/>
    <br/>
    <div >
      <p><strong>Nickname:</strong> <span>{{ user.nickname }}</span></p>
      <p><strong>Email:</strong> <span>{{ user.email }}</span></p>
      <p>
        <button @click="deleteAccount()" class="btn btn-outline-primary">Delete {{ user.login }}</button>
      </p>
    </div>
  </section>
  <section>
    <h1 class="main-h">My Posts</h1>
    <hr/>
    <br/>

    <div v-if="posts.length" style="margin: 0 70px 0 70px">
      <div v-for="post in posts" :key="post.id" class="notes">
        <div v-if="user.id === post.author.id" >
        <div  class="card" style="width: auto;">
          <div  class="card-body">
            <ul>
              <p><strong>Created: </strong> {{ post.created_at.split('T')[0] }}</p>
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
  name: 'Profile',
  created: function () {
    return this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({user: 'stateUser', posts: 'statePosts'}),
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  },
}
</script>
<style scoped>
.main-h {
  text-align: center;
}
</style>