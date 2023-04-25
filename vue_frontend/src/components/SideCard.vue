<template>
  <div class="card sidebar-card">
    <div class="card-body">
      <h5 class="card-title mb-3">Property Type</h5>
      <ul class="sidebar-card-list">
        <li v-for="(c, index) in typeData" :key="index">
          <i class="mdi mdi-chevron-right"></i>
          {{ c.property_type }}
          <span class="sidebar-badge">
            {{ c.total_count }}
          </span>
        </li>
      </ul>
    </div>
  </div>
  <div class="card sidebar-card">
    <div class="card-body">
      <h5 class="card-title mb-3">Property Status</h5>
      <ul class="sidebar-card-list">
        <li v-for="(c, index) in availabilityData" :key="index">
          <i class="mdi mdi-chevron-right"></i>
          {{ c.property_availability ? 'Available' : 'Rented' }}
          <span class="sidebar-badge">
            {{ c.total_count }}
          </span>
        </li>
      </ul>
    </div>
  </div>
  <div class="card sidebar-card">
    <div class="card-body">
      <h5 class="card-title mb-3">Property By City</h5>
      <ul class="sidebar-card-list">
        <li v-for="(c, index) in cityData" :key="index">
          <i class="mdi mdi-chevron-right"></i>
          {{ c.property_city }}
          <span class="sidebar-badge">
            {{ c.total_count }}
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

import { getCurrentInstance, onMounted, ref } from 'vue'

export default {
  name: 'SideCard',

  setup () {
    const instance = getCurrentInstance()
    const availabilityData = ref([])
    const typeData = ref([])
    const cityData = ref([])
    const fetchGroupedPropertyData = async () => {
      try {
        const response = await instance.appContext.config.globalProperties.$http.get('/property/side-card/')
        console.log(response.data)
        availabilityData.value = response.data.availability_data
        typeData.value = response.data.type_data
        cityData.value = response.data.city_data
      } catch (error) {
        console.error('Error fetching grouped property data:', error)
      }
    }

    onMounted(fetchGroupedPropertyData)

    return {
      typeData,
      cityData,
      availabilityData,
    }
  },
}
</script>
