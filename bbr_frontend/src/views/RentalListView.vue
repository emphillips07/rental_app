<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <RouterLink :to="{name: 'reservation_create'}">Reserve Now</RouterLink>
            </div>
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="rental in rentals"
                v-bind:key="rental.id"
            >
                <RentalItem v-bind:rental="rental" />
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