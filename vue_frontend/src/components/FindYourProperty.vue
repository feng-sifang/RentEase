<template>
  <section class="site-slider">
    <div id="siteslider" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#siteslider" data-slide-to="0" class="active"></li>
        <li data-target="#siteslider" data-slide-to="1"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div class="carousel-item active" style="background-image: url('/static/picture/41.png')">
          <div class="overlay"></div>
        </div>
        <div class="carousel-item" style="background-image: url('/static/picture/33.png')">
          <div class="overlay"></div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#siteslider" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#siteslider" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    <div class="slider-form inner-page-form">
      <div class="container">
        <h1 class="text-center mb-5">Find Your Favorite Property</h1>
        <form @submit.prevent="submitForm">
          <div class="row no-gutters">
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <div class="input-group-addon"><i class="mdi mdi-home-modern"></i></div>
                <select class="form-control select2" v-model="formData.property_type">
                  <option value="" selected>Any Type</option>
                  <option>House</option>
                  <option>Apartment</option>
                  <option value="CommercialBuilding">Commercial Building</option>
                  <option>Land</option>
                  <option value="VacationHome">Vacation Home</option>
                </select></div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <div class="input-group-addon"><i class="mdi mdi-magnify-minus-outline"></i></div>
                <select class="form-control select2" v-model="formData.min_price">
                  <option value="" selected>Min Price</option>
                  <option>100</option>
                  <option>200</option>
                  <option>300</option>
                  <option>400</option>
                  <option>500</option>
                  <option>600</option>
                  <option>700</option>
                  <option>800</option>
                  <option>900</option>
                  <option>1000</option>
                </select></div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <div class="input-group-addon"><i class="mdi mdi-magnify-plus-outline"></i></div>
                <select class="form-control select2" v-model="formData.max_price">
                  <option value="" selected>Max Price</option>
                  <option>1000</option>
                  <option>2000</option>
                  <option>3000</option>
                  <option>4000</option>
                  <option>5000</option>
                  <option>6000</option>
                  <option>7000</option>
                  <option>8000</option>
                  <option>9000</option>
                  <option>10000</option>
                </select></div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <div class="input-group-addon"><i class="mdi mdi-map-marker-multiple"></i></div>
                <select class="form-control select2" v-model="formData.property_city">
                  <option value="" selected>Any City</option>
                  <option>NYC</option>
                  <option>Portland</option>

                </select></div>
            </div>
            <div class="input-group">
              <button type="submit" class="btn btn-success btn-block no-radius font-weight-bold">
                SEARCH
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import {onMounted, reactive, ref} from 'vue'

export default {
  name: 'FindYourProperty',
  setup (_, { emit }) {

    const formData = reactive({
      property_type: '',
      min_price: '',
      max_price: '',
      property_city: '',
    })

    function submitForm () {
      console.log('Form data:', formData)
      sendFormData()
    }

    const sendFormData = () => {
      emit('form-data', formData)
    }
    const cityList = ref('');


    onMounted(() => {
      emit('form-data', formData)
    })
    return {
      formData,
      submitForm,
      cityList
    }

  },

}
</script>

<style scoped>

</style>