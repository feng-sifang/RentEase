import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/login',
    component: AboutView
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
