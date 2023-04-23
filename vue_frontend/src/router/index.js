import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import UserProfileView from '../views/UserProfileView.vue'
import PropertyList from '../views/PropertyList.vue'
import AddProperty from '../views/AddProperty.vue'

const routes = [
  {
    path: '/',
    component: HomeView,
  },
  {
    path: '/login/',
    component: LoginView,
  },
  {
    path: '/register/',
    component: RegisterView,
  },
  {
    path: '/user-profile/',
    component: UserProfileView,
  },
  {
    path: '/property-list',
    component: PropertyList,
  },
  {
    path: '/add_property',
    component: AddProperty,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
