<template>
    <div class="bg-gray-200 h-[100vh]">
        <div class="pt-8 flex justify-evenly mx-auto">
            <div class="p-12 bg-white rounded-lg w-1/3 shadow-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div class="p-12">
                        <div class="p-2">
                            <label class="text-xl font-bold">Name</label><br>
                            <input type="text" v-model="form.name" placeholder= "name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div class="p-2">
                            <label class="text-xl font-bold">Address</label><br>
                            <input type="text" v-model="form.address" placeholder="address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div class="p-2">
                            <label class="text-xl font-bold">Description</label><br>
                            <textarea v-model="form.description" placeholder="add a desription about the rental" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"></textarea>
                        </div>

                        <div class="p-2">
                            <label class="text-xl font-bold">Price</label><br>
                            <input type="number" v-model="form.price" placeholder="0.00" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>
                    </div>
                    <div class="p-4">
                        <template v-if="errors.length > 0">
                            <div class="bg-red-300 text-white rounded-lg p-6">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                        </template>

                        <div>
                            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Save Changes</button>
                        </div>
                    </div>
                </form> 
            </div>

            <div class="p-12 bg-white rounded-lg shadow-lg">
                <div class="py-4">
                    <label class="text-xl font-bold">Profile Picture</label><br>
                    <input type="file" ref="file">
                </div>

                <div class="py-4">
                    <label class="text-xl font-bold">Room Picture One</label><br>
                    <input type="file" ref="file1">
                </div>

                <div class="py-4">
                    <label class="text-xl font-bold">Room Picture Two</label><br>
                    <input type="file" ref="file2">
                </div>

                <div class="py-4">
                    <label class="text-xl font-bold">Room Picture Three</label><br>
                    <input type="file" ref="file3">
                </div>

                <div class="py-4">
                    <label class="text-xl font-bold">Room Picture Four</label><br>
                    <input type="file" ref="file4">
                </div>

                <div class="py-4">
                    <label class="text-xl font-bold">Room Picture Five</label><br>
                    <input type="file" ref="file5">
                </div>
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
                    this.form.file1 = response.data.rental.get_roomPicOne
                    this.form.file2 = response.data.rental.get_roomPicTwo
                    this.form.file3 = response.data.rental.get_roomPicThree
                    this.form.file4 = response.data.rental.get_roomPicFour
                    this.form.file5 = response.data.rental.get_roomPicFive
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
                formData.append('profilePic', this.$refs.file.files[0])
                formData.append('roomPicOne', this.$refs.file1.files[0])
                formData.append('roomPicTwo', this.$refs.file2.files[0])
                formData.append('roomPicThree', this.$refs.file3.files[0])
                formData.append('roomPicFour', this.$refs.file4.files[0])
                formData.append('roomPicFive', this.$refs.file5.files[0])

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
                                this.form.description = this.form.description,
                                this.form.file = response.data.rental.get_profilePic
                                this.form.file1 = response.data.rental.get_roomPicOne
                                this.form.file2 = response.data.rental.get_roomPicTwo
                                this.form.file3 = response.data.rental.get_roomPicThree
                                this.form.file4 = response.data.rental.get_roomPicFour
                                this.form.file5 = response.data.rental.get_roomPicFive

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