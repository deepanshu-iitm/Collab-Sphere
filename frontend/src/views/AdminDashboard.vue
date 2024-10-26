<template>
  <div>
    <header class="dashboard-header">
      <h2>Admin Dashboard</h2>
    </header>
    <section class="dashboard-content">
      <!-- Platform Statistics Card -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Platform Statistics</h5>
          <p class="card-text">Overview of platform activity.</p>
          <p><strong>Active Users:</strong> {{ activeUsers }}</p>
          <p><strong>Active Campaigns:</strong> {{ activeCampaigns }}</p>
          <p><strong>Ad Requests:</strong> {{ adRequests }}</p>
        </div>
      </div>

      <!-- Pending Sponsors Card -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Pending Sponsors</h5>
          <ul v-if="pendingSponsors.length > 0" class="pending-sponsors-list">
            <li v-for="sponsor in pendingSponsors" :key="sponsor.id" class="pending-sponsor-item">
              <p><strong>Email:</strong> {{ sponsor.email }}</p>
              <button @click="approveSponsor(sponsor.id)" class="approve-button">Approve</button>
              <button @click="showFlagUserModal(sponsor.id)" class="flag-button">Flag</button>
            </li>
          </ul>
          <p v-else class="no-pending-sponsors">No pending sponsors.</p>
        </div>
      </div>

      <!-- Flag User Modal -->
      <div v-if="showFlagModal" class="modal">
        <div class="modal-content">
          <span class="close" @click="closeFlagModal">&times;</span>
          <h2>Flag User</h2>
          <label for="flagReason">Reason:</label>
          <textarea id="flagReason" v-model="flagReason"></textarea>
          <button @click="flagUser">Submit</button>
        </div>
      </div>

      <!-- Display Flags -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Flagged Items</h5>
          <ul v-if="flags.length > 0" class="flags-list">
            <li v-for="flag in flags" :key="flag.id" class="flag-item">
              <p><strong>Type:</strong> {{ flag.flagged_type }}</p>
              <p><strong>ID:</strong> {{ flag.flagged_id }}</p>
              <p><strong>Reason:</strong> {{ flag.reason }}</p>
              <p><strong>Timestamp:</strong> {{ flag.timestamp }}</p>
            </li>
          </ul>
          <p v-else>No flagged items.</p>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'AdminDashboard',
  data() {
    return {
      activeUsers: 0,
      activeCampaigns: 0,
      adRequests: 0,
      pendingSponsors: [],
      flags: [],
      showFlagModal: false,
      flagReason: '',
      flagUserId: null,
    }
  },
  mounted() {
    this.fetchStats();
    this.fetchPendingSponsors();
    this.fetchFlags();
  },
  methods: {
    async fetchStats() {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('http://127.0.0.1:5000/admin/dashboard', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.activeUsers = response.data.users_count;
        this.activeCampaigns = response.data.campaigns_count;
        this.adRequests = response.data.ad_requests_count;
      } catch (error) {
        console.error('Error fetching statistics', error);
      }
    },
    async fetchPendingSponsors() {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('http://127.0.0.1:5000/admin/pending_sponsors', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.pendingSponsors = response.data;
      } catch (error) {
        console.error('Error fetching pending sponsors', error);
      }
    },
    async approveSponsor(userId) {
      try {
        const token = localStorage.getItem('access_token');
        await axios.post('http://127.0.0.1:5000/admin/approve_sponsor', { user_id: userId }, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.fetchPendingSponsors();
      } catch (error) {
        console.error('Error approving sponsor', error);
      }
    },
    async fetchFlags() {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('http://127.0.0.1:5000/admin/flags', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.flags = response.data;
      } catch (error) {
        console.error('Error fetching flags', error);
      }
    },
    showFlagUserModal(userId) {
      this.showFlagModal = true;
      this.flagUserId = userId;
    },
    closeFlagModal() {
      this.showFlagModal = false;
      this.flagReason = '';
    },
    async flagUser() {
      try {
        const token = localStorage.getItem('access_token');
        await axios.post('http://127.0.0.1:5000/admin/flag_user', {
          user_id: this.flagUserId,
          reason: this.flagReason
        }, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.closeFlagModal();
        this.fetchFlags();
      } catch (error) {
        console.error('Error flagging user', error);
      }
    }
  }
}
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
  font-size: 2.5rem;
  margin: 0;
  font-weight: bold;
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.card {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  flex: 1;
  min-width: 250px;
}

.card-body {
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 1.8rem;
  color: #d9534f;
  margin-bottom: 15px;
}

.pending-sponsors-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.pending-sponsor-item {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 10px;
}

.no-pending-sponsors {
  color: #999;
  font-style: italic;
}

.approve-button {
  background: #5cb85c;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.approve-button:hover {
  background: #4cae4c;
}

.modal {
  display: flex;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border-radius: 8px;
  width: 500px;
  max-width: 90%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.flag-button {
  background-color: #d9534f;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 10px;
}

.flag-button:hover {
  background-color: #c9302c;
}
</style>
