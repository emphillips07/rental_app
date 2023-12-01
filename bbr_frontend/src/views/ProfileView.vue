<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <p><strong>{{ userStore.user.name }}</strong></p>

                <div class="mt-6">
                    <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        to="/profile/edit"
                    >
                        Edit profile
                    </RouterLink>

                    <button 
                        class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg" 
                        @click="logout"
                    >
                        Log out
                    </button>
                </div>
                
                <template v-if="userStore.user.level < 3">
                    <div><p><strong>{{ userStore.user.employee_title }}</strong></p></div>
                    <div><p><strong>{{ userStore.user.level }}</strong></p></div>
                    <div><p><strong>{{ userStore.user.last_name }}</strong></p></div>
            </template>
            </div>
        </div>
        <div 
                    class="p-4 bg-white border border-gray-200 rounded-lg"
                    v-for="reservation in reservations" 
                    v-bind:key="reservation.id"
                >
                <ReservationItem v-bind:reservation="reservation"/></div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import ReservationItem from '../components/ReservationItem.vue'

export default {
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        ReservationItem
    },

    data() {
        return {
            user: {
                id: ''
            },
            reservations: []
        }
    },

    mounted() {
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

        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/login')
        }
    }
}
</script>