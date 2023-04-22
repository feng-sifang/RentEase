import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

const app = createApp(App)
app.use(router)
app.use(VueAxios, axios)
app.mount('#app')

// add global variable， this may cause coupling
// if you want to avoid coupling, you can use vuex
// but now for convenience, we use this method
app.config.globalProperties.$isUserLoggedIn = false
app.config.globalProperties.$userFirstName = ''
app.config.globalProperties.$userEmail = ''
app.config.globalProperties.$userType = ''

