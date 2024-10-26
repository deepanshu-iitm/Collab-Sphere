<template>
  <div>
    <!-- Header Section -->
    <header class="hero">
      <div class="hero-content">
        <h1>
          Welcome to <br> CollabSphere
        </h1>
        <p>Transforming How Brands and Influencers Connect and Collaborate</p>
        <div class="cta-buttons">
          <router-link to="/login" class="cta-button">Login</router-link>
          <router-link to="/register" class="cta-button">Sign Up</router-link>
        </div>
      </div>
    </header>

    <!-- About Section -->
    <section class="about">
      <div class="container">
        <h2>About Us</h2>
        <p>At CollabSphere, we bridge the gap between brands and influencers with an intuitive platform designed to foster successful partnerships. Our solution streamlines campaign management, enhances influencer discovery, and provides actionable insights to optimize your marketing strategies.</p>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features">
      <div class="container">
        <h2>Powerful Features to Elevate Your Campaigns</h2>
        <div class="feature-cards">
          <div class="feature-card">
            <div class="icon">🔧</div>
            <h3>Streamlined Campaign Management</h3>
            <p>Organize and oversee multiple campaigns effortlessly. Our platform provides tools to set up, manage, and track campaigns, ensuring every detail is handled smoothly.</p>
          </div>
          <div class="feature-card">
            <div class="icon">🔍</div>
            <h3>Advanced Influencer Search</h3>
            <p>Find the ideal influencers for your campaigns using advanced filters such as niche, reach, and engagement metrics. Tailor your search to match your campaign objectives perfectly.</p>
          </div>
          <div class="feature-card">
            <div class="icon">🤝</div>
            <h3>Seamless Collaboration and Negotiation</h3>
            <p>Communicate directly with influencers through our platform. Negotiate terms, finalize agreements, and manage all aspects of your collaborations in one place.</p>
          </div>
          <div class="feature-card">
            <div class="icon">📊</div>
            <h3>Insightful Analytics and Reporting</h3>
            <p>Gain valuable insights into your campaigns with detailed analytics. Track performance, measure ROI, and make data-driven decisions to enhance future campaigns.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-it-works">
      <div class="container">
        <h2>How It Works</h2>
        <div class="steps">
          <div class="step">
            <div class="step-number">1</div>
            <h3>Create Your Account</h3>
            <p>Choose your role—Admin, Sponsor, or Influencer—and complete your profile setup to start using the platform.</p>
          </div>
          <div class="step">
            <div class="step-number">2</div>
            <h3>Build and Manage Campaigns</h3>
            <p>Sponsors can launch campaigns, set goals, and manage ad requests. Influencers can browse and accept opportunities that align with their brand.</p>
          </div>
          <div class="step">
            <div class="step-number">3</div>
            <h3>Engage and Negotiate</h3>
            <p>Influencers and Sponsors can negotiate terms and finalize agreements directly through our secure platform.</p>
          </div>
          <div class="step">
            <div class="step-number">4</div>
            <h3>Analyze and Optimize</h3>
            <p>Use our comprehensive analytics tools to track campaign performance, gather insights, and refine your strategies for maximum impact.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- User Benefits Section -->
    <section class="user-benefits">
      <div class="container">
        <h2>Benefits for Every User</h2>
        <div class="benefits">
          <div class="benefit">
            <h3>For Admins</h3>
            <p>Manage all users and campaigns from a central dashboard. Oversee operations, approve new sponsors, and maintain platform integrity with comprehensive control and monitoring tools.</p>
          </div>
          <div class="benefit">
            <h3>For Sponsors</h3>
            <p>Launch impactful campaigns with ease. Track campaign progress, evaluate performance metrics, and engage with influencers to achieve your marketing goals effectively.</p>
          </div>
          <div class="benefit">
            <h3>For Influencers</h3>
            <p>Access a wide range of campaigns and opportunities. Manage ad requests, negotiate terms, and showcase your influence to drive engagement and growth.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Us Section -->
    <section class="contact-us">
      <div class="container">
        <h2>Contact Us</h2>
        <p>We're here to help! If you have any questions, need assistance, or want to provide feedback, feel free to reach out to us:</p>
        <p>Email: <a href="mailto:deepanshupathak03@gmail.com">deepanshupathak03@gmail.com</a></p>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <div class="container">
        <p>CollabSphere.<br>Made with ❤️ by Deepanshu</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  color: #333;
  background: #f4f4f4;
}

