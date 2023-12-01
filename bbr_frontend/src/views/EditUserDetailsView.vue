<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Edit profile</h1>

                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                </p>

                <RouterLink to="/profile/edit/password" class="underline">Edit password</RouterLink>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>First Name</label><br>
                        <input type="text" v-model="user.name" placeholder="Your first name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Last Name</label><br>
                        <input type="text" v-model="user.last_name" placeholder="Your last name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="user.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="userStore.user.level < 2">
                        <div>
                            <label>Employee Title</label><br>
                            <input type="text" v-model="user.employee_title" placeholder="Employee Title" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div>Level: {{ user.level }}</div>
                            <select v-model="user.level">
                            <option disabled value="">Please select one</option>
                            <option>1</option>
                            <option>2</option>
                        </select>
                    </template>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Save changes</button>
                    </div>
                </form>
                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()

        return {
            toastStore,
            userStore,
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                last_name: '',
                employee_title: '',
                level: '',
                password1: '',
                password2: ''
            },
            user: {},
            errors: [],
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

        submitForm() {
            this.errors = []

            if (this.user.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.user.name === '') {
                this.errors.push('Your first name is missing')
            }

            if (this.user.last_name === '') {
                this.errors.push('Your last name is missing')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('name', this.user.name)
                formData.append('last_name', this.user.last_name)
                formData.append('email', this.user.email)
                formData.append('employee_title', this.user.employee_title)
                formData.append('level', this.user.level)

                axios
                    .post(`/api/userlist/${this.$route.params.id}/edit/`, formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')

                                this.user.id = this.user.id,
                                this.form.name = this.form.name,
                                this.form.last_name = this.form.last_name,
                                this.form.email = this.form.email,
                                this.form.employee_title = this.form.employee_title,
                                this.form. level = this.form.level

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