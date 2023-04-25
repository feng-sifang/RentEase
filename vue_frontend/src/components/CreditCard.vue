<template>
  <div class="col-lg-9 col-md-9">
    <form>
      <div
        class="card padding-card"
        v-for="(creditCard, index) in this.creditCards"
        :key="index">
        <div class="card-body">
          <h5 class="card-title mb-4">
            Credit Card {{ index }}
          </h5>
          <div class="form-group">
            <label>Credit Card Number <span class="text-danger">*</span></label>
            <input
              type="text"
              class="form-control"
              v-model="creditCard['number']"
            />
          </div>
          <div class="form-group">
            <label>Holder's Name <span class="text-danger">*</span></label>
            <input
              type="text"
              class="form-control"
              v-model="creditCard['holder_name']"
            />
          </div>
          <div class="form-group">
            <label>Expiry Date <span class="text-danger">*</span></label>
            <input
              type="email"
              class="form-control"
              v-model="creditCard['expiry_date']"
            />
          </div>
          <div class="form-group">
            <label>CVV <span class="text-danger">*</span></label>
            <input
              type="email"
              class="form-control"
              v-model="creditCard['cvv']"
            />
          </div>
          <div class="form-group">
            <label>Country <span class="text-danger">*</span></label>
            <input
              type="email"
              class="form-control"
              v-model="creditCard['country']"
            />
          </div>
          <div class="form-group">
            <label>City <span class="text-danger">*</span></label>
            <input
              type="email"
              class="form-control"
              v-model="creditCard['city']"
            />
          </div>
          <div class="form-group">
            <label>Street <span class="text-danger">*</span></label>
            <input
              type="email"
              class="form-control"
              v-model="creditCard['street']"
            />
          </div>
          <div class="form-group">
            <label>ZIP <span class="text-danger">*</span></label>
            <input
              type="email"
              class="form-control"
              v-model="creditCard['zip']"
            />
          </div>
        </div>
      </div>

      <button type="submit" class="btn btn-success">
        SAVE EDITS
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CreditCard',

  data () {
    return {
      cardIndex: 0,
      creditCards: [],
    }
  },

  methods: {
    async getUserID () {
      const response = (await this.axios.get('/get-user-profile/')).data
      this.userID = response['user_id']
      console.log('userID: ', this.userID)
    },

    async getCreditCard () {
      const response = (await this.axios.get('/get-user-creditcard/')).data
      if (response.success) {
        this.cardIndex = response['credit_cards'].length
        if (this.cardIndex > 0) {
          this.creditCards = response['credit_cards']
          console.log('creditcard: ', this.creditCards)
        } else {
          this.cardIndex = 0
        }
        console.log('No. of credit cards: ', this.cardIndex)
      }
    },
  },

  mounted () {
    this.getUserID()
    this.getCreditCard()
  },
}
</script>