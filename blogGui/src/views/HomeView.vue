<template>
  <div>
    <h1 class="text-3xl text-sky-500">Hello to my vue blog application!!</h1>
    <p>Let's Log in or create an account</p>
    <p>Current logged user: <span class="text-rose-500">{{ $store.state.currentLoggedUser }}</span></p>
  </div>
</template>
<script>
export default {
  
}
</script>
<style>
</style>