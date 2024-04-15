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
              <div class="py-4">
                  <div class="flex justify-end">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2L9.38 8.236 2 9.472l5.5 5.344L5.764 22l6.236-3.236L18.236 22l-1.5-7.184L22 9.472l-7.38-1.236L12 2z" />
                      </svg>
                      <p class="px-2">5.0</p>
                  </div>
                  <p class="flex justify-end p-2"># Beds</p>
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