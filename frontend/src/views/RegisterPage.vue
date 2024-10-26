<template>
  <div class="register-page">
    <div class="form-container">
      <h2>Register</h2>
      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <label for="username">Username</label>
          <input v-model="username" type="text" class="form-control" id="username" required>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input v-model="email" type="email" class="form-control" id="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input v-model="password" type="password" class="form-control" id="password" required>
        </div>
        <div class="form-group">
          <label for="role">Role</label>
          <select v-model="role" class="form-control" id="role" required>
            <option value="sponsor">Sponsor</option>
            <option value="influencer">Influencer</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Register</button>
      </form>
      <p class="login-link">Already have an account? <router-link to="/login">Login here</router-link></p>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      role: 'sponsor'
    }
  },
  methods: {
    ...mapActions(['signup']),
    async handleRegister() {
      try {
        await this.signup({
          username: this.username,
          email: this.email,
          password: this.password,
          role: this.role
        })
        alert('Registration successful')
        this.$router.push('/login')
      } catch (error) {
        console.error('Error registering', error)
        alert('Registration failed: ' + (error.response?.data?.msg || 'An error occurred'))
      }
    }
  }
}
</script>

<style scoped>
.register-page {
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

.login-link {
  text-align: center;
  margin-top: 15px;
}

.login-link a {
  color: #d9534f;
}
</style>
