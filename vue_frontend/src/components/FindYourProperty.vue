<template>
<!--  <div>-->
<!--    <input v-model="searchCriteria.property_type" placeholder="物业类型"/>-->
<!--    <input v-model="searchCriteria.min_price" placeholder="物业价格"/>-->
<!--    <input v-model="searchCriteria.max_price" placeholder="物业价格"/>-->
<!--    <button @click="sendSearchCriteria">搜索</button>-->
<!--  </div>-->
  <section class="site-slider">
    <div id="siteslider" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#siteslider" data-slide-to="0" class="active"></li>
        <li data-target="#siteslider" data-slide-to="1"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div class="carousel-item active" style="background-image: url('/static/picture/2.png')">
          <div class="overlay"></div>
        </div>
        <div class="carousel-item" style="background-image: url('/static/picture/21.jpg')">
          <div class="overlay"></div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#siteslider" role="button" data-slide="prev"><span
          class="carousel-control-prev-icon" aria-hidden="true"></span><span class="sr-only">Previous</span></a><a
        class="carousel-control-next" href="#siteslider" role="button" data-slide="next"><span
        class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Next</span></a></div>
    <div class="slider-form inner-page-form">
      <div class="container"><h1 class="text-center mb-5">Find Your Favorite Property</h1>
        <form @submit.prevent="submitForm">
          <div class="row no-gutters">
<!--            <div class="col-lg-3 col-md-4 col-sm-6 col-6">-->
<!--              <div class="input-group">-->
<!--                <div class="input-group-addon"><i class="mdi mdi-city"></i></div>-->
<!--                <select class="form-control select2" v-model="formData.status">-->
<!--                  <option disabled="" selected="">Any Status</option>-->
<!--                  <option>Heigh</option>-->
<!--                  <option>Midium</option>-->
<!--                  <option>Normal</option>-->
<!--                </select></div>-->
<!--            </div>-->
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <div class="input-group-addon"><i class="mdi mdi-home-modern"></i></div>
                <select class="form-control select2" v-model="formData.property_type">
                  <option value="" selected disabled>Type</option>
                  <option value="">House</option>
                  <option value="">Apartment</option>
                  <option value="">Commercial Building</option>
                </select></div>
            </div>
<!--            <div class="col-lg-3 col-md-4 col-sm-6 col-6">-->
<!--              <div class="input-group">-->
<!--                <div class="input-group-addon"><i class="mdi mdi-hotel"></i></div>-->
<!--                <select class="form-control select2" v-model="formData.bedrooms">-->
<!--                  <option disabled="" selected="">Min. Bedrooms</option>-->
<!--                  <option>1</option>-->
<!--                  <option>2</option>-->
<!--                  <option>3</option>-->
<!--                  <option>4</option>-->
<!--                  <option>5</option>-->
<!--                  <option>6</option>-->
<!--                  <option>7</option>-->
<!--                  <option>8</option>-->
<!--                  <option>9</option>-->
<!--                  <option>10</option>-->
<!--                </select></div>-->
<!--            </div>-->
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <div class="input-group-addon"><i class="mdi mdi-magnify-minus-outline"></i></div>
                <select class="form-control select2" v-model="formData.min_price">
                  <option value="" selected disabled>Min Price</option>
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
                  <option value="" selected disabled>Max Price</option>
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
                <select class="form-control select2" v-model="formData.location">
                  <option value="" selected disabled>Any Location</option>
                  <option>Australia</option>
                  <option>Brazil</option>
                  <option>Cambodia</option>
                  <option>Dominica</option>
                  <option>France</option>
                  <option>Guyana</option>
                  <option>Hong Kong</option>
                  <option>Ireland</option>
                  <option>Japan</option>
                  <option>Malaysia</option>
                  <option>Nepal</option>
                  <option>Oman</option>
                  <option>Peru</option>
                </select></div>
            </div>

<!--            <div class="col-lg-3 col-md-4 col-sm-6 col-6">-->
<!--              <div class="input-group">-->
<!--                <div class="input-group-addon"><i class="mdi mdi-hot-tub"></i></div>-->
<!--                <select class="form-control select2" v-model="formData.baths">-->
<!--                  <option disabled="" selected="">Baths</option>-->
<!--                  <option>1</option>-->
<!--                  <option>2</option>-->
<!--                  <option>3</option>-->
<!--                  <option>4</option>-->
<!--                  <option>5</option>-->
<!--                  <option>6</option>-->
<!--                  <option>7</option>-->
<!--                  <option>8</option>-->
<!--                  <option>9</option>-->
<!--                  <option>10</option>-->
<!--                </select></div>-->
<!--            </div>-->
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
              <div class="input-group">
                <button type="submit" class="btn btn-success btn-block no-radius font-weight-bold">SEARCH
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section><!-- End Main Slider With Form --><!-- Properties List -->
</template>

<script>
import {onMounted, reactive } from "vue";

export default {
  name: "FindYourProperty",
  setup(_, {emit}) {
    // const searchCriteria = ref({
    //   property_type: "",
    //   min_price: undefined,
    //   max_price: undefined,
    // });
    const formData = reactive({
      // status: '',
      property_type: '',
      // bedrooms: '',
      min_price: '',
      max_price: '',
      location: '',
      // baths: '',
    });

    function submitForm() {
      console.log('Form data:', formData);
      sendFormData();
    }

    const sendFormData = () => {
      emit('form-data', formData);
    };


    // const sendSearchCriteria = () => {
    //   emit("search-criteria", searchCriteria.value);
    // };
    onMounted(() => {
      emit("form-data", formData);
    });
    return {
      formData,
      submitForm,
      // searchCriteria,
      // sendSearchCriteria,
    };

  },

}
</script>

<style scoped>

</style>