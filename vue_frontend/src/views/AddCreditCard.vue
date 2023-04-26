<template>
  <nav-bar></nav-bar>
  <user-top-section></user-top-section>
  <!-- User Profile -->
  <section class="section-padding pt-0 user-pages-main">
    <div class="container">
      <div class="row">
        <user-side-bar></user-side-bar>
        <div class="col-lg-9 col-md-9">
          <form>
            <div class="card padding-card">
              <div class="card-body">
                <h5 class="card-title mb-4">
                  Add New Credit Card
                </h5>
                <div class="form-group">
                  <label>Credit Card Number <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.number"
                  />
                </div>
                <div class="form-group">
                  <label>Holder's Name <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.holder_name"
                  />
                </div>
                <div class="form-group">
                  <label>Expiry Date <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.expiry_date"
                  />
                </div>
                <div class="form-group">
                  <label>CVV <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.cvv"
                  />
                </div>
                <div class="form-group">
                  <label>Country <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.country"
                  />
                </div>
                <div class="form-group">
                  <label>City <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.city"
                  />
                </div>
                <div class="form-group">
                  <label>Street <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.street"
                  />
                </div>
                <div class="form-group">
                  <label>ZIP <span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="this.zip"
                  />
                </div>
              </div>
            </div>

            <button type="submit" class="btn btn-success" @click="postNewCreditCard">
              ADD CARD
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import UserTopSection from '@/components/UserTopSection.vue'
import UserSideBar from '@/components/UserSideBar.vue'

export default {
  name: 'AddCreditCard',
  components: { UserSideBar, UserTopSection, NavBar },

  data () {
    return {
      number: '',
      holder_name: '',
      expiry_date: '',
      cvv: '',
      country: '',
      city: '',
      street: '',
      zip: '',
    }
  },

  methods: {
    async postNewCreditCard () {

      const response = await this.axios.post('/add-user-creditcard/', {
        number: this.number,
        holder_name: this.holder_name,
        expiry_date: this.expiry_date,
        cvv: this.cvv,
        country: this.country,
        city: this.city,
        street: this.street,
        zip: this.zip,
      })
      console.log(response)
    }
  }
}
</script>
