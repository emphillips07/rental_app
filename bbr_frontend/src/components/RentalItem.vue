<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2">
    <div class="main-left">
      <div class="p-1 bg-white rounded-lg">  
        <img v-bind:src="rental.get_profilePic" class="h-[300px] w-[300px] rounded-lg" />
      </div>
    </div>
    <div class="main-right">
      <div class="p-12 text-center">
        <RouterLink :to="{name: 'rentaldetails', params:{'id': rental.id}}"><p class="text-3xl font-bold mb-4 text-white hover:text-blue-500">{{ rental.name }}</p></RouterLink>
        <p class="text-xl text-white">{{ rental.address }}</p>
        <p class="text-white">${{ rental.price }}</p>
        <div class="py-12">  
            <template template v-if="userStore.user.level < 2">
              <RouterLink :to="{name: 'rental_edit', params:{'id': rental.id}}" class="text-xl"><button class="py-4 px-6 bg-blue-300 text-white rounded-lg">Edit</button></RouterLink>
            </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    props: {
        rental: Object
    },

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    data() {
        return {
        }
    },

    methods: {
        
    },
    components: { RouterLink }
}
</script>