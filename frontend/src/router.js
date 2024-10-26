// router.js
import { createRouter, createWebHistory } from 'vue-router'
import store from './store'
import HomePage from './views/HomePage.vue'
import LoginPage from './views/LoginPage.vue'
import RegisterPage from './views/RegisterPage.vue'
import AdminDashboard from './views/AdminDashboard.vue'
import SponsorDashboard from './views/SponsorDashboard.vue'
import InfluencerDashboard from './views/InfluencerDashboard.vue'
import CampaignsPage from './views/CampaignsPage.vue';
import NewCampaignForm from './views/NewCampaignForm.vue';
import EditCampaignForm from './views/EditCampaignForm.vue';
import CampaignsList from './views/CampaignsList.vue';
import AdRequestsList from './views/AdRequestsList.vue';
import CreateAdRequest from './views/CreateAdRequest.vue';
import EditAdRequest from './views/EditAdRequest.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  {
    path: '/admin-dashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true, role: 'admin' }
  },
  {
    path: '/sponsor-dashboard',
    component: SponsorDashboard,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  {
    path: '/influencer-dashboard',
    component: InfluencerDashboard,
    meta: { requiresAuth: true, role: 'influencer' }
  },
  {
    path: '/sponsor/campaigns',
    name: 'CampaignsPage',
    component: CampaignsPage,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  {
    path: '/sponsor/campaigns/new',
    name: 'NewCampaignForm',
    component: NewCampaignForm,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  {
    path: '/sponsor/campaigns/:id/edit',
    name: 'EditCampaignForm',
    component: EditCampaignForm,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  { 
    path: '/sponsor/list-campaigns',
    name: 'CampaignsList',
    component: CampaignsList,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  { 
    path: '/sponsor/campaigns/:id/adrequests',
    name: 'AdRequestsList',
    component: AdRequestsList,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  { 
    path: '/sponsor/campaigns/:campaignId/adrequests/new',
    name: 'CreateAdRequest',
    component: CreateAdRequest,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
  { 
    path: '/sponsor/campaigns/:campaignId/adrequests/:adRequestId/edit',
    name: 'EditAdRequest',
    component: EditAdRequest,
    meta: { requiresAuth: true, role: 'sponsor' }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.state.isAuthenticated
  const userRole = store.state.userRole

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login')
    } else if (to.meta.role && to.meta.role !== userRole) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
