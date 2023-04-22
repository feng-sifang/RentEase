<template>
  <header>
    <!-- Navbar -->
    <nav-bar v-if="isLoginChecked" :userInfo="parentUserInfo"></nav-bar>
  </header>
  <!-- End Navbar -->
  <!-- Main Slider With Form -->
  <section class="site-slider">
    <div id="siteslider" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li
          data-target="#siteslider"
          data-slide-to="0"
          class="active"
        ></li>
        <li data-target="#siteslider" data-slide-to="1"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div
          class="carousel-item active"
          style="background-image: url('/static/picture/11.png')"
        >
          <div class="overlay"></div>
        </div>
        <div
          class="carousel-item"
          style="background-image: url('/static/picture/21.png')"
        >
          <div class="overlay"></div>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#siteslider"
        role="button"
        data-slide="prev">
        <span
          class="carousel-control-prev-icon"
          aria-hidden="true">
        </span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#siteslider"
        role="button"
        data-slide="next">
      <span
        class="carousel-control-next-icon"
        aria-hidden="true">
      </span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    <div class="slider-form">
      <div class="container">
        <div class="text-center mb-5">
          <h6 class="subtitle mb-1 mt-0 text-shadow text-dark">
            Uncover the best offers on the real estate market.
          </h6>
          <h1 class="display-4 mt-0 font-weight-bold text-shadow">
            Your Key to Easy Living.
          </h1>
        </div>
        <form>
          <div class="row no-gutters">
            <div class="col-md-4">
              <div class="input-group">
                <div class="input-group-addon">
                  <i
                    class="mdi mdi-map-marker-multiple"
                  ></i>
                </div>
                <input
                  class="form-control"
                  placeholder="Location, Project or Landmark"
                  type="text"
                />
              </div>
            </div>
            <div class="col-md-3">
              <div class="input-group">
                <div class="input-group-addon">
                  <i class="mdi mdi-google-maps"></i>
                </div>
                <select class="form-control select2 no-radius">
                  <option value="">Locations</option>
                  <option value="AL">Alabama</option>
                  <option value="AK">Alaska</option>
                  <option value="AZ">Arizona</option>
                  <option value="AR">Arkansas</option>
                  <option value="CA">California</option>
                  <option value="CO">Colorado</option>
                  <option value="CT">Connecticut</option>
                  <option value="DE">Delaware</option>
                  <option value="DC">District Of Columbia</option>
                  <option value="FL">Florida</option>
                  <option value="GA">Georgia</option>
                  <option value="HI">Hawaii</option>
                  <option value="ID">Idaho</option>
                  <option value="IL">Illinois</option>
                  <option value="IN">Indiana</option>
                  <option value="IA">Iowa</option>
                  <option value="KS">Kansas</option>
                  <option value="KY">Kentucky</option>
                  <option value="LA">Louisiana</option>
                  <option value="ME">Maine</option>
                  <option value="MD">Maryland</option>
                  <option value="MA">Massachusetts</option>
                  <option value="MI">Michigan</option>
                  <option value="MN">Minnesota</option>
                  <option value="MS">Mississippi</option>
                  <option value="MO">Missouri</option>
                  <option value="MT">Montana</option>
                  <option value="NE">Nebraska</option>
                  <option value="NV">Nevada</option>
                  <option value="NH">New Hampshire</option>
                  <option value="NJ">New Jersey</option>
                  <option value="NM">New Mexico</option>
                  <option value="NY">New York</option>
                  <option value="NC">North Carolina</option>
                  <option value="ND">North Dakota</option>
                  <option value="OH">Ohio</option>
                  <option value="OK">Oklahoma</option>
                  <option value="OR">Oregon</option>
                  <option value="PA">Pennsylvania</option>
                  <option value="RI">Rhode Island</option>
                  <option value="SC">South Carolina</option>
                  <option value="SD">South Dakota</option>
                  <option value="TN">Tennessee</option>
                  <option value="TX">Texas</option>
                  <option value="UT">Utah</option>
                  <option value="VT">Vermont</option>
                  <option value="VA">Virginia</option>
                  <option value="WA">Washington</option>
                  <option value="WV">West Virginia</option>
                  <option value="WI">Wisconsin</option>
                  <option value="WY">Wyoming</option>
                </select>
              </div>
            </div>
            <div class="col-md-3">
              <div class="input-group">
                <div class="input-group-addon">
                  <i class="mdi mdi-security-home"></i>
                </div>
                <select
                  class="form-control select2 no-radius"
                >
                  <option value="">Property Type</option>
                  <option value="">House/Villa</option>
                  <option value="">Flat</option>
                  <option value="">Plot/Land</option>
                  <option value="">Office Space</option>
                  <option value="">Shop/Showroom</option>
                  <option value="">
                    Commercial Land
                  </option>
                  <option value="">
                    Warehouse/ Godown
                  </option>
                  <option value="">
                    Industrial Building
                  </option>
                </select>
              </div>
            </div>
            <div class="col-md-2">
              <button
                type="submit"
                class="btn btn-success btn-block no-radius font-weight-bold"
              >
                SEARCH
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
  <!-- End Main Slider With Form -->
  <!-- Properties by City -->
  <section class="section-padding bg-white">
    <div class="section-title text-center mb-5">
      <h2>Property By City</h2>
      <p>Lorem ipsum dolor sit amet,consectetur adipisicing elit.</p>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-lg-3">
          <div class="card bg-dark text-white card-overlay">
            <a
              href="#"
            ><img
              class="card-img"
              src="/static/picture/13.png"
              alt="Card image"
            />
              <div class="card-img-overlay">
                <h3 class="card-title text-white">
                  New York
                </h3>
                <p class="card-text text-white">
                  16 Properties
                </p>
              </div>
            </a
            >
          </div>
        </div>
        <div class="col-lg-3">
          <div class="card bg-dark text-white card-overlay">
            <a
              href="#"
            ><img
              class="card-img"
              src="/static/picture/23.png"
              alt="Card image"
            />
              <div class="card-img-overlay">
                <h3 class="card-title text-white">
                  Los Angeles
                </h3>
                <p class="card-text text-white">
                  265 Properties
                </p>
              </div>
            </a
            >
          </div>
        </div>
        <div class="col-lg-3">
          <div class="card bg-dark text-white card-overlay">
            <a
              href="#"
            ><img
              class="card-img"
              src="/static/picture/33.png"
              alt="Card image"
            />
              <div class="card-img-overlay">
                <h3 class="card-title text-white">
                  Chicago
                </h3>
                <p class="card-text text-white">
                  620 Properties
                </p>
              </div>
            </a
            >.
          </div>
        </div>
        <div class="col-lg-3">
          <div class="card bg-dark text-white card-overlay">
            <a
              href="#"
            ><img
              class="card-img"
              src="/static/picture/43.png"
              alt="Card image"
            />
              <div class="card-img-overlay">
                <h3 class="card-title text-white">
                  Philadelphia
                </h3>
                <p class="card-text text-white">
                  28 Properties
                </p>
              </div>
            </a
            >
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- End Properties by City -->
  <!-- Properties List -->
  <section class="section-padding">
    <div class="section-title text-center mb-5">
      <h2>Latest Properties</h2>
      <p>Lorem ipsum dolor sit amet,consectetur adipisicing elit.</p>
    </div>
    <div class="container">
      <div class="row">
        <single-block></single-block>
        <single-block></single-block>
        <single-block></single-block>
      </div>
      <div class="row">
        <single-block></single-block>
        <single-block></single-block>
        <single-block></single-block>
      </div>
    </div>
  </section>
  <!-- End Properties List -->
  <!-- Trusted Agents -->
  <section class="section-padding bg-white">
    <div class="section-title text-center mb-5">
      <h2>Trusted Agents</h2>
      <p>Lorem ipsum dolor sit amet,consectetur adipisicing elit.</p>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-4">
          <div class="agents-card text-center">
            <img
              class="img-fluid mb-4"
              src="/static/picture/1.jpg"
              alt=""
            />
            <p class="mb-4">
              Lorem Ipsum is simply dummy text of the printing
              and typesetting industry. Lorem Ipsum has been.
            </p>
            <h6 class="mb-0 text-success">- Stave Martin</h6>
            <small>Buying Agent</small>
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="agents-card text-center">
            <img
              class="img-fluid mb-4"
              src="/static/picture/2.jpg"
              alt=""
            />
            <p class="mb-4">
              Lorem Ipsum is simply dummy text of the printing
              and typesetting industry. Lorem Ipsum has been.
            </p>
            <h6 class="mb-0 text-success">- Mark Smith</h6>
            <small>Selling Agent</small>
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="agents-card text-center">
            <img
              class="img-fluid mb-4"
              src="/static/picture/3.jpg"
              alt=""
            />
            <p class="mb-4">
              Lorem Ipsum is simply dummy text of the printing
              and typesetting industry. Lorem Ipsum has been.
            </p>
            <h6 class="mb-0 text-success">- Ryan Printz</h6>
            <small>Real Estate Broker</small>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- End Trusted Agents -->

</template>


<script>
import SingleBlock from '@/components/SingleBlock.vue'
import NavBar from '@/components/NavBar.vue'
import axios from 'axios'

export default {
  name: 'HomeView',

  data () {
    return {
      isLoginChecked: false,
      parentUserInfo: {
        isLoggedIn: false,
        userFirstName: '',
        userType: '',
      },
    }
  },

  methods: {
    async checkLogin () {
      try {
        const response = await axios.get('/check-login/')
        if (response.data.success) {
          // if returned data is true, means user is logged in
          this.parentUserInfo.isLoggedIn = response.data['is_logged_in']
          this.parentUserInfo.userFirstName = response.data['user_first_name']
          this.parentUserInfo.userType = response.data['user_type']
          console.log(response.data)
        } else {
          // not logged in
          console.log(response.data)
        }
        this.isLoginChecked = true

      } catch (error) {
        console.error('An error occurred:', error)
      }
    },
  },

  mounted () {
    this.checkLogin()
  },

  components: {
    SingleBlock,
    NavBar,
  },
}
</script>