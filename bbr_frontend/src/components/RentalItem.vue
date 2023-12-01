<template>
    <div>
        <RouterLink :to="{name: 'rentaldetails', params:{'id': rental.id}}"><p>{{ rental.name }}</p></RouterLink>
        
    </div>
    <div><img v-bind:src="rental.get_profilePic" class="w-[40px] rounded-full" /></div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    props: {
        rental: Object
    },

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
        }
    },

    methods: {
        
    },
    components: { RouterLink }
}
</script>