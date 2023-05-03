<template>
  <div class="col-lg-12 col-md-12" >
    <div class="card card-list card-list-view">
      <router-link :to="{ name: 'view', params: { itemId: property.property_id } }"><div class="row no-gutters">
        <div class="col-lg-5 col-md-5">

          <img
              class="card-img-top"
              :src="`/static/picture/${property.property_type.toLowerCase()}.png`"
              alt="Card image cap"
          >
        </div>
        <div class="col-lg-7 col-md-7">
          <div class="card-body"><span class="float-right text-success" v-if="userType==='Agent'"><router-link
              :to="{ name: 'edit', params: { itemId: property.property_id } }"><i
              class="mdi mdi-table-edit">Manage</i></router-link>
            <a class="float-right text-danger" @click="sendItemId"><i
                class="mdi mdi-delete-forever"></i>Delete</a>
</span>
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
              <small>Total Cost: </small>${{ property.property_price }}
            </h2>
          </div>
          <div class="card-footer">
            <span><i class="mdi mdi-sofa"></i>
              Start Date: <strong>{{property.start_date}}</strong>
            </span>
            <span><i class="mdi mdi-scale-bathroom"></i>
              End Date: <strong>{{property.end_date}}</strong>
            </span>
            <span><i class="mdi mdi-move-resize-variant"></i>
              Booking ID: <strong>{{property.booking_id}}</strong>
            </span>
          </div>
        </div>
      </div> </router-link>
    </div>
  </div>
</template>

<script>
import {onMounted} from "vue";

export default {
  name: 'BookingListItem',
    props: {
    property: {
      type: Object,
      required: true,
    },
    userType: {
      type: String,
      required: true,
    },
  },
  setup(props, {emit}) {
    const sendItemId = () => {
    emit('sent-item-id', props.property.property_id)
    onMounted(async () => {
      console.log("property",props.property)
    })
  }
  return{
      sendItemId
  }
  },


}
</script>
