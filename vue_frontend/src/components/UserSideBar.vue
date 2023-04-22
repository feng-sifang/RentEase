<template>
  <div class="col-lg-3 col-md-3">
    <!-- Collapse -->
    <div class="card padding-card tab-view user-pages-sidebar">
      <div class="card-body">
        <!-- Heading -->
        <h6 class="text-uppercase mt-0 mb-3">Account</h6>
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link active text-success" href="">
              User Profile</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              My Properties
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Favorite Properties
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Add Property
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserSideBar',
}
</script>
