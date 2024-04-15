<template>
    <div class="flex justify-center pt-20 bg-gray-200 h-[100vh]">
        <div>
        <div class="flex justify-center">
            <div class="p-4 bg-white text-center rounded-lg shadow-lg">
                <p>Welcome {{ userStore.user.name }} {{ userStore.user.last_name }}</p>
                <div class="mt-6">
                    <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        to="/profile/edit"
                    >
                        Edit profile
                    </RouterLink>
                </div>
            </div>
        </div>
        <div class="w-1/2">
          <div class="flex flex-col">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg" v-for="reservation in reservations" v-bind:key="reservation.id">
              <div class="px-32 border ">
                <ReservationItem v-bind:reservation="reservation"/>
              </div>
            </div>
          </div>
        </div>
    </div>
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