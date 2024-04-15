<template>
    <div class="bg-gray-200 h-[100vh]">
        <div class="pt-8 flex justify-center mx-auto w-1/3">
            <div class="p-12 bg-white rounded-lg w-full shadow-lg">
            <div class="">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label class="text-xl font-bold">Arrival Date</label><br>
                        <VueDatePicker v-model="form.arrival" :format="format" :min-date="new Date()"/>
                    </div>

                    <div>
                        <label class="text-xl font-bold">Depature Date</label><br>
                        <VueDatePicker v-model="form.departure" :format="format" :min-date="new Date()"/>
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
import { ref } from 'vue'
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
            form: {
                arrival: '',
                departure: '',
            },
            reservation: {},
            errors: [],
        }
    },

    mounted() {
        this.getReservations()
    },

    methods: {
        getReservations() {
            axios
                .get(`/api/reservations/${this.$route.params.id}`)
                .then(response => {
                    console.log('data', response.data)
                    this.reservation = response.data.reservation
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            this.errors = []

            if (this.form.arrival === '') {
                this.errors.push('arrival is missing')
            }

            if (this.form.departure === '') {
                this.errors.push('departure is missing')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('arrival', this.reservation.arrival)
                formData.append('departure', this.reservation.departure)

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