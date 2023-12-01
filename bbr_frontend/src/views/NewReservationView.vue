<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div v-if="userStore.user.level > 2">
                        <p>userStore.user.email</p>
                    </div>
                    <div v-else>
                        <label>Guest Email</label><br>
                        <input type="email" v-model="form.email" placeholder="" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Arrival Date</label><br>
                        <input type="date" v-model="form.arrival" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Departure Date</label><br>
                        <input type="date" v-model="form.departure" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <select v-model="form.location">
                        <option v-for="rental in rentals" v-bind:value="rental.id">{{ rental.name }}</option>
                        </select>
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Reserve</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
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
            rentals: [],
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

        disableDates(date) {
            
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
                    })
            }
        }
    }
}
</script>