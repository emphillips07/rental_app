<template>
    <div class="grid grid-cols-2 gap-2">
        <div class="">
            <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="rental in rentals"
                v-bind:key="rentals.id"
            >
                <RentalItem v-bind:rental="rental" />
            <template template 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="reservation in reservations"
                v-bind:key="reservation.id"
            >
                <template template v-if="rental.id == reservation.location.id">
                <template template v-if="reservation.checkedIn == true">
                    <div class="grid grid-cols-2 gap-2">
                        <div><ReservationItem v-bind:reservation="reservation" /></div>
                        <div><button class="py-3 px-4 bg-purple-600 text-white rounded-lg" @click="changeStatus(reservation.id)">Check Out</button></div>
                    </div>
                </template>
                </template>
            </template>
            </div>
        </div>

        <div class="">
            <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="rental in rentals"
                v-bind:key="rentals.id"
            >
                <p>{{ rental.name }}</p>
            <template template 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="reservation in reservations"
                v-bind:key="reservation.id"
            >
                <template template v-if="rental.id == reservation.location.id">
                <template template v-if="reservation.get_status == true">
                <template template v-if="reservation.isCurrent == true">
                <template template v-if="reservation.checkedIn != true">
                    <div class="grid grid-cols-2 gap-2">
                        <div><p>{{ reservation.guest.name }}</p></div>
                        <div><button class="py-3 px-4 bg-purple-600 text-white rounded-lg" @click="changeStatus(reservation.id)">Check in</button></div>
                    </div>
                </template>
                </template>
                </template>
                </template>
                
            </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ReservationItem from '../components/ReservationItem.vue'
import RentalItem from '../components/RentalItem.vue'

export default {
    name: 'Reservations',

    components: {
        ReservationItem,
        RentalItem
    },

    data() {
        return {
            rentals: [],
            reservations: []
        }
    },

    mounted() {
        this.getReservations()
    },

    methods: {
        getReservations() {
            axios
                .get('/api/reservations/current')
                .then(response => {
                    console.log('data', response.data)
                    this.rentals = response.data.rentals
                    this.reservations = response.data.reservations
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        changeStatus(pk) {
            axios
                .post(`api/reservations/${pk}/`)
                .then(response => {
                    console.log('data', response.data)
                    window.location.reload();
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>