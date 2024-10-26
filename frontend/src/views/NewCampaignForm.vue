<template>
  <div class="form-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Create New Campaign</h1>
      </div>
    </header>
    <form @submit.prevent="submitForm" class="form-container">
      <div class="form-group">
        <label for="name">Campaign Name</label>
        <input type="text" class="form-control" id="name" v-model="name" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea class="form-control" id="description" v-model="description" required></textarea>
      </div>
      <div class="form-group">
        <label for="start_date">Start Date</label>
        <input type="date" class="form-control" id="start_date" v-model="startDate" required>
      </div>
      <div class="form-group">
        <label for="end_date">End Date</label>
        <input type="date" class="form-control" id="end_date" v-model="endDate" required>
      </div>
      <div class="form-group">
        <label for="budget">Budget</label>
        <input type="number" class="form-control" id="budget" v-model="budget" required>
      </div>
      <div class="form-group">
        <label for="visibility">Visibility</label>
        <select class="form-control" id="visibility" v-model="visibility" required>
          <option value="public">Public</option>
          <option value="private">Private</option>
        </select>
      </div>
      <div class="form-group">
        <label for="goals">Goals</label>
        <textarea class="form-control" id="goals" v-model="goals" required></textarea>
      </div>
      <button type="submit" class="cta-button">Create Campaign</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      description: '',
      startDate: '',
      endDate: '',
      budget: '',
      visibility: 'public',  // Default value
      goals: ''
    };
  },
  methods: {
    submitForm() {
      const token = localStorage.getItem('access_token');
      const campaign = {
        name: this.name,
        description: this.description,
        start_date: this.startDate,
        end_date: this.endDate,
        budget: this.budget,
        visibility: this.visibility,
        goals: this.goals
      };
      fetch('http://127.0.0.1:5000/sponsor/campaigns', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(campaign)
      })
        .then(response => {
        if (response.ok) {
          this.$router.push('/sponsor/campaigns');
        } else {
          return response.json().then(data => {
            throw new Error(data.msg || 'Failed to create campaign');
          });
        }
      })
        .catch(error => {
          console.error('Error creating campaign:', error);
        });
    }
  }
};
</script>

<style scoped>
.form-page {
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
.form-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 20px;
}
.form-control {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
.cta-button {
  background: #d9534f;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1.2rem;
  border: none;
  cursor: pointer;
  transition: background 0.3s, color 0.3s;
}
.cta-button:hover {
  background: #e07a7a;
}
</style>
