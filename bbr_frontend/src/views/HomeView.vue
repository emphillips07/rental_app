<template>
  <div class="bg-gray-200">
          <div class="grid grid-cols-4 gap-8 mx-auto pt-8 px-20 ">
          <div 
              class="bg-white rounded-lg w-full h-[40vh] shadow-lg hover:scale-110 transition-transform duration-300 ease-in-out"
              v-for="rental in rentals"
              v-bind:key="rental.id"
          >
          <RouterLink :to="{name: 'rentaldetails', params:{'id': rental.id}}">
          <div><img v-bind:src="rental.get_profilePic" class="w-full rounded-lg max-h-64" /></div>
          <div class="relative grid grid-cols-2 px-2 py-4 text-xl whitespace-nowrap bg-white rounded-lg">
              <div class="">
                  <p class="font-bold">{{ rental.name }}</p>
                  <p>{{ rental.address }}</p>
                  <p>${{ rental.price }} per night</p>
              </div>
              </div>
      </RouterLink>    
      </div>
      
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import RentalItem from '../components/RentalItem.vue'
import { RouterLink } from 'vue-router'

export default {
  name: 'RentalListView',

  components: {
  RentalItem,
  RouterLink
},

  data() {
      return {
          rentals: []
      }
  },

  mounted() {
      this.getRentals()
  },

  methods: {
      getRentals() {
          axios
              .get('/api/rentals/')
              .then(response => {
                  console.log('data', response.data)

                  this.rentals = response.data
              })
              .catch(error => {
                  console.log('error', error)
              })
      },
  }
}
</script>