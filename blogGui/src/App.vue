<template>
  <nav class="flex items-center justify-around h-10">
    <div>
      <router-link class="mx-12 duration-200" to="/">Home</router-link>
    </div>
    <div v-if="!$store.state.isLogged">
      <router-link class="mx-12 duration-200" to="/login">Login</router-link>
    </div>
    <div v-if="$store.state.isLogged">
      <router-link class="mx-12 duration-200" to="/login">Profile</router-link>
    </div>
  </nav>
  <router-view class="mt-6"/>
</template>

<script>
export default {
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  font-size: largeHello to my blog application!!;
}

nav a.router-link-exact-active {
  color: #ff9f1c;
}
</style>
