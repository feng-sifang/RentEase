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
            <router-link to="/my-bookings/" class="nav-link">
              My Bookings
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Renter' && this.ifCreditCard === true">
            <router-link to="/user-creditcard/" class="nav-link">
              Credit Card
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Renter'">
            <router-link to="/user-add-creditcard/" class="nav-link">
              Add Credit Card
            </router-link>
          </li>
          <li class="nav-item" v-if="this.userType==='Renter'">
            <router-link to="/reword-points/" class="nav-link">
              Reword Points
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
      ifCreditCard: false,
    }
  },

  methods: {
    async checkUserType () {
      const response = await this.axios.get('/get-user-profile/')
      this.userType = response.data['user_type']
    },

    async checkCreditCard () {
      const response = await this.axios.get('/get-user-creditcard/')
      if (response.data['success']) {
        console.log(response.data)
        this.ifCreditCard = true
      }
    },
  },

  async mounted () {
    await this.checkUserType()
    await this.checkCreditCard()
  },
}
</script>
