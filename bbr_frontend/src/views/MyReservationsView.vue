<template>
    <div class="p-10 mx-auto bg-gray-200 h-[100vh]">
        <div class="main-center col-span-3 space-y-4 shadow-lg">    
            <EasyDataTable :headers="headers" :items="reservations">
                <template #item-location="{ location }">
                    <RouterLink :to="{name: 'rentaldetails', params:{'id': location.id}}">{{ location.name }}</RouterLink>
                </template>
                <template #item-status="{ isCurrent, checkedIn }">
                    <template template v-if="isCurrent == true && checkedIn != true">Upcoming</template>
                    <template template v-else-if="isCurrent != true && checkedIn == true">Current</template>
                    <template template v-else="isCurrent != true && checkedIn != true">Past</template>
                </template>
                <template #item-arrival="{ arrival }">
                    {{ formatDate(arrival) }}
                </template>
                <template #item-departure="{ departure }">
                    {{ formatDate(departure) }}
                </template>
            </EasyDataTable>            
        </div> 
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {
    name: 'MyReservationsView',

    components: {
        EasyDataTable: window['vue3-easy-data-table'],
        RouterLink
    },

    data() {
        return {
            reservations: [],
            rentals: [],
            headers: [
                { text: "Property", value: "location"},
                { text: "Check In", value: "arrival"},
                { text: "Check Out", value: "departure"},
                { text: "Status", value: "status"},
            ],
        }
    },

    beforeMount() {
        this.getReservations()
    },

    methods: {
        getReservations() {
            axios
                .get('/api/reservations/')
                .then(response => {
                    console.log('data', response.data)

                    this.reservations = response.data
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
    }
}
</script>