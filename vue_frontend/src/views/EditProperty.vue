<template>
  <TopPart/>
  <section class="bg-dark py-5 user-header">
    <div class="container">
      <div class="row align-items-center mt-2 mb-5 pb-4">
        <div class="col"><!-- Heading --><h1 class="text-white mb-2">Add Property </h1><!-- Text --><h6
            class="font-weight-normal text-white-50 mb-0">Settings for <a class="text-reset"
                                                                          href="mailto:yoursite@gmail.com">yoursite@gmail.com</a>
        </h6></div>
        <div class="col-auto"><!-- Button -->
          <button class="btn btn-sm btn-primary">Log Out</button>
        </div>
      </div><!-- / .row --></div><!-- / .container --></section><!-- End Inner Header --><!-- Add Property -->
  <section class="section-padding pt-0 user-pages-main">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-md-3"><!-- Collapse -->
          <div class="card padding-card tab-view user-pages-sidebar">
            <div class="card-body"><!-- Heading --><h6 class="text-uppercase mt-0 mb-3">Account </h6>
              <ul class="nav">
                <li class="nav-item"><a class="nav-link" href="user-profile.html">User Profile</a></li>
                <li class="nav-item"><a class="nav-link" href="social-profiles.html">Social Profiles</a></li>
                <li class="nav-item"><a class="nav-link" href="my-properties.html">My Properties</a></li>
                <li class="nav-item"><a class="nav-link" href="favorite-properties.html">Favorite Properties</a></li>
                <li class="nav-item"><a class="nav-link active text-success" href="">Add Property</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-lg-9 col-md-9">
          <form @submit.prevent="submitForm">
            <div class="card padding-card">
              <div class="card-body"><h5 class="card-title mb-4">Property Description</h5>
                <div class="form-group"><label>Property Type <span class="text-danger">*</span></label><select
                    class="form-control custom-select" v-model="propertyType">
                  <option value="" disabled selected>Select Type</option>
                  <option>House</option>
                  <option>Apartment</option>
                  <option value="CommercialBuilding">Commercial Building</option>
                  <option>Land</option>
                  <option>Vacation Home</option>
                </select></div>
                <div class="form-group"><label>Property Description <span class="text-danger">*</span></label><textarea
                    class="form-control" rows="4" v-model="propertyDescription"></textarea>
                </div>

                <div class="row">
                  <div class="form-group col-md-4"><label>Number Of Rooms</label><select
                      class="form-control custom-select" :disabled="!['House', 'Apartment'].includes(propertyType)"
                      v-model="numOfRooms">
                    <option disabled selected value="">Select Number</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                  </select></div>
                  <div class="form-group col-md-4"><label>Apartment Type <span
                      class="text-danger">*</span></label><select
                      class="form-control custom-select" :disabled="propertyType !== 'Apartment'">
                    <option disabled selected value="">Select Type</option>
                    <option>Type 1</option>
                    <option>Type 2</option>
                    <option>Type 3</option>
                  </select></div>
                  <div class="form-group col-md-4"><label>Business Type <span
                      class="text-danger">*</span></label><select
                      class="form-control custom-select" :disabled="propertyType !== 'CommercialBuilding'"
                      v-model="businessType">
                    <option disabled selected value="">Select Type</option>
                    <option>Type 1</option>
                    <option>Type 2</option>
                    <option>Type 3</option>
                  </select></div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4"><label>Vacation Characteristics <span
                      class="text-danger">*</span></label><input
                      type="text" class="form-control" placeholder="Vacation Characteristics"
                      :disabled="propertyType !== 'Vacation Home'"></div>
                  <div class="form-group col-md-4"><label>Land Size <span class="text-danger">*</span></label><input
                      type="text" class="form-control" placeholder="sq ft" :disabled="propertyType !== 'Land'"></div>
                  <div class="form-group col-md-4"><label>Rent Price <span
                      class="text-danger">*</span></label><input type="text" class="form-control"
                                                                 placeholder="Enter Rent Price" v-model="propertyPrice
"></div>
                </div>
              </div>
            </div>
            <div class="card padding-card">
              <div class="card-body"><h5 class="card-title mb-4">Property Location</h5>
                <div class="row">
                  <div class="form-group col-md-4"><label>Address <span class="text-danger">*</span></label><input
                      type="text" class="form-control" placeholder="Enter Address" v-model="propertyAddress"></div>

                  <div class="form-group col-md-4"><label>City <span class="text-danger">*</span></label><input
                      type="text" class="form-control" placeholder="Enter City" v-model="propertyCity"></div>
                  <div class="form-group col-md-4"><label>State <span class="text-danger">*</span></label><input
                      type="text" class="form-control" placeholder="Enter State" v-model="propertyState"></div>
                </div>
                <div class="row">

                  <div class="form-group col-md-4"><label>Zip/Postal Code <span
                      class="text-danger">*</span></label><input type="text" class="form-control"
                                                                 placeholder="Enter Zip/Postal"></div>
                  <div class="form-group col-md-4"><label>Neighborhood <span class="text-danger">*</span></label><input
                      type="text" class="form-control" placeholder="..."></div>
                </div>
              </div>
            </div>
            <button type="submit" class="btn btn-success" :disabled="!allInputsValid()">ADD PROPERTY</button>
          </form>
        </div>
      </div>
    </div>
  </section><!-- End Add Property --><!-- Join Team -->


</template>

<script>
import TopPart from "@/components/TopPart.vue";
import {getCurrentInstance, onMounted, ref} from "vue";

export default {
  name: "EditProperty",
  components: {TopPart},
  setup() {
    const propertyType = ref('');
    const propertyDescription = ref('')
    const propertyPrice = ref(undefined)
    const propertyAddress = ref('')
    const propertyCity = ref('')
    const propertyState = ref('')
    const numOfRooms = ref('')
    const businessType = ref('')

    const allInputsValid = () => {
      // Check if all the required input fields are valid here
      if (propertyType.value === '') return false;
      // Other input validation checks here
      return true;
    };
    const instance = getCurrentInstance();

    onMounted(async () => {
      // Initial the data
      try {
        const response = await instance.appContext.config.globalProperties.$http.get('/property/edit/');
        propertyType.value = response.data.property_type,
        propertyDescription.value = response.data.property_description,
        propertyPrice.value = response.data.property_price,
        propertyAddress.value = response.data.property_address,
        propertyCity.value = response.data.property_city,
        propertyState.value = response.data.property_state,
        console.log(response);
      } catch (error) {
        console.error(error);
        // Handle error, e.g., show an error message
      }
    });

    const submitForm = async () => {
      if (!allInputsValid()) {
        // Show an error message or highlight the invalid fields
        return;
      }

      try {
        const formData = {
          property_type: propertyType.value,
          property_description: propertyDescription.value,
          property_price: propertyPrice.value,
          property_address: propertyAddress.value,
          property_city: propertyCity.value,
          property_state: propertyState.value,
          user_id: 1,
        };
        if (numOfRooms.value) {
          formData.num_of_rooms = numOfRooms.value;
        }
        if (businessType.value) {
          formData.business_type = businessType.value;
        }

        const response = await instance.appContext.config.globalProperties.$http.post('/property/add/', formData);
        console.log(response);

      } catch (error) {
        console.error(error);
        // Handle error, e.g., show an error message
      }
    };

    return {
      propertyType,
      propertyDescription,
      propertyPrice,
      propertyAddress,
      propertyCity,
      propertyState,
      numOfRooms,
      businessType,
      allInputsValid,
      submitForm,

    };
  },
}
</script>

<style scoped>

</style>
