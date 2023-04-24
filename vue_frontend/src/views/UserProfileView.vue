<template>
  <nav-bar></nav-bar>
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
  <!-- User Profile -->
  <section class="section-padding pt-0 user-pages-main">
    <div class="container">
      <div class="row">
        <user-side-bar></user-side-bar>
        <div class="col-lg-9 col-md-9">
          <form>
            <div class="card padding-card">

              <!-- renter profile -->
              <div v-if="this.userType==='Renter'" class="card-body">
                <h5 class="card-title mb-4">
                  Personal Details
                </h5>
                <div class="form-group">
                  <label>First Name <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.firstName"
                  />
                </div>
                <div class="form-group">
                  <label>Last Name <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.lastName"
                  />
                </div>
                <div class="form-group">
                  <label>Email Address <span class="text-danger">*</span></label>
                  <input
                    type="email"
                    class="form-control"
                    v-model="this.email"
                  />
                </div>
                <div class="form-group">
                  <label>Phone</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.phone"
                  />
                </div>
                <div class="form-group">
                  <label>Location</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.location"
                  />
                </div>
                <div class="form-group">
                  <label>Rental Preferences</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.rentalPreferences"
                  />
                </div>
                <div class="form-group">
                  <label>Desired Move in Date</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.desiredMoveInDate"
                  />
                </div>
                <div class="form-group">
                  <label>Preferred Location</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.preferredLocation"
                  />
                </div>
                <div class="form-group">
                  <label>Budget</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.budget"
                  />
                </div>
              </div>

              <!-- agent profile -->
              <div v-if="this.userType==='Agent'" class="card-body">
                <h5 class="card-title mb-4">
                  Personal Details
                </h5>
                <div class="form-group">
                  <label>First Name <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.firstName"
                  />
                </div>
                <div class="form-group">
                  <label>Last Name <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.lastName"
                  />
                </div>
                <div class="form-group">
                  <label>Email Address <span class="text-danger">*</span></label>
                  <input
                    type="email"
                    class="form-control"
                    v-model="this.email"
                  />
                </div>
                <div class="form-group">
                  <label>Phone</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.phone"
                  />
                </div>
                <div class="form-group">
                  <label>Location</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.location"
                  />
                </div>
                <div class="form-group">
                  <label>Job Title</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.jobTitle"
                  />
                </div>
                <div class="form-group">
                  <label>Company</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.company"
                  />
                </div>
                <div class="form-group">
                  <label>Contact Information</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.contactInformation"
                  />
                </div>
              </div>
            </div>

            <button @click="saveUserProfile" type="submit" class="btn btn-success">
              SAVE EDITS
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
  <!-- End User Profile -->
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import UserSideBar from '@/components/UserSideBar.vue'

export default {
  name: 'UserProfileView',

  data () {
    return {
      userType: '',
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      location: '',
      rentalPreferences: '',
      desiredMoveInDate: '',
      preferredLocation: '',
      budget: '',
      jobTitle: '',
      company: '',
      contactInformation: '',
    }
  },

  methods: {
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

    async getUserProfile () {
      try {
        const response = (await this.axios.get('/get-user-profile/')).data
        if (response.success) {
          console.log('get:', response)
          this.userType = response['user_type']
          this.firstName = response['first_name']
          this.lastName = response['last_name']
          this.email = response['email']
          this.phone = response['phone']
          this.location = response['location']
          this.rentalPreferences = response['rental_preferences']
          this.desiredMoveInDate = response['desired_move_in_date']
          this.preferredLocation = response['preferred_location']
          this.budget = response['budget']
          this.jobTitle = response['job_title']
          this.company = response['company']
          this.contactInformation = response['contact_information']
        }
        console.log('User Profile', response)
      } catch (error) {
        console.log(error)
      }
    },

    async saveUserProfile (event) {
      event.preventDefault()

      const data = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        phone: this.phone,
        location: this.location,
        rental_preferences: this.rentalPreferences,
        desired_move_in_date: this.desiredMoveInDate,
        preferred_location: this.preferredLocation,
        budget: this.budget,
        job_title: this.jobTitle,
        company: this.company,
        contact_information: this.contactInformation,
      }

      try {
        const response = (await this.axios.post('/save-user-profile/', data)).data
        if (response.success) {
          alert('New User Profile Saved')
          console.log('User Profile New Profile', data)
        }
      } catch (error) {
        console.log(error)
      }
    },
  },

  components: {
    UserSideBar,
    NavBar,
  },

  async mounted () {
    await this.getUserProfile()
  },
}
</script>