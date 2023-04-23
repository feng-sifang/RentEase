<template>
  <div class="card sidebar-card">
    <div class="card-body"><h5 class="card-title mb-3">Property Type</h5>
      <ul class="sidebar-card-list">
        <li v-for="(c, index) in typeData" :key="index"><i class="mdi mdi-chevron-right"></i>{{c.property_type}} <span
            class="sidebar-badge">{{c.total_count}}</span></li>

      </ul>
    </div>
  </div>
  <div class="card sidebar-card">
    <div class="card-body"><h5 class="card-title mb-3">Property Status</h5>
      <ul class="sidebar-card-list">
        <li v-for="(c, index) in availabilityData" :key="index"><i class="mdi mdi-chevron-right"></i>{{ c.property_availability ? 'Available' : 'Rented'}} <span class="sidebar-badge">{{c.total_count}}</span>
        </li>
      </ul>
    </div>
  </div>
  <div class="card sidebar-card">
    <div class="card-body"><h5 class="card-title mb-3">Property By City</h5>
      <ul class="sidebar-card-list">
        <li v-for="(c, index) in cityData" :key="index"><i class="mdi mdi-chevron-right" ></i>{{c.property_city}} <span class="sidebar-badge">{{c.total_count}}</span>
        </li>

      </ul>
    </div>
  </div>
  <!--  <div class="card sidebar-card">-->
  <!--    <div class="card-body"><h5 class="card-title mb-4">Featured Properties</h5>-->
  <!--      <div id="featured-properties" class="carousel slide" data-ride="carousel">-->
  <!--        <ol class="carousel-indicators">-->
  <!--          <li data-target="#featured-properties" data-slide-to="0" class="active"></li>-->
  <!--          <li data-target="#featured-properties" data-slide-to="1"></li>-->
  <!--        </ol>-->
  <!--        <div class="carousel-inner">-->
  <!--          <div class="carousel-item active">-->
  <!--            <div class="card card-list"><a href="#"><span-->
  <!--                class="badge badge-success">For Sale</span><img class="card-img-top"-->
  <!--                                                                src="static/picture/11.png"-->
  <!--                                                                alt="Card image cap">-->
  <!--              <div class="card-body"><h5 class="card-title">House in Kent Street</h5><h6-->
  <!--                  class="card-subtitle mb-2 text-muted"><i-->
  <!--                  class="mdi mdi-home-map-marker"></i>127 Kent Sreet,Sydny,NEW 2000</h6>-->
  <!--                <h2 class="text-success mb-0 mt-3">$130,000 <small>/month</small></h2></div>-->
  <!--            </a></div>-->
  <!--          </div>-->
  <!--          <div class="carousel-item">-->
  <!--            <div class="card card-list"><a href="#"><span-->
  <!--                class="badge badge-secondary">For Rent</span><img class="card-img-top"-->
  <!--                                                                  src="static/picture/21.png"-->
  <!--                                                                  alt="Card image cap">-->
  <!--              <div class="card-body"><h5 class="card-title">Family House in Hudson</h5><h6-->
  <!--                  class="card-subtitle mb-2 text-muted"><i-->
  <!--                  class="mdi mdi-home-map-marker"></i>Hoboken,NJ,USA</h6>-->
  <!--                <h2 class="text-success mb-0 mt-3">$127,000 <small>/month</small></h2></div>-->
  <!--            </a></div>-->
  <!--          </div>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--  </div>-->
</template>

<script>

import {getCurrentInstance, onMounted, ref} from "vue";

export default {
  name: "SideCard",
  setup() {
    const instance = getCurrentInstance();
    const typeData = ref([]);
    const cityData = ref([]);
    const availabilityData = ref([]);
    const fetchGroupedPropertyData = async () => {
      try {
        const response = await instance.appContext.config.globalProperties.$http.get('/property/side_card/');
        console.log(response.data)
        typeData.value = response.data.type_data;
        cityData.value = response.data.city_data;
        availabilityData.value = response.data.availability_data;
      } catch (error) {
        console.error('Error fetching grouped property data:', error);
      }
    };
    onMounted(fetchGroupedPropertyData);
    return {
      typeData,
      cityData,
      availabilityData,
    };


  }

}
</script>

<style scoped>

</style>