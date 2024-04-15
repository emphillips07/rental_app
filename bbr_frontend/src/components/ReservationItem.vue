<template>
    <div class="flex items-center justify-between">
      <div>
        <img v-bind:src="reservation.location.get_profilePic" class="h-[100px] w-[100px] rounded-lg" />
      </div>
      <div>
        <template v-if="userStore.user.name != reservation.guest.name">
          <RouterLink :to="{name: 'userdetails', params:{'id': reservation.guest.id}}"><p>{{ reservation.guest.name }}</p></RouterLink>
        </template>
        <RouterLink :to="{name: 'rentaldetails', params:{'id': reservation.location.id}}"><p class="text-xl font-bold">{{ reservation.location.name }}</p></RouterLink>
        <p>Arrival: {{ reservation.arrival }}</p>
        <p>Departure: {{ reservation.departure }}</p>
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
        reservation: Object
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