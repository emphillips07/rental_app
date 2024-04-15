<template>
    <div class="flex pt-10 bg-gray-200">
        <div class="grid grid-cols-3 gap-4 mx-auto w-3/4">
            <div
                class="p-4 bg-white border border-black rounded-lg w-full h-full shadow-lg"
                v-for="rental in rentals"
                v-bind:key="rentals.id"
            >
            <RouterLink :to="{name: 'rentaldetails', params:{'id': rental.id}}"><p class="text-xl font-semibold text-center border-b border-black pb-2">{{ rental.name }}</p></RouterLink>
            <template template 
                class=""
                v-for="reservation in reservations"
                v-bind:key="reservation.id"
            >
                <template template v-if="rental.id == reservation.location.id">
                <template template v-if="reservation.checkedIn == true">
                    <div class="">
                        <RouterLink :to="{name: 'userdetails', params:{'id': reservation.guest.id}}"><p>Name: {{ reservation.guest.name }}</p></RouterLink>
                        <p>Number of Guests: {{ reservation.guest.name }}</p>
                        <p>Phone Number: {{ reservation.guest.name }}</p>
                        <p>Check In: {{ formatDate(reservation.arrival) }}</p>
                        <p>Check Out: {{ formatDate(reservation.departure) }}</p>
                    </div>
                </template>
                </template>
            </template>
            </div>
        </div>

        <div class="grid grid-cols-1 mx-auto w-1/4 px-8">
            <div class="p-4 bg-white border border-black h-[50vh] shadow-md">
                <p class="text-xl font-semibold text-center border-b border-black pb-2">ARRIVALS</p>
                <template template v-for="reservation in reservations" v-bind:key="reservation.id">
                    <template template v-if="formatDate(reservation.arrival) == today()">
                    <template template v-if="reservation.get_status == true">
                    <template template v-if="reservation.isCurrent == true">
                    <template template v-if="reservation.checkedIn != true">
                        <div class="p-4 bg-white border border-black flex items-center justify-between">
                            <div class="">
                                <p>{{ reservation.guest.name }} {{ reservation.guest.last_name }}</p>
                                <p>{{ reservation.location.name }}</p>
                            </div>
                            <div>
                                <button class="px-4 py-2 bg-orange-300 text-white rounded-lg" @click="changeStatus(reservation.id)">Check in</button>
                            </div>
                        </div>
                    </template>
                    </template>
                    </template>
                    </template>

                </template>
            </div>

            <div class="p-4 bg-white border border-black h-[50vh] shadow-md">
                <p class="text-xl font-semibold text-center border-b border-black pb-2">DEPARTURES</p>
                <template template v-for="reservation in reservations" v-bind:key="reservation.id">
                    <template template v-if="formatDate(reservation.departure) == today()">
                    <template template v-if="reservation.checkedIn == true">
                    <template template v-if="reservation.isCurrent != true">
                        <div class="p-4 bg-white border border-black flex items-center justify-between">
                            <div class="">
                                <p>{{ reservation.guest.name }} {{ reservation.guest.last_name }}</p>
                                <p>{{ reservation.location.name }}</p>
                            </div>
                            <div>
                                <button class="px-4 py-2 bg-orange-300 text-white rounded-lg" @click="changeStatus(reservation.id)">Check Out</button>
                            </div>
                        </div>
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

export default {
    name: 'Reservations',

    components: {
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
                .get('/api/reservations/list/')
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
                .post(`api/reservations/${pk}/status`)
                .then(response => {
                    console.log('data', response.data)
                    window.location.reload();
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        formatDate(date) {
            const dateObj = new Date(date);
            const year = String(dateObj.getFullYear());
            const month = String(dateObj.getMonth() + 1).padStart(2, '0');
            const day = String(dateObj.getDate()).padStart(2, '0');

            return `${month}/${day}/${year}`;
        },

        today() {
            const dateObj = new Date();
            const year = String(dateObj.getFullYear());
            const month = String(dateObj.getMonth() + 1).padStart(2, '0');
            const day = String(dateObj.getDate()).padStart(2, '0');

            return `${month}/${day}/${year}`;
        }
    }
}
</script>