<template>
  <nav-bar/>
  <section class="bg-dark py-5 user-header">
    <div class="container">
      <div class="row">
      <div class="col">
        <!-- Heading -->
        <h1 class="text-white mb-2">
          {{ formData.property_type }}
        </h1>
        <!-- Text -->
        <h6 class="font-weight-normal text-white-50 mb-0">
          {{ 'Property ID: ' + property_id }}
        </h6>
      </div>

      </div>

    </div>

  </section>
  <body><!-- Navbar -->

  <section class="section-padding">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-8">
          <div class="card">
            <img
                class="card-img-top"
                :src="`/static/picture/${formData.property_type.toLowerCase()}.png`"
                alt="Card image cap"
            >
          </div>
          <div class="row">
            <div class="col-lg-4 col-md-4">
              <div class="list-icon"><i class="mdi mdi-hot-tub"></i><strong>Price:</strong>
                <p class="mb-0">${{ formData.property_price }}</p></div>
            </div>
            <div class="col-lg-4 col-md-4" v-if="formData.num_of_rooms">
              <div class="list-icon"><i class="mdi mdi-garage"></i><strong>Rooms:</strong>
                <p class="mb-0">{{ formData.num_of_rooms }} Rooms</p></div>
            </div>
            <div class="col-lg-4 col-md-4" v-if="formData.land_size">
              <div class="list-icon"><i class="mdi mdi-move-resize-variant"></i><strong>Land Size:</strong>
                <p class="mb-0">{{ formData.land_size }} aq ft</p></div>
            </div>
            <div class="col-lg-4 col-md-4" v-if="formData.building_type">
              <div class="list-icon"><i class="mdi mdi-sofa"></i><strong>Apartment Type:</strong>
                <p class="mb-0">{{ formData.building_type }}</p></div>
            </div>


            <div class="col-lg-4 col-md-4" v-if="formData.characteristics">
              <div class="list-icon"><i class="mdi mdi-floor-plan"></i><strong>Characteristics:</strong>
                <p class="mb-0">{{ formData.characteristics }}</p></div>
            </div>
            <div class="col-lg-4 col-md-4" v-if="formData.business_type">
              <div class="list-icon"><i class="mdi mdi-car-convertible"></i><strong>Business
                Type:</strong>
                <p class="mb-0">{{ formData.business_type }}</p></div>
            </div>
          </div>
          <div class="card padding-card">
            <div class="card-body"><h5 class="card-title mb-3">Description</h5>
              <p>{{ formData.property_description }}</p>
            </div>
          </div>
          <div class="card padding-card">
            <div class="card-body">
              <h5 class="card-title mb-3">Location</h5>
              <div class="row mb-3">
                <div class="col-lg-6 col-md-6">
                  <p><strong class="text-dark">Address :</strong> {{ formData.property_address }}</p>
                  <p><strong class="text-dark">State :</strong> {{ formData.property_state }}</p>
                </div>
                <div class="col-lg-6 col-md-6">
                  <p><strong class="text-dark">City :</strong> {{ formData.property_city }}</p>
                  <p><strong class="text-dark">Neighborhood :</strong> to be</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="card sidebar-card">
            <div class="card-body"><h5 class="card-title mb-4">About Agent</h5>
              <div id="featured-properties">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <div class="card card-list"><a href="#"><img class="card-img-top"
                                                                 src="static/picture/agent.jpg"
                                                                 alt="Card image cap">
                      <div class="card-body pb-0"><h5 class="card-title mb-4">Jennie Wilson</h5><h6
                          class="card-subtitle mb-3 text-muted"><i
                          class="mdi mdi-email"></i> {{ email }}</h6></div>
                    </a></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="card sidebar-card">
            <div class="card-body"><h5 class="card-title mb-4">Book this Property</h5>
              <form name="sentMessage" @submit.prevent="submitForm">
                <div class="control-group form-group">
                  <div class="controls"><label>Select Your Credit Card <span class="text-danger">*</span></label><select
                  class="form-control custom-select" v-model="formData.property_type" :disabled="mode_ === 'edit'">
                  <option v-for="(c, index) in creditCards" :key="index">{{ c.number }}</option>
                </select>
                  </div>
                </div>
                <div class="control-group form-group">
                  <div class="controls"><label>Start Date <span class="text-danger">*</span></label><input
                      type="text"  class="form-control" required="">
                  </div>
                </div>
                 <div class="control-group form-group">
                  <div class="controls"><label>End Date <span class="text-danger">*</span></label><input
                      type="text"  class="form-control" required="">
                  </div>
                </div>
                <button type="submit" class="btn btn-success btn-block">Submit Booking</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section><!-- End Property Single Slider --><!-- Similar Properties -->
  </body>



</template>

<script>
import {getCurrentInstance, onMounted, reactive, ref} from 'vue'
import {useRoute} from 'vue-router'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'AddPropertyDetail',
  components: {NavBar},
  props: {
    mode: {
      type: String,
      required: true,
    },
    itemId: {
      type: String,
      default: null,
    },
  },
  setup(props) {
    const route = useRoute()
    const mode_ = ref(props.mode)
    const property_id = ref(props.itemId)
    const itemId = route.params.itemId
    const formData = reactive({
      // property_id: null,
      property_type: '',
      property_description: '',
      property_price: '',
      property_address: '',
      property_city: '',
      property_state: '',
      user_id: '1',
      num_of_rooms: null,
      business_type: '',
      building_type: '',
      characteristics: '',
      land_size: '',
    })
    const email = ref('')
    const phone = ref('')
    const name = ref('')
    const creditCards = ref([])


    const allInputsValid = () => {
      // Check if all the required input fields are valid here
      if (formData.property_type === '') return false
      // Other input validation checks here
      return true
    }
    const instance = getCurrentInstance()

    onMounted(async () => {
      try {
        const response = await instance.appContext.config.globalProperties.$http.get(`/property/detail/${itemId}/`)
        Object.assign(formData, response.data)
      } catch (error) {
        console.error(error)
        // Handle error, e.g., show an error message
      }

      try {
        const response = (await (instance.appContext.config.globalProperties.$http.get(`/get-user-by-id/${formData.user_id}`))).data
        email.value = response['email']
        phone.value = response['phone']
        name.value = response['first_name'] + ' ' + response['last_name']
      } catch (error) {
        console.log(error)
      }
      try {
        const response = (await (instance.appContext.config.globalProperties.$http.get(`/get-user-creditcard/`))).data
          console.log('get:', response)

        creditCards.value = response['credit_cards']
        console.log('get:', creditCards)
      } catch (error) {
        console.log(error)
      }


    })


    return {
      mode_,
      property_id,
      formData,
      allInputsValid,
      email,
      name,
      creditCards
    }
  },
}
</script>

<style scoped>

</style>
