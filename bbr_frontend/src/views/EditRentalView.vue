<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Name</label><br>
                        <input type="text" v-model="form.name" placeholder= "name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Address</label><br>
                        <input type="text" v-model="form.address" placeholder="address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Description</label><br>
                        <textarea v-model="form.description" placeholder="add a desription about the rental" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"></textarea>
                    </div>

                    <div>
                        <label>Price</label><br>
                        <p>$</p><input type="number" v-model="form.price" placeholder="0.00" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Profile Picture</label><br>
                        <input type="file" ref="file" @change="onFileChange">
                    </div>

                    <div>
                        <label>Room Picture</label><br>
                        <input type="file" ref="file2" @change="onFileChange">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Save Changes</button>
                    </div>
                </form>
            </div>
        </div>
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <img :src="rental.get_profilePic" class="w-full mb-4 rounded-xl">
                {{ rental.get_profilePic }}
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
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

    mounted() {
        this.getRentalDetails()
    },

    data() {
        return {
            rental: {},
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
        getRentalDetails() {
            axios
                .get(`/api/rentals/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)
                    this.rental.id = response.data.rental.id
                    this.form.name =  response.data.rental.name
                    this.form.address =  response.data.rental.address
                    this.form.description =  response.data.rental.description
                    this.form.price =  response.data.rental.price
                    this.form.file = response.data.rental.get_profilePic
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

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
                let formData = new FormData()
                formData.append('name', this.form.name)
                formData.append('address', this.form.address)
                formData.append('price', this.form.price)
                formData.append('description', this.form.description)
                formData.append('file', this.form.file)

                axios
                    .post(`/api/rentals/${this.$route.params.id}/edit/`, formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')

                                this.rental.id = this.rental.id,
                                this.form.name = this.form.name,
                                this.form.address = this.form.address,
                                this.form.price = this.form.price,
                                this.form.description = this.form.description
                                this.form.file = this.$refs.file.files[0]

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