<template>
  <div class="dashboard">
    <header class="hero">
      <div class="hero-content">
        <h1 class="text-center">Sponsor Dashboard</h1>
        <div class="cta-buttons">
          <button class="cta-button" @click="goToCampaigns">Manage Campaigns</button>
          <button class="cta-button" @click="goToAdRequests">Manage Ad Requests</button>
        </div>
      </div>
    </header>
    <section class="search-section">
      <h2>Search Influencers</h2>
      <form @submit.prevent="searchInfluencers">
        <input v-model="searchNiche" type="text" placeholder="Search by niche">
        <input v-model.number="searchMinReach" type="number" placeholder="Min reach" min="0">
        <input v-model.number="searchMaxReach" type="number" placeholder="Max reach" min="0">
        <input v-model.number="searchMinFollowers" type="number" placeholder="Min followers" min="0">
        <input v-model.number="searchMaxFollowers" type="number" placeholder="Max followers" min="0">
        <button type="submit" class="search-button">Search</button>
        <button type="button" @click="clearSearch" class="clear-button">Clear</button>
      </form>
      <p v-if="loading" class="loading-message">Searching...</p>
      <p v-if="!loading && !influencers.length && searchNiche" class="no-results-message">
        No influencers found matching your search criteria.
      </p>
      <ul v-if="!loading && influencers.length">
        <li v-for="influencer in influencers" :key="influencer.id" class="influencer-item">
          <p><strong>Name:</strong> {{ influencer.name }}</p>
          <p><strong>Niche:</strong> {{ influencer.niche }}</p>
          <p><strong>Reach:</strong> {{ influencer.reach }}</p>
          <p><strong>Followers:</strong> {{ influencer.followers }}</p>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchNiche: '',
      searchMinReach: null,
      searchMaxReach: null,
      searchMinFollowers: null,
      searchMaxFollowers: null,
      influencers: [],
      loading: false
    };
  },
  methods: {
    goToCampaigns() {
      this.$router.push('/sponsor/campaigns');
    },
    goToAdRequests() {
      this.$router.push('/sponsor/list-campaigns');
    },
    async searchInfluencers() {
      this.loading = true;
      try {
        const response = await axios.get('http://127.0.0.1:5000/sponsor/search/influencers', {
          headers: this.getAuthHeaders(),
          params: {
            niche: this.searchNiche,
            min_reach: this.searchMinReach,
            max_reach: this.searchMaxReach,
            min_followers: this.searchMinFollowers,
            max_followers: this.searchMaxFollowers
          }
        });
        this.influencers = response.data;
      } catch (error) {
        console.error('Error searching influencers', error);
      } finally {
        this.loading = false;
      }
    },
    clearSearch() {
      this.searchNiche = '';
      this.searchMinReach = null;
      this.searchMaxReach = null;
      this.searchMinFollowers = null;
      this.searchMaxFollowers = null;
      this.influencers = [];
    },
    getAuthHeaders() {
      const token = localStorage.getItem('access_token');
      return {
        Authorization: `Bearer ${token}`
      };
    }
  }
};
</script>

<style scoped>
.dashboard {
  text-align: center;
  margin-top: 50px;
}
.hero {
  background: linear-gradient(to right, #e07a7a, #d9534f);
  color: #fff;
  text-align: left;
  padding: 60px 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 40vh;
}
.hero-content {
  max-width: 900px;
}
.hero-content h1 {
  font-size: 3rem;
  margin: 0;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
.cta-buttons {
  margin-top: 20px;
}
.cta-button {
  background: #fff;
  color: #d9534f;
  padding: 15px 30px;
  border-radius: 5px;
  font-size: 1.2rem;
  margin: 10px;
  display: inline-block;
  transition: background 0.3s, color 0.3s;
}
.cta-button:hover {
  background: #d9534f;
  color: #fff;
}

.search-section {
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  margin-top: 20px;
}
.search-section h2 {
  font-size: 2rem;
  margin-bottom: 10px;
}
form {
  display: flex;
  flex-direction: column;
}
input {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.search-button {
  background: #d9534f;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2rem;
}
.search-button:hover {
  background: #c9302c;
}
.clear-button {
  background: #ccc;
  color: #333;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2rem;
  margin-top: 10px;
}
.clear-button:hover {
  background: #bbb;
}
.loading-message, .no-results-message {
  font-size: 1rem;
  color: #777;
}
.influencer-item {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
</style>
