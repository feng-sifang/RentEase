<template>
  <NavBar></NavBar>
  <FindYourProperty @form-data="handleFormData"/>
  <section class="section-padding">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-4">
          <side-card/>
        </div>
        <div class="col-lg-8 col-md-8">

          <div class="row">
            <PropertyListItem
              v-for="(property, index) in properties" :key="index" :property="property" :userType="userType"/>
          </div>
          <nav class="mt-5">
            <ul class="pagination justify-content-center">
              <li class="page-item" :class="{ disabled: !hasPrevious }">
                <a class="page-link" href="#" @click.prevent="goToPreviousPage" tabindex="-1">
                  <i class="mdi mdi-chevron-left"></i>
                </a>
              </li>
              <li
                v-for="pageNumber in pageNumbers"
                :key="pageNumber"
                class="page-item"
                :class="{ active: pageNumber === currentPage }">
                <a class="page-link" href="#" @click.prevent="goToPage(pageNumber)">
                  {{ pageNumber }}
                </a>
              </li>
              <li class="page-item" :class="{ disabled: !hasNext }">
                <a class="page-link" href="#" @click.prevent="goToNextPage">
                  <i class="mdi mdi-chevron-right"></i>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import PropertyListItem from '@/components/PropertyListItem.vue'
import { computed, getCurrentInstance, onMounted, provide, ref } from 'vue'
import FindYourProperty from '@/components/FindYourProperty.vue'
import SideCard from '@/components/SideCard.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'PropertyList',
  components: { NavBar, SideCard, FindYourProperty, PropertyListItem },

  setup () {
    const properties = ref([])
    provide('properties', properties)
    const price_min = ref(0)
    const price_max = ref(2000)
    const baseUrl = '/property/find/'
    const instance = getCurrentInstance()
    const searchResults = ref([])
    const userType = ref('')
    const handleFormData = async (criteria) => {
      const url = baseUrl
      try {
        const response = await instance.appContext.config.globalProperties.$http.post(url, criteria)
        properties.value = response.data
      } catch (error) {
        console.error('Error fetching properties:', error)
      }
    }
    onMounted(async () => {
      console.log('ok')
      try {
        const response = (await instance.appContext.config.globalProperties.$http.get('/get-user-profile/')).data
        if (response.success) {
          console.log('get:', response)
          userType.value = response['user_type']
        }
        console.log('User Profile', response)
      } catch (error) {
        console.log(error)
      }
    })

    // pages
    const currentPage = ref(1)
    const numPages = ref(10)

    const hasPrevious = computed(() => currentPage.value > 1)
    const hasNext = computed(() => currentPage.value < numPages.value)

    const pageNumbers = computed(() => {
      const start = Math.max(1, currentPage.value - 2)
      const end = Math.min(numPages.value, currentPage.value + 2)
      return Array.from({ length: end - start + 1 }, (_, i) => i + start)
    })

    function goToPage (pageNumber) {
      currentPage.value = pageNumber
    }

    function goToPreviousPage () {
      if (hasPrevious.value) {
        goToPage(currentPage.value - 1)
      }
    }

    function goToNextPage () {
      if (hasNext.value) {
        goToPage(currentPage.value + 1)
      }
    }

    return {
      properties,
      price_min,
      price_max,
      handleFormData,
      searchResults,
      currentPage,
      numPages,
      hasPrevious,
      hasNext,
      pageNumbers,
      goToPage,
      goToPreviousPage,
      goToNextPage,
      userType,
    }
  },

}
</script>

<style scoped>

</style>