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
                <template #item-operation="{ id }">
                        <div>
                            <button @click="() => deleteReservation(id)">    
                                <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="#FF0000" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                            </button>                   
                        </div>
                    </template>
            </EasyDataTable>         
        </div> 
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { ref } from 'vue';
import { useToastStore } from '@/stores/toast'

export default {
    name: 'MyReservationsView',
    
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
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
                { text: "Delete", value: "operation"},
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
            const month = String(dateObj.getMonth() + 1).padStart(2, '0');
            const day = String(dateObj.getDate()).padStart(2, '0');

            return `${month}/${day}/${year}`;
        },

        deleteReservation(pk) {
            axios
                .delete(`/api/reservations/${pk}/delete/`)
                .then(response => {
                    console.log(response.data)

                    this.toastStore.showToast(5000, 'The reservation was deleted', 'bg-emerald-500')
                    window.location.reload();
                })
                .catch(error => {
                    console.log("error", error);
                })
        },
    }
}
</script>