<template>
    <div class="bg-gray-200 h-[100vh]">
        <div class="pt-8 flex justify-center mx-auto w-1/3">
            <div class="p-12 bg-white rounded-lg w-full shadow-lg">
            <div class="">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div  class="text-xl font-bold">
                        <template v-if="userStore.user.level < 3 && reservation.guest">{{ reservation.guest.name }}  {{ reservation.guest.last_name }}</template>
                    </div>
                    <div class="text-xl font-bold">
                        <template v-if="reservation.location"> {{ reservation.location.name }}</template>
                    </div>
                    <template v-for="x in reservations" v-bind:key="reservation.id">
                        <template v-if="x.location.id = reservation.location.id && x.id != reservation.id">
                            {{ getDates(change(x.arrival), change(x.departure)) }}
                        </template>                        
                    </template>
                    <div>
                        <label class="text-xl font-bold">Arrival Date</label><br>
                        <VueDatePicker v-model="reservation.arrival" :format="format" :min-date="new Date()" :disabled-dates="disabledDates"/>
                    </div>
                    <div>
                        <label class="text-xl font-bold">Depature Date</label><br>
                        <VueDatePicker v-model="reservation.departure" :format="format" :min-date="min(reservation.arrival, reservation.checkedIn)" :max-date="max(reservation.arrival)" :disabled-dates="disabledDates"/>
                    </div>
                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Save Changes</button>
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
import { ref, reactive } from 'vue'
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

        const min = (date, checkedIn) => {
            const today = new Date();
            const arr = new Date(date);
            arr.setDate(arr.getDate() + 1)

            if (checkedIn === true) {
                today.setDate(today.getDate())
            }
            else (
                today.setDate(today.getDate() + 1)
            )

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
            disabledDates,
            change,
            getDates,
            min,
            max
        }
    },

    data() {
        return {
            form: {
                arrival: '',
                departure: '',
                checkedIn: '',
                guest: {},
                isCancelled: '',
                isCurrent: '',
                location: {}
            },
            reservation: {},
            rental: {},
            reservations: [],
            errors: [],
        }
    },

    computed: {

    },

    mounted() {
        this.getReservationDetails()
        this.getReservations()
    },

    methods: {
        getReservationDetails() {
            axios
                .get(`/api/reservations/${this.$route.params.id}`)
                .then(response => {
                    this.reservation = response.data.reservation
                    this.rental = response.data.reservation.location
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getReservations() {
            axios
                .get('/api/reservations/list/')
                .then(response => {
                    this.reservations = response.data.reservations.filter(data => data.isCancelled === false && (data.isCurrent === true || data.checkedIn === true)
                                                                          && data.location.id === this.rental.id)
                    console.log('res', this.reservations)
                    console.log('location', this.rental.id)
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

            if (this.reservation.arrival === '') {
                this.errors.push('arrival is missing')
            }

            if (this.reservation.departure === '') {
                this.errors.push('departure is missing')
            }

            if ( this.retFormat(this.reservation.arrival) >= this.retFormat(this.reservation.departure)) {
                this.errors.push('arrival date cannot be after departure date')
            }
            
            console.log('arrival', this.retFormat(this.reservation.arrival))
            console.log('departure', this.retFormat(this.reservation.departure))

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('arrival', this.retFormat(this.reservation.arrival))
                formData.append('departure', this.retFormat(this.reservation.departure))
                
                axios
                    .post(`/api/reservations/${this.$route.params.id}/edit/`, formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')
                            this.reservation.id = this.reservation.id
                            this.form.arrival = this.form.arrival
                            this.form.departure = this.form.departure
                            this.$router.back()                            
                        } else {
                            this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
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