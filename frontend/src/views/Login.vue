<template>
  <section>
    <form @submit.prevent="submit" class="main-form">
      <h1 class="main-h">TechCheap</h1>
      <p class="main-h">Be always with us</p>
      <div class="mb-3">
        <label for="username" class="form-label">Login:</label>
        <input type="text" name="username" v-model="form.login" class="form-control"/>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" name="password" v-model="form.password" class="form-control"/>
      </div>
      <button type="submit" class="btn btn-outline-primary">Login</button>
      <p class="transition-register">
        <span>Not Registered? </span>
        <span><a href="/register">Register</a></span>
      </p>
    </form>
  </section>
</template>

<script>
import {mapActions} from 'vuex';

export default {
  name: 'Login',
  data() {
    return {
      form: {
        login: '',
        password: '',
      }
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.login);
      User.append('password', this.form.password);
      await this.logIn(User);
      this.$router.push('/');
    }
  }
}
</script>
<style scoped>
.main-form {
  margin: 0 200px 0 200px;
}

.main-h {
  text-align: center;
  margin: 0 0 20px 0;
}

.transition-register {
  margin: 20px 0 0 0;
  text-align: center;
}
</style>