<template>
  <section>
    <form @submit.prevent="submit" class="main-form">
      <h1 class="main-h">TechCheap</h1>
      <p class="main-h">Be always with us</p>
      <div class="mb-3">
        <label for="full_name" class="form-label">Nickname:</label>
        <input type="text" name="full_name" v-model="user.nickname" class="form-control"/>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input type="text" name="email" v-model="user.email" class="form-control"/>
      </div>
      <div class="mb-3">
        <label for="username" class="form-label">Login:</label>
        <input type="text" name="username" v-model="user.login" class="form-control"/>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" name="password" v-model="user.password" class="form-control"/>
      </div>
      <button type="submit" class="btn btn-outline-primary">Register</button>
      <p class="transition-login">
        <span>Already registered? </span>
        <span><a href="/login">Log in</a></span>
      </p>
    </form>
  </section>
</template>

<script>
import {mapActions} from 'vuex';

export default {
  name: 'Register',
  data() {
    return {
      user: {
        login: '',
        nickname: '',
        password: '',
        email: '',
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        await this.register(this.user);
        this.$router.push('/');
      } catch (error) {
        throw 'Login already exists. Please try again.';
      }
    },
  },
};
</script>
<style scoped>
.main-form {
  margin: 0 200px 0 200px;
}

.main-h {
  text-align: center;
  margin: 0 0 20px 0;
}

.transition-login {
  margin: 20px 0 0 0;
  text-align: center;
}
</style>