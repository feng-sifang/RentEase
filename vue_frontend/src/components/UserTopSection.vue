<template>
  <section class="bg-dark py-5 user-header">
    <div class="container">
      <div class="row align-items-center mt-2 mb-5 pb-4">
        <div class="col">
          <!-- Heading -->
          <h1 class="text-white mb-2">{{ this.userType }} Profile</h1>
          <!-- Text -->
          <h6 class="font-weight-normal text-white-50 mb-0">
            Settings for
            <a class="text-reset" href="mailto:yoursite@gmail.com">
              {{ this.email }}
            </a>
          </h6>
        </div>
        <div class="col-auto">
          <!-- Button -->
          <router-link to="/" class="btn btn-sm btn-primary" @click="logOut">
            Log Out
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'UserTopSection',

  data () {
    return {
      userType: '',
      email: '',
    }
  },

  methods: {
    async getUserProfile () {
      try {
        const response = (await this.axios.get('/get-user-profile/')).data
        if (response.success) {
          console.log('get:', response)
          this.userType = response['user_type']
          this.email = response['email']
        }
        console.log('User Profile', response)
      } catch (error) {
        console.log(error)
      }
    },

    async logOut () {
      try {
        const response = (await this.axios.get('/logout/')).data
        if (response.success) {
          console.log('Logged out successfully')
        }
      } catch (error) {
        console.log(error)
      }
    },
  },

  async mounted () {
    await this.getUserProfile()
  },
}
</script>
