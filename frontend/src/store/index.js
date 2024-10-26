import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: false,
    userRole: null,
  },
  mutations: {
    SET_AUTH(state, payload) {
      state.isAuthenticated = payload.isAuthenticated
      state.userRole = payload.userRole
    },
    LOGOUT(state) {
      state.isAuthenticated = false
      state.userRole = null
    },
  },
  actions: {
    async login({ commit }, { email, password }) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/auth/login', { email, password })
        commit('SET_AUTH', { isAuthenticated: true, userRole: response.data.role })
        localStorage.setItem('access_token', response.data.access_token)
        return response.data.role
      } catch (error) {
        console.error('Error logging in:', error)
        throw error
      }
    },
    async signup(_, userData) {
      try {
        await axios.post('http://127.0.0.1:5000/auth/register', userData)
      } catch (error) {
        console.error('Error signing up:', error)
        throw error
      }
    },
    logout({ commit }) {
      localStorage.removeItem('access_token')
      commit('LOGOUT')
    },
  },
})
