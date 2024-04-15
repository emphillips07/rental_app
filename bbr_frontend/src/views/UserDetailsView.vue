<template>
    <div class="pt-20 max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
            >
            <p>{{ user.name }}</p>
            <p>{{ user.last_name }}</p>
            <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        :to="{name: 'edituserdetails', params:{'id': user.id}}"
                    >
                        Edit profile
            </RouterLink>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UserDetailsView',

    components: {
    },

    data() {
        return {
            user: {}
        }
    },
 
    mounted() {
        this.getUserDetails()
    },

    methods: {
        getUserDetails() {
            axios
                .get(`/api/userlist/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>