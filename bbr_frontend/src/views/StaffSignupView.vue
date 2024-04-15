<template>
    <div class="bg-gray-200 h-full">
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
                        <label class="text-xl font-bold">Email</label><br>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-xl font-bold">Job Title</label><br>
                        <input type="text" v-model="form.employee_title" placeholder="Employee Title" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-xl font-bold">Level: {{ form.level }}</label><br>
                        <select v-model="form.level" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        <option disabled value="">Please select one</option>
                            <option value="1">Manager</option>
                            <option value="2">Staff</option>
                        </select>
                    </div>

                    <div>
                        <label class="text-xl font-bold">Password</label><br>
                        <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-xl font-bold">Repeat password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Log In</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
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

            if (this.form.employee_title === '') {
                this.errors.push('Your title is missing')
            }

            if (this.form.level === '') {
                this.errors.push('Your level is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/staffsignup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered.', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.last_name = ''
                            this.form.employee_title = ''
                            this.form.level = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
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