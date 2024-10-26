<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="brand-logo">CollabSphere</router-link>
    </div>
    <div class="navbar-menu">
      <router-link to="/" class="nav-link">Home</router-link>
      <router-link to="/about" class="nav-link">About</router-link>
      <!-- Add more links as needed -->
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #d36c6c;
  color: #fff;
  padding: 10px 20px;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  z-index: 1000;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}

.brand-logo {
  color: #fff;
  text-decoration: none;
}

.navbar-menu {
  display: flex;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  margin: 0 15px;
  font-weight: 500;
  padding: 8px 12px;
}

.nav-link:hover,
.nav-link.router-link-exact-active {
  background-color: #c05454;
  border-radius: 4px;
}
</style>
