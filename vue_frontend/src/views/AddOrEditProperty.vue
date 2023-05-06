<template>
  <nav-bar/>
  <section class="bg-dark py-5 user-header">
    <div class="container">
      <div class="row align-items-center mt-2 mb-5 pb-4">
        <div class="col">
          <!-- Heading -->
          <h1 class="text-white mb-2">
            MANAGE PROPERTY
          </h1>
          <!-- Text -->
          <h6 class="font-weight-normal text-white-50 mb-0">
            {{ mode_ === 'edit' ? 'Edit property' + ' | ID: ' + property_id : 'add property' }}
          </h6>
        </div>
      </div>
    </div>
  </section>
  <section class="section-padding pt-0 user-pages-main">
    <div class="container">
      <div class="row">
        <div class="col-lg-9 col-md-9">
          <form @submit.prevent="submitForm">
            <div class="card padding-card">
              <div class="card-body"><h5 class="card-title mb-4">Property Description</h5>
                <div class="form-group"><label>Property Type </label><select
                  class="form-control custom-select" v-model="formData.property_type" :disabled="mode_ === 'edit'">
                  <option value="" disabled selected>Select Type</option>
                  <option>House</option>
                  <option>Apartment</option>
                  <option value="CommercialBuilding">Commercial Building</option>
                  <option>Land</option>
                  <option>Vacation Home</option>
                </select></div>
                <div class="form-group"><label>Property Description </label><textarea
                  class="form-control" rows="4" v-model="formData.property_description"></textarea>
                </div>

                <div class="row">
                  <div class="form-group col-md-4"><label>Number Of Rooms</label><select
                    class="form-control custom-select"
                    :disabled="!['House', 'Apartment'].includes(formData.property_type)"
                    v-model="formData.num_of_rooms">
                    <option disabled selected value="">Select Number</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                  </select></div>
                  <div class="form-group col-md-4"><label>Apartment Type </label><select
                    class="form-control custom-select" :disabled="formData.property_type !== 'Apartment'"
                    v-model="formData.building_type">
                    <option disabled selected value="">Select Type</option>
                    <option>Condominium</option>
                    <option>Loft</option>
                    <option>Duplex</option>
                  </select></div>
                  <div class="form-group col-md-4"><label>Business Type </label><select
                    class="form-control custom-select" :disabled="formData.property_type !== 'CommercialBuilding'"
                    v-model="formData.business_type">
                    <option disabled selected value="">Select Type</option>
                    <option>Type 1</option>
                    <option>Type 2</option>
                    <option>Type 3</option>
                  </select></div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4"><label>Vacation Characteristics </label><input
                    type="text" class="form-control" placeholder="Vacation Characteristics"
                    :disabled="formData.property_type !== 'Vacation Home'" v-model="formData.characteristics"></div>
                  <div class="form-group col-md-4"><label>Land Size </label><input
                    type="text" class="form-control" placeholder="sq ft"
                    :disabled="formData.property_type !== 'Land'" v-model="formData.land_size"></div>
                  <div class="form-group col-md-4"><label>Rent Price </label><input
                    type="text" class="form-control"
                    placeholder="Enter Rent Price" v-model="formData.property_price"></div>
                </div>
              </div>
            </div>
            <div class="card padding-card">
              <div class="card-body"><h5 class="card-title mb-4">Property Location</h5>
                <div class="row">
                  <div class="form-group col-md-4"><label>Address </label><input
                    type="text" class="form-control" placeholder="Enter Address" v-model="formData.property_address">
                  </div>

                  <div class="form-group col-md-4"><label>City </label><input
                    type="text" class="form-control" placeholder="Enter City" v-model="formData.property_city"></div>
                  <div class="form-group col-md-4"><label>State </label><input
                    type="text" class="form-control" placeholder="Enter State" v-model="formData.property_state">
                  </div>
                </div>
                <div class="row">

                  <div class="form-group col-md-4"><label>Neighborhood </label><input
                    type="text" class="form-control" placeholder="..." v-model="formData.neighbour"></div>
                </div>
              </div>
            </div>
            <button type="submit" class="btn btn-success" :disabled="!allInputsValid()">
              {{ mode_ === 'edit' ? 'COMMIT CHANGES' : 'ADD PROPERTY' }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>


</template>

<script>
import { getCurrentInstance, onMounted, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'EditOrProperty',
  components: {  NavBar },
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
  setup (props) {
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
      property_availability:'',
      user_id: '1',
      neighbour: '',
      num_of_rooms: null,
      business_type: '',
      building_type: '',
      characteristics: '',
      land_size: '',

    })
    const userType = ref('')
    const email = ref('')

    const allInputsValid = () => {
      // Check if all the required input fields are valid here
      if (formData.property_type === '') return false
      // Other input validation checks here
      return true
    }
    const instance = getCurrentInstance()

    onMounted(async () => {
      console.log('ok')
      try {
        const response = (await (instance.appContext.config.globalProperties.$http.get('/get-user-profile/'))).data
        if (response.success) {
          console.log('get:', response)
          userType.value = response['user_type']
          email.value = response['email']
          formData.user_id = response['user_id']
        }
        console.log('User Profile', response)
      } catch (error) {
        console.log(error)
      }

      // Initial the data
      if (mode_.value === 'edit') {
        console.log(itemId)
        try {
          const response = await instance.appContext.config.globalProperties.$http.get(`/property/detail/${itemId}/`)
          Object.assign(formData, response.data)
        } catch (error) {
          console.error(error)
          // Handle error, e.g., show an error message
        }
      }

    })

    const submitForm = async () => {
      if (!allInputsValid()) {
        // Show an error message or highlight the invalid fields
        return
      }

      try {
        const filteredData = { ...formData }
        if (!filteredData.num_of_rooms) {
          delete filteredData.num_of_rooms
        }
        if (!filteredData.business_type) {
          delete filteredData.business_type
        }
        if (!filteredData.building_type) {
          delete filteredData.building_type
        }
        if (!filteredData.characteristics) {
          delete filteredData.characteristics
        }
        if (!filteredData.land_size) {
          delete filteredData.land_size
        }
        if (!filteredData.property_availability) {
          delete filteredData.property_availability
        }
        if (mode_.value === 'edit') {
          delete filteredData.user_id
        }

        const post_url = mode_.value === 'edit' ? `/property/edit/${itemId}/` : '/property/add/'
        const response = await instance.appContext.config.globalProperties.$http.post(post_url, filteredData)
        console.log(response)

      } catch (error) {
        console.error(error)
        // Handle error, e.g., show an error message
      }
    }

    return {
      mode_,
      property_id,
      formData,
      allInputsValid,
      submitForm,
      userType,
      email,
    }
  },
}
</script>

<style scoped>

</style>
