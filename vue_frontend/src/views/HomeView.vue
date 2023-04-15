<template>
  <header>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a
          class="navbar-brand text-success logo" href=""
        ><img
          class="img-fluid"
          src="/static/picture/logo.svg"
          alt=""/></a
        >
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="">Home</a>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                id="navbarDropdownPortfolio"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >Properties
              </a>
              <div
                class="dropdown-menu"
                aria-labelledby="navbarDropdownPortfolio"
              >
                <a
                  class="dropdown-item"
                  href="#"
                >Properties Grid</a
                ><a
                class="dropdown-item"
                href="#"
              >Properties List</a
              ><a
                class="dropdown-item"
                href="#"
              >Property Single Slider</a
              ><a
                class="dropdown-item"
                href="#"
              >Property Single Gallery</a
              >
              </div>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                id="navbarDropdownPortfolio"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >Agency
              </a>
              <div
                class="dropdown-menu"
                aria-labelledby="navbarDropdownPortfolio"
              >
                <a
                  class="dropdown-item"
                  href="#"
                >Agency List</a>
                <a
                  class="dropdown-item"
                  href="#"
                >Agency Profile</a>
                <a
                  class="dropdown-item" href="#"
                >Agents</a>
                <a
                  class="dropdown-item"
                  href="#"
                >Agent Profile</a>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                id="navbarDropdownPortfolio"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >Blog
              </a>
              <div
                class="dropdown-menu"
                aria-labelledby="navbarDropdownPortfolio"
              >
                <a
                  class="dropdown-item" href="#"
                >Blog</a
                ><a
                class="dropdown-item"
                href="#"
              >Blog Single</a>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                id="navbarDropdownPortfolio"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >My Account
              </a>
              <div
                class="dropdown-menu"
                aria-labelledby="navbarDropdownPortfolio"
              >
                <a
                  class="dropdown-item"
                  href="#"
                >User Profile</a>
                <a
                  class="dropdown-item"
                  href="#"
                >Social Profiles</a>
                <a
                  class="dropdown-item"
                  href="#"
                >My Properties</a>
                <a
                  class="dropdown-item"
                  href="#"
                >Favorite Properties</a>
                <a
                  class="dropdown-item"
                  href="#"
                >Add Property</a>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                id="navbarDropdownPortfolio"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false">
                Pages
              </a>
              <div
                class="dropdown-menu"
                aria-labelledby="navbarDropdownPortfolio">
                <a class="dropdown-item" href="#">
                  About Us
                </a>
                <a class="dropdown-item" href="#">
                  FAQ
                </a>
                <a
                  class="dropdown-item"
                  href="#">
                  Contact
                </a>
              </div>
            </li>
          </ul>
          <div class="my-2 my-lg-0">
            <ul class="list-inline main-nav-right">
              <li class="list-inline-item">
                <router-link to="/login" class="btn btn-link btn-sm">Login</router-link>

              </li>
              <li class="list-inline-item">
                <a
                  class="btn btn-success btn-sm"
                  href="#"
                >Sign Up</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
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
                <select
                  class="form-control select2 no-radius"
                >
                  <option value="">Locations</option>
                  <option value="AL">Alabama</option>
                  <option value="AK">Alaska</option>
                  <option value="AZ">Arizona</option>
                  <option value="AR">Arkansas</option>
                  <option value="CA">California</option>
                  <option value="CO">Colorado</option>
                  <option value="CT">Connecticut</option>
                  <option value="DE">Delaware</option>
                  <option value="DC">
                    District Of Columbia
                  </option>
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
                  <option value="MA">
                    Massachusetts
                  </option>
                  <option value="MI">Michigan</option>
                  <option value="MN">Minnesota</option>
                  <option value="MS">Mississippi</option>
                  <option value="MO">Missouri</option>
                  <option value="MT">Montana</option>
                  <option value="NE">Nebraska</option>
                  <option value="NV">Nevada</option>
                  <option value="NH">
                    New Hampshire
                  </option>
                  <option value="NJ">New Jersey</option>
                  <option value="NM">New Mexico</option>
                  <option value="NY">New York</option>
                  <option value="NC">
                    North Carolina
                  </option>
                  <option value="ND">North Dakota</option>
                  <option value="OH">Ohio</option>
                  <option value="OK">Oklahoma</option>
                  <option value="OR">Oregon</option>
                  <option value="PA">Pennsylvania</option>
                  <option value="RI">Rhode Island</option>
                  <option value="SC">
                    South Carolina
                  </option>
                  <option value="SD">South Dakota</option>
                  <option value="TN">Tennessee</option>
                  <option value="TX">Texas</option>
                  <option value="UT">Utah</option>
                  <option value="VT">Vermont</option>
                  <option value="VA">Virginia</option>
                  <option value="WA">Washington</option>
                  <option value="WV">
                    West Virginia
                  </option>
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
        <div class="col-lg-4 col-md-4">
          <div class="card card-list">
            <a
              href="#"
            ><span
              class="badge badge-success"
            >For Sale</span
            ><img
              class="card-img-top"
              src="/static/picture/11.png"
              alt="Card image cap"
            />
              <div class="card-body">
                <h5 class="card-title">
                  House in Kent Street
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                  <i class="mdi mdi-home-map-marker"></i
                  >127 Kent Sreet,Sydny,NEW 2000
                </h6>
                <div class="review-block-rate">
                  <i class="mdi mdi-star"></i
                  ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star-outline"></i
                ><i class="mdi mdi-star-outline"></i
                ><span
                  class="badge-pill badge-success ml-2"
                >3.2</span
                >
                </div>
                <h2 class="text-success mb-0 mt-3">
                  $130,000 <small>/month</small>
                </h2>
              </div>
              <div class="card-footer">
                                    <span
                                    ><i class="mdi mdi-sofa"></i
                                    >Beds:<strong>3</strong></span
                                    ><span
              ><i class="mdi mdi-scale-bathroom"></i
              >Baths:<strong>2</strong></span
              ><span
              ><i
                class="mdi mdi-move-resize-variant"
              ></i
              >Area:<strong>587 sq ft</strong></span
              >
              </div>
            </a
            >
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="card card-list">
            <a
              href="#"
            ><span
              class="badge badge-secondary"
            >For Rent</span
            ><img
              class="card-img-top"
              src="/static/picture/21.png"
              alt="Card image cap"
            />
              <div class="card-body">
                <h5 class="card-title">
                  Family House in Hudson
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                  <i class="mdi mdi-home-map-marker"></i
                  >Hoboken,NJ,USA
                </h6>
                <div class="review-block-rate">
                  <i class="mdi mdi-star"></i
                  ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star-outline"></i
                ><i class="mdi mdi-star-outline"></i
                ><span
                  class="badge-pill badge-success ml-2"
                >3.2</span
                >
                </div>
                <h2 class="text-success mb-0 mt-3">
                  $127,000 <small>/month</small>
                </h2>
              </div>
              <div class="card-footer">
                                    <span
                                    ><i class="mdi mdi-sofa"></i
                                    >Beds:<strong>5</strong></span
                                    ><span
              ><i class="mdi mdi-scale-bathroom"></i
              >Baths:<strong>3</strong></span
              ><span
              ><i
                class="mdi mdi-move-resize-variant"
              ></i
              >Area:<strong>300 sq ft</strong></span
              >
              </div>
            </a
            >
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="card card-list">
            <a
              href="#"
            ><span
              class="badge badge-success"
            >For Sale</span
            ><img
              class="card-img-top"
              src="/static/picture/31.png"
              alt="Card image cap"
            />
              <div class="card-body">
                <h5 class="card-title">
                  Loft Above The City
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                  <i class="mdi mdi-home-map-marker"></i
                  >Hope Street(Stop P),London SW11,UK
                </h6>
                <div class="review-block-rate">
                  <i class="mdi mdi-star"></i
                  ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star-outline"></i
                ><i class="mdi mdi-star-outline"></i
                ><span
                  class="badge-pill badge-success ml-2"
                >3.2</span
                >
                </div>
                <h2 class="text-success mb-0 mt-3">
                  $55,000 <small>/month</small>
                </h2>
              </div>
              <div class="card-footer">
                                    <span
                                    ><i class="mdi mdi-sofa"></i
                                    >Beds:<strong>2</strong></span
                                    ><span
              ><i class="mdi mdi-scale-bathroom"></i
              >Baths:<strong>1</strong></span
              ><span
              ><i
                class="mdi mdi-move-resize-variant"
              ></i
              >Area:<strong>100 sq ft</strong></span
              >
              </div>
            </a
            >
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-4 col-md-4">
          <div class="card card-list">
            <a
              href="#"
            ><span class="badge badge-danger">For Sale</span
            ><img
              class="card-img-top"
              src="/static/picture/41.png"
              alt="Card image cap"
            />
              <div class="card-body">
                <h5 class="card-title">
                  Store Space Greenville
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                  <i class="mdi mdi-home-map-marker"></i
                  >250-260 3rd St,Hoboken,NJ 07030,USA
                </h6>
                <div class="review-block-rate">
                  <i class="mdi mdi-star"></i
                  ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star-outline"></i
                ><i class="mdi mdi-star-outline"></i
                ><span
                  class="badge-pill badge-success ml-2"
                >3.2</span
                >
                </div>
                <h2 class="text-success mb-0 mt-3">
                  $25,000 <small>/month</small>
                </h2>
              </div>
              <div class="card-footer">
                                    <span
                                    ><i class="mdi mdi-sofa"></i
                                    >Beds:<strong>6</strong></span
                                    ><span
              ><i class="mdi mdi-scale-bathroom"></i
              >Baths:<strong>4</strong></span
              ><span
              ><i
                class="mdi mdi-move-resize-variant"
              ></i
              >Area:<strong>987 sq ft</strong></span
              >
              </div>
            </a
            >
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="card card-list">
            <a
              href="#"
            ><span
              class="badge badge-warning"
            >For Rent</span
            ><img
              class="card-img-top"
              src="/static/picture/51.png"
              alt="Card image cap"
            />
              <div class="card-body">
                <h5 class="card-title">
                  Villa in Melbourne
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                  <i class="mdi mdi-home-map-marker"></i
                  >NJ 07305,USA
                </h6>
                <div class="review-block-rate">
                  <i class="mdi mdi-star"></i
                  ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star-outline"></i
                ><i class="mdi mdi-star-outline"></i
                ><span
                  class="badge-pill badge-success ml-2"
                >3.2</span
                >
                </div>
                <h2 class="text-success mb-0 mt-3">
                  $12,000 <small>/month</small>
                </h2>
              </div>
              <div class="card-footer">
                                    <span
                                    ><i class="mdi mdi-sofa"></i
                                    >Beds:<strong>8</strong></span
                                    ><span
              ><i class="mdi mdi-scale-bathroom"></i
              >Baths:<strong>4</strong></span
              ><span
              ><i
                class="mdi mdi-move-resize-variant"
              ></i
              >Area:<strong>120 sq ft</strong></span
              >
              </div>
            </a
            >
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="card card-list">
            <a
              href="#"
            ><span class="badge badge-info">For Rent</span
            ><img
              class="card-img-top"
              src="/static/picture/61.png"
              alt="Card image cap"
            />
              <div class="card-body">
                <h5 class="card-title">
                  Villa on Hollywood Boulev
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                  <i class="mdi mdi-home-map-marker"></i
                  >The Village,Jersey City,NJ 07302,USA
                </h6>
                <div class="review-block-rate">
                  <i class="mdi mdi-star"></i
                  ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star"></i
                ><i class="mdi mdi-star-outline"></i
                ><i class="mdi mdi-star-outline"></i
                ><span
                  class="badge-pill badge-success ml-2"
                >3.2</span
                >
                </div>
                <h2 class="text-success mb-0 mt-3">
                  $356,000 <small>/month</small>
                </h2>
              </div>
              <div class="card-footer">
                                    <span
                                    ><i class="mdi mdi-sofa"></i
                                    >Beds:<strong>1</strong></span
                                    ><span
              ><i class="mdi mdi-scale-bathroom"></i
              >Baths:<strong>3</strong></span
              ><span
              ><i
                class="mdi mdi-move-resize-variant"
              ></i
              >Area:<strong>187 sq ft</strong></span
              >
              </div>
            </a
            >
          </div>
        </div>
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
  <!-- Join Team -->
  <section class="py-5 bg-primary">
    <div class="container">
      <div class="row align-items-center text-center text-md-left">
        <div class="col-md-8">
          <h2 class="text-white my-2">
            Join Our Professional Team & Agents
          </h2>
        </div>
        <div class="col-md-4 text-center text-md-right">
          <button type="button" class="btn btn-outline-light my-2">
            Read More
          </button>
          <button type="button" class="btn btn-light my-2">
            Contact Us
          </button>
        </div>
      </div>
    </div>
  </section>
  <!-- End Join Team -->

</template>


<script>
export default {
  name: 'HomeView',
}
</script>