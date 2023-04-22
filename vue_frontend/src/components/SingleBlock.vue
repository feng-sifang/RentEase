<template>
  <div class="col-lg-4 col-md-4">
    <div class="card card-list">
      <a href="#">
        <span class="badge badge-success">
          For Sale
        </span>
        <img
          class="card-img-top"
          src="/static/picture/11.png"
          alt="Card image cap"
        />
        <div class="card-body">
          <h5 class="card-title">
            House in Kent Street
          </h5>
          <h6 class="card-subtitle mb-2 text-muted">
            <i class="mdi mdi-home-map-marker"></i>
            127 Kent Sreet,Sydny,NEW 2000
          </h6>
          <div class="review-block-rate">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <span class="badge-pill badge-success ml-2">3.2</span>
          </div>
          <h2 class="text-success mb-0 mt-3">
            $130,000 <small>/month</small>
          </h2>
        </div>
        <div class="card-footer">
          <span>
            <i class="mdi mdi-sofa"></i>
            Beds:<strong>3</strong>
          </span>
          <span>
            <i class="mdi mdi-scale-bathroom"></i>
            Baths:<strong>2</strong>
          </span>
          <span>
            <i class="mdi mdi-move-resize-variant"></i>
            Area:<strong>587 sq ft</strong>
          </span>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SingleBlock',
}
</script>