a {
  text-decoration: none;
  color: #d9534f;
}

a:hover {
  text-decoration: underline;
}

/* Header */
.hero {
  background: linear-gradient(to right, #e07a7a, #d9534f);
  color: #fff;
  text-align: left;
  padding: 120px 20px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hero-content {
  max-width: 900px;
}

.hero-content h1 {
  font-size: 4rem;
  margin: 0;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.hero-content p {
  font-size: 1.8rem;
  margin-top: 20px;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
}

.cta-buttons {
  margin-top: 30px;
}

.cta-button {
  background: #fff;
  color: #d9534f;
  padding: 15px 30px;
  border-radius: 5px;
  font-size: 1.2rem;
  margin: 0 10px;
  display: inline-block;
  transition: background 0.3s, color 0.3s;
}

.cta-button:hover {
  background: #d9534f;
  color: #fff;
}

/* About Section */
.about {
  background: #fff;
  padding: 80px 20px;
}

.about .container {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.about h2 {
  font-size: 2.8rem;
  margin-bottom: 20px;
}

.about p {
  font-size: 1.3rem;
  line-height: 1.8;
}

/* Features Section */
.features {
  background: #f9f9f9;
  padding: 80px 20px;
}

.features .container {
  max-width: 1200px;
  margin: 0 auto;
}

.features h2 {
  font-size: 2.8rem;
  margin-bottom: 40px;
  text-align: center;
}

.feature-cards {
  display: flex;
  justify-content: space-between;
  flex-wrap: nowrap;
  overflow-x: auto;
}

.feature-card {
  background: #fff;
  padding: 20px;
  margin: 15px;
  border-radius: 10px;
  text-align: center;
  flex: 1;
  min-width: 250px;
  max-width: 270px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.feature-card .icon {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.feature-card h3 {
  font-size: 1.5rem;
  margin: 10px 0;
}

.feature-card p {
  font-size: 1rem;
  color: #666;
}

/* How It Works Section */
.how-it-works {
  background: #fff;
  padding: 80px 20px;
}

.how-it-works .container {
  max-width: 1200px;
  margin: 0 auto;
}

.how-it-works h2 {
  font-size: 2.8rem;
  margin-bottom: 40px;
  text-align: center;
}

.steps {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.step {
  background: #fff;
  padding: 30px;
  margin: 15px;
  border-radius: 10px;
  text-align: center;
  flex: 1;
  min-width: 240px;
  max-width: 280px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.step-number {
  background: #d9534f;
  color: #fff;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin: 0 auto 15px;
}

.step h3 {
  font-size: 1.8rem;
  margin: 15px 0;
}

.step p {
  font-size: 1rem;
  color: #666;
}

/* User Benefits Section */
.user-benefits {
  background: #f9f9f9;
  padding: 80px 20px;
}

.user-benefits .container {
  max-width: 1200px;
  margin: 0 auto;
}

.user-benefits h2 {
  font-size: 2.8rem;
  margin-bottom: 40px;
  text-align: center;
}

.benefits {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.benefit {
  background: #fff;
  padding: 30px;
  margin: 15px;
  border-radius: 10px;
  text-align: center;
  flex: 1;
  min-width: 240px;
  max-width: 280px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.benefit h3 {
  font-size: 1.8rem;
  margin: 15px 0;
}

.benefit p {
  font-size: 1.1rem;
  color: #666;
}

/* Contact Us Section */
.contact-us {
  background: #fff;
  padding: 80px 20px;
}

.contact-us .container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.contact-us h2 {
  font-size: 2.8rem;
  margin-bottom: 20px;
}

.contact-us p {
  font-size: 1.3rem;
  line-height: 1.8;
}

/* Footer */
footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 50px 20px;
}

footer .container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

footer p {
  margin: 5px 0;
}
</style>
