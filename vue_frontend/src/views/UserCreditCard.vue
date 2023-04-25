<template>
  <nav-bar></nav-bar>
  <user-top-section></user-top-section>
  <!-- User Profile -->
  <section class="section-padding pt-0 user-pages-main">
    <div class="container">
      <div class="row">
        <user-side-bar></user-side-bar>
        <credit-card></credit-card>
      </div>
    </div>
  </section>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import UserSideBar from '@/components/UserSideBar.vue'
import UserTopSection from '@/components/UserTopSection.vue'
import CreditCard from '@/components/CreditCard.vue'

export default {
  name: 'UserCreditCard',
  components: { CreditCard, UserSideBar, NavBar, UserTopSection },
}
</script>