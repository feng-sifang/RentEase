<template>
  <body>
    <!-- Register -->
    <section class="hv-100">
      <div class="container">
        <div class="row align-items-center hv-100">
          <div class="col-lg-5 col-md-5 mx-auto">
            <div class="card padding-card mb-0">
              <div class="card-body">
                <h5 class="card-title mb-4">Register</h5>
                <form>
                  <div class="form-group">
                    <label for="first-name">First Name<span class="text-danger">*</span></label
                    ><input
                    id="first-name"
                    type="text"
                    class="form-control"
                    placeholder="Enter Full Name"
                    v-model="firstName"
                  />
                  </div>
                  <div class="form-group">
                    <label for="last-name">Last Name<span class="text-danger">*</span></label
                    ><input
                    id="last-name"
                    type="text"
                    class="form-control"
                    placeholder="Enter Full Name"
                    v-model="lastName"
                  />
                  </div>
                  <div class="form-group">
                    <label for="email-address">Email Address<span class="text-danger">*</span></label>
                    <input
                      id="email-address"
                      type="email"
                      class="form-control"
                      placeholder="Enter Email Address"
                      v-model="email"
                    />
                  </div>
                  <div class="form-group">
                    <label for="password">Password<span class="text-danger">*</span></label>
                    <input
                      id="password"
                      class="form-control"
                      placeholder="Enter Password"
                      v-model="password"
                    />
                  </div>

                  <div class="form-group">
                    <label for="user-type">User Type<span class="text-danger">*</span></label>
                    <select class="form-control" id="user-type" v-model="userType">
                      <option>Renter</option>
                      <option>Agent</option>
                    </select>
                  </div>

                  <button type="submit" class="btn btn-success btn-block" @click="registerCheck">
                    REGISTER
                  </button>
                </form>

                <div class="mt-4 text-center">Have an account -
                  <router-link to="/login/">Login</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- End Register -->
  </body>
</template>

<script>
export default {
  name: 'RegisterView',
  data () {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      userType: '',
    }
  },
  methods: {
    async registerCheck (event) {
      event.preventDefault()
      const data = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        password: this.password,
        user_type: this.userType,
      }
      const response = await this.axios.post('/post-register/', data)
      console.log(response)
      if (response.data.success) {
        alert('Register Success')
        this.$router.push({ path: '/login/' })
      }
    },
  },
}
</script>
