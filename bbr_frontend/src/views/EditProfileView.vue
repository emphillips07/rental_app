<template>
    <div class="bg-gray-200 h-[100vh]">
        <div class="pt-8 flex justify-center mx-auto w-1/3">
            <div class="p-12 bg-white rounded-lg w-full shadow-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                <div>
                    <label class="text-xl font-bold">First Name</label><br>
                    <input type="text" v-model="form.name" placeholder="Your first name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <div>
                    <label class="text-xl font-bold">Last Name</label><br>
                    <input type="text" v-model="form.last_name" placeholder="Your last name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <div>
                    <label class="text-xl font-bold">Email Address</label><br>
                    <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <p><RouterLink to="/profile/edit/password" class="font-bold underline">Click Here</RouterLink> to change your password.</p>

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
            userStore
        }
    },

    data() {
        return {
            form: {
                email: this.userStore.user.email,
                name: this.userStore.user.name,
                last_name: this.userStore.user.last_name,
                employee_title: this.userStore.user.employee_title,
                level: this.userStore.user.level
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your first name is missing')
            }

            if (this.form.last_name === '') {
                this.errors.push('Your last name is missing')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('name', this.form.name)
                formData.append('last_name', this.form.last_name)
                formData.append('email', this.form.email)
                formData.append('employee_title', this.form.employee_title)
                formData.append('level', this.form.level)

                axios
                    .post('/api/editprofile/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')

                            this.userStore.setUserInfo({
                                id: this.userStore.user.id,
                                name: this.form.name,
                                last_name: this.form.last_name,
                                email: this.form.email,
                                employee_title: this.form.employee_title,
                                level: this.form.level
                            })

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