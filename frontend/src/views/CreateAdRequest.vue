<template>
  <div class="create-ad-request-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Create New Ad Request</h1>
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
          <input type="number" v-model="adRequest.payment_amount" id="payment_amount" required />
        </div>
        <div class="form-group">
          <label for="status">Status:</label>
          <select v-model="adRequest.status" id="status" required>
            <option value="pending">Pending</option>
            <option value="approved">Approved</option>
            <option value="rejected">Rejected</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
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
      campaignId: null
    };
  },
  created() {
    this.campaignId = this.$route.params.campaignId;
  },
  methods: {
    submitForm() {
      if (!this.campaignId) {
        console.error('Campaign ID is not available');
        return;
      }

      const token = localStorage.getItem('access_token');

      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${this.campaignId}/adrequests`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.adRequest)
      })
      .then(response => {
        if (response.ok) {
          this.$router.push(`/sponsor/campaigns/${this.campaignId}/adrequests`);
        } else {
          return response.json().then(data => {
            throw new Error(data.msg || 'Failed to create ad request');
          });
        }
      })
      .catch(error => {
        console.error('Error creating ad request:', error);
      });
    }
  }
}
</script>

<style scoped>
.create-ad-request-page {
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
</style>
