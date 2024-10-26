<template>
  <div class="adrequests-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Ad Requests for {{ campaignName }}</h1>
        <button class="btn btn-primary" @click="createNewAdRequest">Create New Ad Request</button>
      </div>
    </header>
    <div class="adrequest-list">
      <div v-for="adRequest in adRequests" :key="adRequest.id" class="adrequest-card">
        <h2>Ad Request ID: {{ adRequest.id }}</h2>
        <p><strong>Influencer ID:</strong> {{ adRequest.influencer_id || 'N/A' }}</p>
        <p><strong>Messages:</strong> {{ adRequest.messages || 'N/A' }}</p>
        <p><strong>Requirements:</strong> {{ adRequest.requirements || 'N/A' }}</p>
        <p><strong>Payment Amount:</strong> {{ adRequest.payment_amount || 'N/A' }}</p>
        <p><strong>Status:</strong> {{ adRequest.status || 'N/A' }}</p>
        <div class="button-group">
          <button class="btn btn-warning" @click="editAdRequest(adRequest.id)">Edit</button>
          <button class="btn btn-danger" @click="deleteAdRequest(adRequest.id)">Delete</button>
        </div>
      </div>
      <p v-if="!adRequests.length">No ad requests available.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdRequestsList',
  data() {
    return {
      campaignId: null,
      campaignName: '',
      adRequests: []
    };
  },
  created() {
    this.campaignId = this.$route.params.id;
    if (this.campaignId) {
      this.fetchAdRequests();
      this.fetchCampaignName();
    } else {
      console.error('Campaign ID is not defined');
    }
  },
  methods: {
    fetchAdRequests() {
      if (!this.campaignId) return;
      
      const token = localStorage.getItem('access_token');
      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${this.campaignId}/adrequests`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        this.adRequests = data;
      })
      .catch(error => {
        console.error('Error fetching ad requests:', error);
      });
    },
    fetchCampaignName() {
      if (!this.campaignId) return;
      
      const token = localStorage.getItem('access_token');
      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${this.campaignId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        this.campaignName = data.name;
      })
      .catch(error => {
        console.error('Error fetching campaign name:', error);
      });
    },
    createNewAdRequest() {
      this.$router.push(`/sponsor/campaigns/${this.campaignId}/adrequests/new`);
    },
    editAdRequest(adRequestId) {
      this.$router.push(`/sponsor/campaigns/${this.campaignId}/adrequests/${adRequestId}/edit`);
    },
    deleteAdRequest(adRequestId) {
      if (!this.campaignId) return;

      const token = localStorage.getItem('access_token');
      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${this.campaignId}/adrequests/${adRequestId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (response.ok) {
          this.fetchAdRequests();
        } else {
          throw new Error('Failed to delete ad request');
        }
      })
      .catch(error => {
        console.error('Error deleting ad request:', error);
      });
    }
  }
}
</script>

<style scoped>
.adrequests-page {
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

.adrequest-list {
  margin-top: 30px;
}

.adrequest-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
  padding: 20px;
  text-align: left;
  transition: transform 0.3s, box-shadow 0.3s;
}

.adrequest-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.adrequest-card h2 {
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

.btn-warning {
  background: #f0ad4e;
  color: #fff;
}

.btn-warning:hover {
  background: #ec971f;
}

.btn-danger {
  background: #d9534f;
  color: #fff;
}

.btn-danger:hover {
  background: #c9302c;
}
</style>
