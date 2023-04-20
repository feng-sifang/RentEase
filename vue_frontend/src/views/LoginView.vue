<template>
  <section class="hv-100">
    <div class="container hv-100">
      <div class="row align-items-center hv-100">
        <div class="col-lg-4 col-md-4 mx-auto">
          <div class="card padding-card mb-0">
            <div class="card-body">
              <h5 class="card-title mb-4">Login</h5>
              <form>
                <div class="form-group">
                  <!-- "for" attribute connect to the input's id can help to locate to input even when user click label -->
                  <label for="login-email">Email Address<span class="text-danger">*</span></label>
                  <input
                    type="email" class="form-control" name="login-email" id="login-email"
                    placeholder="Enter Email Address" v-model="loginEmail"/>
                </div>
                <div class="form-group">
                  <label for="login-password">Password<span class="text-danger">*</span></label>
                  <input
                    type="password" class="form-control" name="login-password" id="login-password"
                    placeholder="Enter Password" v-model="loginPassword"/>
                </div>
                <div class="form-group">
                  <div class="custom-control custom-checkbox">
                    <input
                      type="checkbox" class="custom-control-input" id="customControlAutosizing" name="remember_me"/>
                    <label class="custom-control-label" for="customControlAutosizing">
                      Remember Me
                    </label>
                  </div>
                </div>
                <button type="submit" class="btn btn-success btn-block" @click="loginCheck">
                  SIGN IN
                </button>
              </form>
              <div class="mt-4 text-center">
                Don't have an account?
                <router-link to="/register/">Register</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'LoginView',
  data () {
    return {
      loginEmail: '',
      loginPassword: '',
      loginStatus: null,
      userType: null,
    }
  },
  methods: {
    async loginCheck (event) {
      event.preventDefault()
      const data = {
        'login-email': this.loginEmail,
        'login-password': this.loginPassword,
      }
      try {
        const response = await this.axios.post('/post-signin/', data)

        if (response.data.success) {
          // {'success': True}
          this.loginStatus = true
          this.userType = response.data['user-type']
        } else {
          this.loginStatus = false
          alert('Incorrect email or password. Please try again.')
        }
      } catch (error) {
        this.loginStatus = false
        console.error(error)
      }
    },
  },
}
</script>