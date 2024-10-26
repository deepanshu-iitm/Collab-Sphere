<template>
  <div class="dashboard">
    <header class="dashboard-header">
      <h2 class="header-title">Influencer Dashboard</h2>
    </header>
    <section class="search-section">
      <input v-model="searchQuery" @input="searchAdRequests" placeholder="Search ad requests..." />
    </section>
    <section class="ad-requests-container">
      <div class="ad-request-card" v-for="adRequest in filteredAdRequests" :key="adRequest.id">
        <div class="card-body">
          <h3 class="card-title">Ad Request #{{ adRequest.id }}</h3>
          <p><strong>Campaign ID:</strong> {{ adRequest.campaign_id }}</p>
          <p><strong>Requirements:</strong> {{ adRequest.requirements }}</p>
          <p><strong>Payment Amount:</strong> {{ adRequest.payment_amount }}</p>
          <p><strong>Status:</strong> {{ adRequest.status }}</p>
        </div>
        <div class="button-group">
          <button @click="acceptAdRequest(adRequest.id)" class="btn btn-success">Accept</button>
          <button @click="rejectAdRequest(adRequest.id)" class="btn btn-danger">Reject</button>
          <button @click="negotiateAdRequest(adRequest)" class="btn btn-warning">Negotiate</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'InfluencerDashboard',
  data() {
    return {
      adRequests: [],
      filteredAdRequests: [],
      searchQuery: ''
    };
  },
  mounted() {
    this.fetchAdRequests();
  },
  methods: {
    getAuthHeaders() {
      const token = localStorage.getItem('access_token');
      return {
        headers: {
          Authorization: `Bearer ${token}`
        }
      };
    },
    async fetchAdRequests() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/influencer/ad_requests', this.getAuthHeaders());
        this.adRequests = response.data;
        this.filteredAdRequests = this.adRequests;
      } catch (error) {
        console.error('Error fetching ad requests', error);
      }
    },
    searchAdRequests() {
      const query = this.searchQuery.toLowerCase();
      this.filteredAdRequests = this.adRequests.filter(adRequest =>
        adRequest.campaign_id.toString().includes(query) ||
        adRequest.requirements.toLowerCase().includes(query)
      );
    },
    async acceptAdRequest(adRequestId) {
      try {
        await axios.post(`http://127.0.0.1:5000/influencer/ad_requests/${adRequestId}/accept`, {}, this.getAuthHeaders());
        this.fetchAdRequests();
      } catch (error) {
        console.error('Error accepting ad request', error);
      }
    },
    async rejectAdRequest(adRequestId) {
      try {
        await axios.post(`http://127.0.0.1:5000/influencer/ad_requests/${adRequestId}/reject`, {}, this.getAuthHeaders());
        this.fetchAdRequests();
      } catch (error) {
        console.error('Error rejecting ad request', error);
      }
    },
    async negotiateAdRequest(adRequest) {
      const newPaymentAmount = prompt("Enter your proposed payment amount:", adRequest.payment_amount);
      if (newPaymentAmount !== null) {
        try {
          await axios.post(`http://127.0.0.1:5000/influencer/ad_requests/${adRequest.id}/negotiate`, {
            payment_amount: newPaymentAmount
          }, this.getAuthHeaders());
          this.fetchAdRequests();
        } catch (error) {
          console.error('Error negotiating ad request', error);
        }
      }
    }
  }
};
</script>

<style scoped>
.dashboard {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.dashboard-header {
  background: linear-gradient(to right, #e07a7a, #d9534f);
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
}

.dashboard-header h2 {
  font-size: 2rem;
  margin: 0;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.search-section {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-section input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  max-width: 500px;
}

.ad-requests-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.ad-request-card {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  padding: 20px;
  box-sizing: border-box;
}

.card-body {
  margin-bottom: 20px;
}

.card-title {
  font-size: 1.2rem;
  color: #333;
  margin-bottom: 10px;
}

.button-group {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.btn {
  padding: 10px 20px;
  font-size: 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  color: #fff;
  text-align: center;
}

.btn-success {
  background-color: #28a745;
}

.btn-danger {
  background-color: #dc3545;
}

.btn-warning {
  background-color: #ffc107;
}
</style>
