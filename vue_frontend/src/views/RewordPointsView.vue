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
                  Reword Points
                </h5>
                <div class="form-group">
                  <label>Total Points</label>
                  <p type="text" class="form-control">
                    {{ this.totalPoints }}
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
import UserSideBar from '@/components/UserSideBar.vue'
import UserTopSection from '@/components/UserTopSection.vue'

export default {
  name: 'RewordPointsView',
  components: { UserTopSection, UserSideBar, NavBar },

  data () {
    return {
      totalPoints: 0,
    }
  },

  methods: {
    async getTotalPoints () {
      const response = await this.axios.get('/get-points')
      console.log(response.data)
      this.totalPoints = response.data['total_points']
    },
  },

  mounted () {
    this.getTotalPoints()
  },
}
</script>
