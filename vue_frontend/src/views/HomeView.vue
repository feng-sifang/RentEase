<template>
  <header>
    <!-- Navbar -->
    <nav-bar></nav-bar>
    <!-- End Navbar -->
  </header>
  <!-- Main Slider With Form -->
  <section class="site-slider">
    <div id="site-slider" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li
          data-target="#site-slider"
          data-slide-to="0"
          class="active"
        ></li>
        <li data-target="#site-slider" data-slide-to="1"></li>
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
        href="#site-slider"
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
        href="#site-slider"
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
      <div class="text-center mb-5">
        <h6 class="subtitle mb-1 mt-0 text-shadow text-dark">
          Uncover the best offers on the real estate market.
        </h6>
        <h1 class="display-4 mt-0 font-weight-bold text-shadow">
          Your Key to Easy Living.
        </h1>
      </div>
      <div class="d-flex justify-content-center align-items-center">
        <div>
          <router-link
            to="/property/list/"
            type="submit"
            class="btn btn-success font-weight-bold"
            style="padding: 10px 200px;">
            DISCOVER MORE
          </router-link>
        </div>
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

export default {
  name: 'HomeView',
  components: { SingleBlock, NavBar, },
}
</script>