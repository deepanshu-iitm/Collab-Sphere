<template>
  <div class="form-page">
    <h1>Edit Campaign</h1>
    <form @submit.prevent="submitForm" class="form-container">
      <div class="form-group">
        <label for="name">Campaign Name</label>
        <input type="text" class="form-control" id="name" v-model="name">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea class="form-control" id="description" v-model="description"></textarea>
      </div>
      <div class="form-group">
        <label for="start_date">Start Date</label>
        <input type="date" class="form-control" id="start_date" v-model="start_date">
      </div>
      <div class="form-group">
        <label for="end_date">End Date</label>
        <input type="date" class="form-control" id="end_date" v-model="end_date">
      </div>
      <div class="form-group">
        <label for="budget">Budget</label>
        <input type="number" class="form-control" id="budget" v-model="budget">
      </div>
      <div class="form-group">
        <label for="visibility">Visibility</label>
        <select class="form-control" id="visibility" v-model="visibility">
          <option value="">Select visibility</option>
          <option value="public">Public</option>
          <option value="private">Private</option>
        </select>
      </div>
      <div class="form-group">
        <label for="goals">Goals</label>
        <textarea class="form-control" id="goals" v-model="goals"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Save Changes</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.params.id,
      name: '',
      description: '',
      start_date: '',
      end_date: '',
      budget: '',
      visibility: '',
      goals: ''
    };
  },
  created() {
    this.fetchCampaign();
  },
  methods: {
    fetchCampaign() {
      const token = localStorage.getItem('access_token');
      fetch(`http://127.0.0.1:5000/sponsor/campaigns`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
        .then(response => response.json())
        .then(data => {
          this.name = data.name || '';
          this.description = data.description || '';
          this.start_date = data.start_date || '';
          this.end_date = data.end_date || '';
          this.budget = data.budget || '';
          this.visibility = data.visibility || '';
          this.goals = data.goals || '';
        })
        .catch(error => {
          console.error('Error fetching campaign:', error);
        });
    },
    submitForm() {
      // Create an object with only the fields that have values
      const campaign = {
        ...(this.name && { name: this.name }),
        ...(this.description && { description: this.description }),
        ...(this.start_date && { start_date: this.start_date }),
        ...(this.end_date && { end_date: this.end_date }),
        ...(this.budget && { budget: this.budget }),
        ...(this.visibility && { visibility: this.visibility }),
        ...(this.goals && { goals: this.goals })
      };
      const token = localStorage.getItem('access_token');
      fetch(`http://127.0.0.1:5000/sponsor/campaigns/${this.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(campaign)
      })
        .then(() => {
          this.$router.push('/sponsor/campaigns');
        })
        .catch(error => {
          console.error('Error updating campaign:', error);
        });
    }
  }
};
</script>

<style scoped>
.form-page {
  width: 70%;
  margin: 50px auto;
}
.form-container {
  max-width: 800px;
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
.btn-primary {
  background: #d9534f;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1.2rem;
  border: none;
  cursor: pointer;
  transition: background 0.3s, color 0.3s;
}
.btn-primary:hover {
  background: #e07a7a;
}
</style>
