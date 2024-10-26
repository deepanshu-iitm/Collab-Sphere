<template>
  <div class="campaigns-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Your Campaigns</h1>
      </div>
    </header>
    <div class="campaign-list">
      <div v-for="campaign in campaigns" :key="campaign.id" class="campaign-card">
        <h2>{{ campaign.name }}</h2>
        <p>{{ campaign.description }}</p>
        <p>Start Date: {{ campaign.start_date }}</p>
        <p>End Date: {{ campaign.end_date }}</p>
        <p>Budget: {{ campaign.budget }}</p>
        <p>Visibility: {{ campaign.visibility }}</p>
        <p>Goals: {{ campaign.goals }}</p>
        <div class="button-group">
          <button class="btn btn-primary" @click="viewAdRequests(campaign.id)">View Ad Requests</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CampaignsList',
  data() {
    return {
      campaigns: []
    }
  },
  created() {
    this.fetchCampaigns();
  },
  methods: {
    fetchCampaigns() {
      const token = localStorage.getItem('access_token');
      fetch('http://127.0.0.1:5000/sponsor/campaigns', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => response.json())
      .then(data => {
        this.campaigns = data;
      })
      .catch(error => {
        console.error('Error fetching campaigns:', error);
      });
    },
    viewAdRequests(campaignId) {
      this.$router.push(`/sponsor/campaigns/${campaignId}/adrequests`);
    }
  }
}
</script>

<style scoped>
.campaigns-page {
  background: #f8f9fa;
  padding: 40px;
}

.hero {
  background: linear-gradient(to right, #e07a7a, #d9534f);
  color: #fff;
  padding: 40px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.hero-content h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
  font-weight: 600;
}

.campaign-list {
  margin-top: 30px;
}

.campaign-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
  padding: 20px;
  text-align: left;
  transition: transform 0.3s, box-shadow 0.3s;
}

.campaign-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.campaign-card h2 {
  margin-top: 0;
  font-size: 1.5rem;
}

.button-group {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: background 0.3s, transform 0.3s;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: #d9534f;
  color: #fff;
}

.btn-primary:hover {
  background: #c94c4c;
}
</style>
