<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="user in users"
                v-bind:key="user.id"
            >
                <UserItem v-bind:user="user" />
            </div>
           
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import UserItem from '../components/UserItem.vue'

export default {
    name: 'UserListView',

    components: {
        UserItem
    },

    data() {
        return {
            users: []
        }
    },

    mounted() {
        this.getUsers()
    },

    methods: {
        getUsers() {
            axios
                .get('/api/userlist/')
                .then(response => {
                    console.log('data', response.data)

                    this.users = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>