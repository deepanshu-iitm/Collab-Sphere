<template>
  <div class="login-page">
    <div class="form-container">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email</label>
          <input v-model="email" type="email" class="form-control" id="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input v-model="password" type="password" class="form-control" id="password" required>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
      <p class="register-link">Don't have an account? <router-link to="/register">Register here</router-link></p>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    ...mapActions(['login']),
    async handleLogin() {
      try {
        const role = await this.login({ email: this.email, password: this.password })
        console.log('Login successful. User role:', role)

        // Redirect based on role
        switch (role) {
          case 'admin':
            this.$router.push('/admin-dashboard')
            break
          case 'sponsor':
            this.$router.push('/sponsor-dashboard')
            break
          case 'influencer':
            this.$router.push('/influencer-dashboard')
            break
          default:
            console.error('Unexpected role:', role)
            alert('Login failed: Unexpected role')
        }
      } catch (error) {
        console.error('Error logging in', error)
        alert('Login failed: ' + (error.response?.data?.msg || 'An error occurred'))
      }
    }
  }
}
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f4f4f4;
}

.form-container {
  background: #fff;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

h2 {
  font-size: 2rem;
  color: #d9534f;
  margin-bottom: 20px;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

.label {
  font-size: 1rem;
  color: #333;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.btn-primary {
  background: #d9534f;
  color: #fff;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  width: 100%;
  transition: background 0.3s;
}

.btn-primary:hover {
  background: #c94c4c;
}

.register-link {
  text-align: center;
  margin-top: 15px;
}

.register-link a {
  color: #d9534f;
}
</style>
