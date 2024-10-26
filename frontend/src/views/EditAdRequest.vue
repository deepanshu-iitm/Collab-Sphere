<template>
  <div class="edit-ad-request-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Edit Ad Request</h1>
      </div>
    </header>
    <div class="form-container">
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="influencer_id">Influencer ID:</label>
          <input type="text" v-model="adRequest.influencer_id" id="influencer_id" required />
        </div>
        <div class="form-group">
          <label for="messages">Messages:</label>
          <textarea v-model="adRequest.messages" id="messages" required></textarea>
        </div>
        <div class="form-group">
          <label for="requirements">Requirements:</label>
          <textarea v-model="adRequest.requirements" id="requirements" required></textarea>
        </div>
        <div class="form-group">
          <label for="payment_amount">Payment Amount:</label>
          <input type="number" v-model.number="adRequest.payment_amount" id="payment_amount" required />
        </div>
        <div class="form-group">
          <label for="status">Status:</label>
          <select v-model="adRequest.status" id="status" required>
            <option value="pending">Pending</option>
            <option value="approved">Approved</option>
            <option value="rejected">Rejected</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary" :disabled="loading">
          <span v-if="loading">Updating...</span>
          <span v-else>Update</span>
        </button>
        <p v-if="error" class="error-message">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      adRequest: {
        influencer_id: '',
        messages: '',
        requirements: '',
        payment_amount: '',
        status: 'pending'
      },
      loading: false,
      error: null
    };
  },
  created() {
    this.fetchAdRequest();
  },
  methods: {
    fetchAdRequest() {
      const token = localStorage.getItem('access_token');
      const campaignId = this.$route.params.campaignId;
      const adRequestId = this.$route.params.adRequestId;

      this.loading = true;
      this.error = null;

      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${campaignId}/adrequests/${adRequestId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch ad request');
        }
        return response.json();
      })
      .then(data => {
        this.adRequest = data;
      })
      .catch(error => {
        this.error = error.message;
        console.error('Error fetching ad request:', error);
      })
      .finally(() => {
        this.loading = false;
      });
    },
    submitForm() {
      const token = localStorage.getItem('access_token');
      const campaignId = this.$route.params.campaignId;
      const adRequestId = this.$route.params.adRequestId;

      this.loading = true;
      this.error = null;

      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${campaignId}/adrequests/${adRequestId}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.adRequest)
      })
      .then(response => {
        if (response.ok) {
          this.$router.push(`/sponsor/campaigns/${campaignId}/adrequests`);
        } else {
          throw new Error('Failed to update ad request');
        }
      })
      .catch(error => {
        this.error = error.message;
        console.error('Error updating ad request:', error);
      })
      .finally(() => {
        this.loading = false;
      });
    }
  }
}
</script>

<style scoped>
.edit-ad-request-page {
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

.form-container {
  margin-top: 30px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-weight: bold;
  margin-bottom: 5px;
}

.form-group input,
.form-group textarea,
.form-group select {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.btn {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: background 0.3s, transform 0.3s;
}

.btn-primary {
  background: #d9534f;
  color: #fff;
}

.btn-primary:hover {
  background: #c94c4c;
}

.error-message {
  color: red;
  font-size: 0.875rem;
}
</style>
