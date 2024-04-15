<template>
    <div class="bg-gray-200 h-[100vh]">
        <div class="pt-8 flex justify-center mx-auto w-1/3">
            <div class="p-12 bg-white rounded-lg w-full shadow-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label class="text-xl font-bold">Name</label><br>
                        <input type="text" v-model="form.name" placeholder="name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-xl font-bold">Address</label><br>
                        <input type="text" v-model="form.address" placeholder="address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-xl font-bold">Description</label><br>
                        <textarea v-model="form.description" placeholder="add a desription about the rental" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"></textarea>
                    </div>

                    <div>
                        <label class="text-xl font-bold">Price</label><br>
                        <input type="number" v-model="form.price" placeholder="0.00" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Create Rental</button>
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
                name: '',
                address: '',
                description: '',
                price: '',
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.name === '') {
                this.errors.push('Rental name is missing')
            }

            if (this.form.address === '') {
                this.errors.push('Rental address is missing')
            }

            if (this.form.description === '') {
                this.errors.push('Rental description is missing')
            }

            if (this.form.price === '') {
                this.errors.push('Rental price is missing')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/rentals/create/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Rental Created.', 'bg-emerald-500')

                            this.form.name = ''
                            this.form.address = ''
                            this.form.description = ''
                            this.form.price = ''

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