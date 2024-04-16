<template>
    <div class="p-10 mx-auto bg-gray-200 h-[100vh]">
        <div class="main-center col-span-3 space-y-4 shadow-lg">  
            <EasyDataTable :headers="headers" :items="reservations">
                <template #item-location="{ location }">
                    <RouterLink :to="{name: 'rentaldetails', params:{'id': location.id}}">{{ location.name }}</RouterLink>
                </template>
                <template #item-guest="{ guest }">
                   <p>{{ guest.name }} {{ guest.last_name }}</p>
                </template>
                <template #item-status="{ isCurrent, checkedIn, isCancelled }">
                    <template template v-if="isCancelled == true" v-bind:value="Cancelled">Cancelled</template>
                    <template template v-else>
                        <template template v-if="isCurrent == true && checkedIn != true">Upcoming</template>
                        <template template v-else-if="isCurrent != true && checkedIn == true">Current</template>
                        <template template v-else="isCurrent != true && checkedIn != true">Past</template>
                    </template>
                </template>
                <template #item-arrival="{ arrival }">
                    {{ formatDate(arrival) }}
                </template>
                <template #item-departure="{ departure }">
                    {{ formatDate(departure) }}
                </template>
                <template #item-operation="{ id, isCurrent, checkedIn, isCancelled }">
                        <div class="flex justify-end items-center">
                            <div v-if="isCurrent == true && isCancelled != true" class="px-2">
                                <RouterLink :to="{name: 'reservations_edit', params:{'id': id}}">
                                    <img
                                        src="../assets/edit.png"
                                        class="w-10"
                                    /></RouterLink>
                            </div>
                            <div v-if="isCurrent == true && checkedIn != true && isCancelled != true">
                                <button @click="() => cancel(id)">    
                                    <svg xmlns="http://www.w3.org/2000/svg" width="27" height="27" viewBox="0 0 24 24" fill="none" stroke="#FF0000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line></svg>                                </button>
                            </div>                   
                        </div>
                    </template>
            </EasyDataTable>         
        </div> 
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { ref, computed } from 'vue';
import { useToastStore } from '@/stores/toast'

export default {
    name: 'MyReservationsView',
    
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore,
        }
    },

    computed: {

    },

    components: {
        EasyDataTable: window['vue3-easy-data-table'],
        RouterLink,
    },

    data() {
        return {
            reservations: [],
            rentals: [],
            headers: [
                { text: "Property", value: "location"},
                { text: "Guest", value: "guest"},
                { text: "Check In", value: "arrival"},
                { text: "Check Out", value: "departure"},
                { text: "Status", value: "status"},
                { text: "", value: "operation"},
            ],
        }
    },

    beforeMount() {
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

        formatDate(date) {
            const dateObj = new Date(date);
            const year = String(dateObj.getFullYear());
            const month = String(dateObj.getMonth() + 1);
            const day = String(dateObj.getDate());

            return `${month}/${day}/${year}`;
        },

        cancel(pk) {
            axios
                .post(`api/reservations/${pk}/cancel`)
                .then(response => {
                    console.log('data', response.data)
                    window.location.reload();
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>