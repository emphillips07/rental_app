<template>
    <div>
        <RouterLink :to="{name: 'userdetails', params:{'id': reservation.guest.id}}"><p>{{ reservation.guest.name }}</p></RouterLink>
        <p>{{ reservation.arrival }}</p>
        <p>{{ reservation.departure }}</p>
        <RouterLink :to="{name: 'rentaldetails', params:{'id': reservation.location.id}}"><p>{{ reservation.location.name }}</p></RouterLink>
        <p>{{ reservation.Checkedin }}</p>
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