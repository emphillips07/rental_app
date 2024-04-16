<template>
    <div class="bg-gray-200 h-[100vh]">
        <div class="pt-8 flex justify-center mx-auto w-1/3">
            <div class="p-12 bg-white rounded-lg w-full shadow-lg">
            <div class="">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div v-if="userStore.user.level > 2">
                        <p>{{ userStore.user.email }}</p>
                    </div>
                    <div v-else>
                        <label class="text-xl font-bold">Guest Email</label><br>
                        <input type="email" v-model="form.email" placeholder="" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-xl font-bold">Location</label><br>
                        <select v-model="form.location" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                            <option disabled value="">Please Select Location</option>
                            <option  v-for="rental in rentals" v-bind:value="rental.id">{{ rental.name }}</option>
                        </select>
                    </div>
                    
                    <div>
                        <label class="text-xl font-bold">Arrival Date</label><br>
                        <VueDatePicker v-model="form.arrival" :format="format" :min-date="new Date()"/>
                    </div>

                    <div>
                        <label class="text-xl font-bold">Depature Date</label><br>
                        <VueDatePicker v-model="form.departure" :format="format"/>
                    </div>
                    <p> {{ form.arrival }}</p>
                    <p> {{ form.departure }}</p>  

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Reserve</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import { ref } from 'vue';
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

export default {
    components: {
        VueDatePicker
    },

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore() 
        const date = ref();
        const format = (date) => {
            const day = date.getDate();
            const month = date.getMonth() + 1;
            const year = date.getFullYear();
        
            return `${month}/${day}/${year}`;
        }
        
        return {
            userStore,
            toastStore,
            date,
            format,
        }
    },

    data() {
            return {
                rentals: [],
                reservations: [],
                form: {
                    email: '',
                    arrival: '',
                    departure: '',
                    location: '',
                },
                errors: [],
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
                    this.rentals = response.data.rentals
                    this.reservations = response.data.reservations
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('e-mail is missing')
            }

            if (this.form.arrival === '') {
                this.errors.push('arrival is missing')
            }

            if (this.form.departure === '') {
                this.errors.push('departure is missing')
            }

            if (this.form.location === '') {
                this.errors.push('location is missing')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/reservations/create/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Success', 'bg-emerald-500')
                            this.form.email = ''
                            this.form.arrival = ''
                            this.form.departure = ''
                            this.form.location = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                        console.log(this.arrival)
                    })
            }
        }
    }
}
</script>