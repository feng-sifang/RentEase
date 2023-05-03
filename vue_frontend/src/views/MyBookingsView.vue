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
                  My Booking {{ this.bookingIndex }}
                </h5>
                <BookingListItem v-for="(p, index) in properties" :key="index" :property="p"/>


                <div class="form-group">
                  <label>Booking ID</label>
                  <p type="text" class="form-control">
                    {{ this.bookingID }}
                  </p>
                </div>
                <div class="form-group">
                  <label>Start Date</label>
                  <p type="text" class="form-control">
                    {{ this.startDate }}
                  </p>
                </div>
                <div class="form-group">
                  <label>End Date</label>
                  <p type="text" class="form-control">
                    {{ this.endDate }}
                  </p>
                </div>
                <div class="form-group">
                  <label>Total Cost</label>
                  <p type="text" class="form-control">
                    {{ this.totalCost }}
                  </p>
                </div>
                <div class="form-group">
                  <label>Credit Card</label>
                  <p type="text" class="form-control">
                    {{ this.creditCard }}
                  </p>
                </div>
                <div class="form-group">
                  <label>Property Name</label>
                  <p type="text" class="form-control">
                    {{ this.propertyName }}
                  </p>
                </div>
              </div>
            </div>
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
import {getCurrentInstance, onMounted, ref} from "vue";
import BookingListItem from "@/components/BookingListItem.vue";

export default {
  name: 'MyBookingsView',
  components: {BookingListItem, UserSideBar, UserTopSection, NavBar},
  setup() {
    const instance = getCurrentInstance()
    const properties = ref([])
    const loginUserId = ref(null)
    onMounted(async () => {
      try {
        const response = (await (instance.appContext.config.globalProperties.$http.get('/get-user-profile/'))).data
        loginUserId.value = response['user_id']
      } catch (error) {
        console.log(error)
      }
      try {
        const response = await instance.appContext.config.globalProperties.$http.get(`/get-booking-by-user/${loginUserId.value}/`)
        properties.value = response.data
        console.log('list',properties.value)
      } catch (error) {
        console.error('Error fetching properties:', error)
      }
    })
    return {
      properties,
      // bookingIndex,
      // bookingID: '',
      // startDate: '',
      // endDate: '',
      // totalCost: '',
      // creditCard: '',
      // propertyName: '',
    }
  }
}
</script>