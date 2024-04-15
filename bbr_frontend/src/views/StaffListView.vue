<template>
    <div class="inset-0 p-10 bg-gray-200 h-[100vh] z-0">
        <div class="mx-auto">
            <div class="px-12 pt-2 pb-10 bg-white rounded-lg w-full shadow-lg">
                    <div class="flex justify-center pb-2">
                        <div class="">
                            <button class="py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">
                                <RouterLink to="/userlist">User List</RouterLink>
                            </button>
                        </div>
                    </div>
                <EasyDataTable :headers="headers" :items="users">
                    <template #item-name="{ name, id }">
                        <RouterLink :to="{name: 'userdetails', params:{'id': id}}">{{ name }}</RouterLink>
                    </template>
                    <template #item-operation="{ id }">
                        <div class="flex justify-end">
                            <RouterLink :to="{name: 'edituserdetails', params:{'id': id}}">    
                                <img
                                    src="../assets/edit.png"
                                    class="w-10"
                                />
                            </RouterLink>                           
                        </div>
                    </template>
                </EasyDataTable>
            </div>            
        </div> 
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {
    name: 'UserListView',

    components: {
        EasyDataTable: window['vue3-easy-data-table'],
        RouterLink
    },

    data() {
        return {
            users: [],
            headers: [
                { text: "First Name", value: "name"},
                { text: "Last Name", value: "last_name"},
                { text: "Email", value: "email"},
                { text: "Job Title", value: "employee_title"},
                { text: "", value: "operation"},
            ],
        }
    },

    beforeMount() {
        this.getUsers()
    },

    methods: {
        getUsers() {
            axios
                .get('/api/userlist/')
                .then(response => {
                    this.users = response.data.filter(data => data.level < 3)
                    console.log('data', this.users)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>