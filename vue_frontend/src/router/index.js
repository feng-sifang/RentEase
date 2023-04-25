import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import UserProfileView from '../views/UserProfileView.vue'
import PropertyList from '../views/PropertyList.vue'
import AddProperty from '../views/AddProperty.vue'
import UserCreditCard from '../views/UserCreditCard.vue'
import AddCreditCard from '@/views/AddCreditCard.vue'

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
    path: '/property/list/',
    component: PropertyList,
  },
  {
    path: '/add-property/',
    component: AddProperty,
  },
  {
    path: '/user-creditcard/',
    component: UserCreditCard,
  },
  {
    path: '/user-add-creditcard/',
    component: AddCreditCard,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
