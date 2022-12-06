<template>
  <section class="main-section">
    <h1 class="main-h">TechCheap</h1>
    <p>A blog that will help you learn something new.</p>
    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/posts">here</a> to view all posts.</p>
    </div>
    <p v-else>
      <span>To be with us as soon as possible </span>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log in</a></span>
      <span>.</span>
    </p>
  </section>
</template>
<script>

export default {
  name: 'Home',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    }
  },
}
</script>
<style scoped>
.main-section {
  text-align: center;
  margin-top: 150px;
}

.main-h {
  font-size: 100px;
}
</style>
