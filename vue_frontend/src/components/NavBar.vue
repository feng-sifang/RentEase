<template>
  <nav v-if="waitCheckLogin" class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand text-success logo" href="/">
        <img class="img-fluid" src="/static/picture/logo.svg" alt=""/>
      </a>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item dropdown">
            <router-link
              to="/user-profile/"
              class="nav-link"
              id="navbarDropdownPortfolio">
              My Account
            </router-link>
          </li>
        </ul>

        <!--    if user logged in    -->
        <div v-if="displayUserName" class="my-2 my-lg-0">
          <ul class="list-inline main-nav-right">
            <li class="list-inline-item">
              <router-link to="/user-profile/" class="btn btn-link btn-sm">
                Hi, {{ this.userFirstName }}
              </router-link>
            </li>
          </ul>
        </div>

        <!--    if user not logged in    -->
        <div v-else class="my-2 my-lg-0">
          <ul class="list-inline main-nav-right">
            <li class="list-inline-item">
              <router-link to="/login/" class="btn btn-link btn-sm">Login</router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/register/" class="btn btn-success btn-sm">Sign Up</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>


export default {
  name: 'NavBar',

  data () {
    return {
      waitCheckLogin: false,
      displayUserName: false,
      userFirstName: '',
    }
  },

  methods: {
    async checkLogin () {
      const response = (await this.axios.get('/get-user-profile/')).data
      this.displayUserName = !!response['is_logged_in']
      this.userFirstName = response['first_name']
      this.waitCheckLogin = true
    },
  },

  // check if data is passed from parent component
  async mounted () {
    await this.checkLogin()
  },
}
</script>