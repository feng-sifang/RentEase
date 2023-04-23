import {createRouter, createWebHashHistory, } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/LoginView.vue'
import PropertyList from "../views/PropertyList.vue";
import AddProperty from "@/views/AddProperty.vue";
import AddProperty_test from "@/views/AddProperty_test.vue";

const routes = [
    {
        path: '/',
        component: HomeView,
    },
    {
        path: '/login',
        component: AboutView
    },
    {
        path: '/property_list',
        component: PropertyList
    },
    {
        path: '/add_property',
        component: AddProperty
    },
    {
        path: '/add_property_test',
        component: AddProperty_test
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
