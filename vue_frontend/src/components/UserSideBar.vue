<template>
  <div class="col-lg-3 col-md-3">
    <!-- Collapse -->
    <div class="card padding-card tab-view user-pages-sidebar">
      <div class="card-body">
        <!-- Heading -->
        <h6 class="text-uppercase mt-0 mb-3">Account</h6>
        <ul class="nav">
          <li class="nav-item">
            <router-link to="/user-profile/" class="nav-link">
              User Profile
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Renter'">
            <router-link to="user-fav-prop" class="nav-link">
              Favorite Properties
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Renter'">
            <router-link to="/user-creditcard/" class="nav-link">
              Credit Card
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Renter'">
            <router-link to="user-reword" class="nav-link">
              Reword Points
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Agent'">
            <router-link to="" class="nav-link">
              Add Property
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserSideBar',

  data () {
    return {
      userType: '',
    }
  },

  methods: {
    async checkUserType () {
      const response = await this.axios.get('/get-user-profile/')
      this.userType = response.data['user_type']
    },
  },

  async mounted () {
    await this.checkUserType()
  },
}
</script>
