import {
    createRouter,
    createWebHashHistory,
} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import UserProfileView from '../views/UserProfileView.vue'
import PropertyList from '../views/PropertyList.vue'
import AddProperty from '../views/AddProperty.vue'
import UserCreditCard from '../views/UserCreditCard.vue'
import AddCreditCard from '@/views/AddCreditCard.vue'
import MyBookingsView from '@/views/MyBookingsView.vue'
import RewordPointsView from '@/views/RewordPointsView.vue'
import EditProperty from "@/views/EditProperty.vue";

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
        path: '/edit-property/',
        component: EditProperty,
    },
    {
        path: '/user-creditcard/',
        component: UserCreditCard,
    },
    {
        path: '/user-add-creditcard/',
        component: AddCreditCard,
    },
    {
        path: '/my-bookings/',
        component: MyBookingsView,
    },
    {
        path: '/reword-points/',
        component: RewordPointsView,
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router
