<template>
    <div>
        <RouterLink :to="{name: 'userdetails', params:{'id': user.id}}"><p>{{ user.name }}</p></RouterLink>
    </div>
    <template v-if="userStore.user.level < 2">
    <button 
                        class="flex justify-right py-4 px-3 bg-red-600 text-xs text-white rounded-lg" 
                        @click="deleteUser"
                    >
                        Delete User
                    </button>
                </template>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    props: {
        user: Object
    },

    emits: ['deleteUser'],

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    data() {
    },

    methods: {
        deleteUser() {
            this.$emit('deleteUser', this.user.id)

            axios
                .delete(`/api/userlist/${this.user.id}/delete/`)
                .then(response => {
                    console.log(response.data)

                    this.toastStore.showToast(5000, 'The user was deleted', 'bg-emerald-500')
                })
                .catch(error => {
                    console.log("error", error);
                })
        },
    },
    components: { RouterLink }
}
</script>