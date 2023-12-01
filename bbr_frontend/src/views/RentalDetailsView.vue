<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
            >
            <figure class="image mb-4">   
            </figure>
            <p>{{ rental.name }}</p>
            <p>{{ rental.description }}</p>
            <div><img v-bind:src="rental.get_profilePic" /></div>
            </div>
            <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        :to="{name: 'rental_edit', params:{'id': rental.id}}"
                    >
                        Edit Rental
            </RouterLink>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RentalDetailView',

    components: {
    },

    data() {
        return {
            rental: {}
        }
    },

    actions: {

    },

    mounted() {
        this.getRentalDetails()
    },

    methods: {
        getRentalDetails() {
            axios
                .get(`/api/rentals/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.rental = response.data.rental
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>