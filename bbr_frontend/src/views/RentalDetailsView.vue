<template>
    <div class="inset-0 px-12 bg-gray-200 h-full z-0">
        <div v-if="userStore.user.isAuthenticated && userStore.user.id && userStore.user.level < 2" class="pt-8 fixed">
                        <button class="py-4 px-6 bg-orange-300 font-bold text-white rounded-lg">
                            <RouterLink :to="{name: 'rental_edit', params:{'id': rental.id}}">Edit</RouterLink>
                        </button>
                    </div>
        <div class="flex justify-center">
            <p class="text-center py-6 text-6xl underline font-bold">{{ rental.name }}</p>
        </div>
        <div class="grid grid-cols-7 gap-4">
            <div class="fixed justify-center col-span-1">
                
                <div class="p-8 bg-white rounded-lg shadow-lg">
                    <div class="">
                        <template v-if="userStore.user.isAuthenticated && userStore.user.id  && userStore.user.level > 2">
                        <form class="space-y-6" v-on:submit.prevent="submitForm">
                            <div>
                                <label class="text-xl font-bold">Arrival Date</label><br>
                                <VueDatePicker v-model="form.arrival" :format="format" :min-date="new Date()" :disabled-dates="disabledDates"/>
                            </div>
                            <div>
                                <label class="text-xl font-bold">Depature Date</label><br>
                                <VueDatePicker v-model="form.departure" :format="format" :min-date="form.arrival" :disabled-dates="disabledDates"/>
                            </div>
                            <select v-model="form.location" class="border border-gray-200">
                                <option disabled value="">Please Confirm Location</option>
                                <option v-bind:value="rental.id">{{ rental.name }}</option>
                            </select>
                            <template v-if="errors.length > 0">
                                <div class="bg-red-300 text-white rounded-lg p-6">
                                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                </div>
                            </template>

                            <div class="flex justify-center">
                                <button class="py-4 px-6 bg-orange-300 font-bold text-white rounded-lg">Reserve</button>
                            </div>
                        </form>
                        </template>
                        <template v-else-if="userStore.user.isAuthenticated && userStore.user.id  && userStore.user.level < 3">
                            <form class="space-y-6" v-on:submit.prevent="submitForm">
                                <div>
                                    <label class="text-xl font-bold">Guest Email</label><br>
                                    <input type="email" v-model="form.email" placeholder="" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                                </div>
                                <div>
                                    <label class="text-xl font-bold">Arrival Date</label><br>
                                    <VueDatePicker v-model="form.arrival" :format="format" :min-date="new Date()" :disabled-dates="disabledDates"/>
                                </div>
                                <div>
                                    <label class="text-xl font-bold">Depature Date</label><br>
                                    <VueDatePicker v-model="form.departure" :format="format" :min-date="min(form.arrival)" :max-date="max(form.arrival)" :disabled-dates="disabledDates"/>
                                </div>
                                <div>
                                    <label class="font-bold">Please Confirm Rental</label><br>
                                    <select v-model="form.location" class="border border-gray-200">
                                        <option disabled value="">Please Confirm Location</option>
                                        <option v-bind:value="rental.id">{{ rental.name }}</option>
                                    </select>
                                </div>
                                <template v-if="errors.length > 0">
                                    <div class="bg-red-300 text-white rounded-lg p-6">
                                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                    </div>
                                </template>

                                <div class="flex justify-center">
                                    <button class="py-4 px-6 bg-orange-300 font-bold text-white rounded-lg">Reserve</button>
                                </div>
                            </form>
                        </template>    
                        <template v-else>
                        <div class="">
                            <div class="">
                                <p class="text-2xl pb-8">Log in to reserve</p>
                                <RouterLink to="/login" class="flex justify-center mr-4 py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Log In</RouterLink>
                            </div>
                        </div>
                        </template>
                    </div>
                </div>
            </div>
            <div></div>
            <div class="col-span-1"></div>
            <div class="col-span-5">
                <div class="">
                    
                    <p class="dynamic-text-size">{{ rental.address }} Charleston, SC, 29405</p>
                    <p class="text-4xl py-3">${{ rental.price }} Per Night</p>
                    <p class="text-2xl py-3">{{ rental.description }}</p>
                </div> 
                <div class="grid grid-cols-3 gap-3">
                    <img v-bind:src="rental.get_profilePic" class="h-full w-full rounded-lg shadow-lg"/>
                    <img v-bind:src="rental.get_roomPicOne" class="h-full w-full rounded-lg shadow-lg"/>
                    <img v-bind:src="rental.get_roomPicTwo" class="h-full w-full rounded-lg shadow-lg"/>
                    <img v-bind:src="rental.get_roomPicThree" class="h-full w-full rounded-lg shadow-lg"/>
                    <img v-bind:src="rental.get_roomPicFour" class="h-full w-full rounded-lg shadow-lg"/>
                    <img v-bind:src="rental.get_roomPicFive" class="h-full w-full rounded-lg shadow-lg"/>                
                </div>
            </div>
            <div class="col-span-1">
                    <template v-for="reservation in reservations" v-bind:key="reservation.id">
                        {{ getDates(change(reservation.arrival), change(reservation.departure)) }}

                    </template>
                  
            </div>
        </div>   
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import { ref, reactive } from 'vue';
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
        
        let disabledDates = reactive([])

        const change = (date) => {
            return new Date(date);
        }

        function getDates(startDate, stopDate) {
            var currentDate = startDate;
            while (currentDate <= stopDate) {
                disabledDates.push(new Date (currentDate));
                currentDate.setDate(currentDate.getDate() + 1)
            }
        }

        const min = (date) => {
            const today = new Date();
            const arr = new Date(date);
            today.setDate(today.getDate() + 1)
            arr.setDate(arr.getDate() + 1)

            if (arr > today) {
                return arr;
            }
            else {
                return today;
            }
        }

        const max = (date) => {
            const arr = new Date(date)
            const year = new Date()
            year.setDate(year.getFullYear() + 1)
            var max = new Date(year)
            
            for (let i = 0; i < disabledDates.length; i++) {
                if (arr < disabledDates[i]) {
                    if (disabledDates[i] < max) {
                        max = disabledDates[i]
                    }
                }
            }

            return new Date(max)
        }

        return {
            userStore,
            toastStore,
            date,
            format,
            change,
            getDates,
            disabledDates,
            min,
            max
        }
    },

    data() {
        if (this.userStore.user.level > 2) {
            return {
                rental: {},
                reservations: [],
                form: {
                    email: this.userStore.user.email,
                    location: this.rental,
                    arrival: '',
                    departure: '',
                },
                errors: [],
            }
        }
        else {
            return {
                rental: {},
                reservations: [],
                form: {
                    email: '',
                    location: this.rental,
                    arrival: '',
                    departure: '',
                },
                errors: [],
            }
        }
    },

    mounted() {
        this.getRentalDetails()
        this.getReservations()
    },

    methods: {
        getRentalDetails() {
            axios
                .get(`/api/rentals/${this.$route.params.id}/`)
                .then(response => {
                    this.rental = response.data.rental
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getReservations() {
            axios
                .get('/api/reservations/list/')
                .then(response => {
                    console.log('data', response.data)
                    this.reservations = response.data.reservations.filter(data => data.isCancelled === false && (data.isCurrent === true || data.checkedIn === true) && data.location.id === `${this.$route.params.id}`)
                    console.log('res', this.reservations)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        retFormat(date) {
            const dateObj = new Date(date);
            const day = String(dateObj.getDate());
            const month = String(dateObj.getMonth() + 1);
            const year = String(dateObj.getFullYear());

            return `${year}-${month}-${day}T05:00:01Z`
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

            if (this.retFormat(this.form.arrival) >= this.retFormat(this.form.departure)) {
                this.errors.push('arrival date cannot be after departure date')
            }

            if (this.errors.length === 0) {
                axios
                    .post(`/api/reservations/create/`, this.form)
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

<style>
    .dynamic-text-size {
      font-size: calc(1vw + 1vh + 0.5vmin);
    }
  </style>