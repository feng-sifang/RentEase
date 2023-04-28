<template>
  <div class="col-lg-12 col-md-12">
    <div class="card card-list card-list-view">
        <div class="row no-gutters">
          <div class="col-lg-5 col-md-5">
          <span class="badge badge-success">
            Available
          </span>
            <img
                class="card-img-top"
                :src="`/static/picture/${property.property_type.toLowerCase()}.png`"
                alt="Card image cap"
            >
          </div>
          <div class="col-lg-7 col-md-7">
            <div class="card-body"><span class="float-right text-success"><router-link :to="{ name: 'edit', params: { itemId: property.property_id } }"><i
                class="mdi mdi-table-edit">Manage</i></router-link></span>
              <h5 class="card-title">
                {{ property.property_type === 'CommercialBuilding' ? 'Commercial Building' : property.property_type }}
              </h5>
              <h6
                  class="card-subtitle mb-2 text-muted">
                <i class="mdi mdi-home-map-marker"></i>
                {{ property.property_address }},
                {{ property.property_city }},
                {{ property.property_state }}</h6>
              <h2 class="text-success mb-0 mt-3">
                ${{ property.property_price }}<small>/month</small>
              </h2>
            </div>
            <div class="card-footer">
            <span><i class="mdi mdi-sofa"></i>
              Beds: <strong>3</strong>
            </span>
              <span><i class="mdi mdi-scale-bathroom"></i>
              Baths: <strong>2</strong>
            </span>
              <span><i class="mdi mdi-move-resize-variant"></i>
              Area: <strong>587 sq ft</strong>
            </span>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PropertyListItem',

  props: {
    property: {
      type: Object,
      required: true,
    },
  },
}
</script>
