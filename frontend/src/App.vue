<template>
  <div id="app">
    <MainNavbar />
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import MainNavbar from './components/MainNavbar.vue';

export default {
  name: 'App',
  components: {
    MainNavbar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 56px;
}

main {
  padding: 20px;
}

.navbar {
  padding: 0; 
}

nav a {
  font-weight: bold;
  color: #d9534f;
}

nav a.router-link-exact-active {
  color: #c94c4c; 
}
</style>
