<template>
  <nav class="py-10 px-8 border-b border-gray-200">
      <div class="mx-auto">
          <div class="flex items-center justify-between">
              <div class="menu-left">
                <RouterLink to="/" class="text-xl">Best Beach Rentals</RouterLink>
              </div>
              <div class="menu-center flex space-x-12">
                <RouterLink to="/rentals" class="text-purple-700">Rentals</RouterLink>
                <template template v-if="userStore.user.level < 3">
                    <RouterLink to="/create" class="text-xl">Create Rental</RouterLink>
                  </template>
                <template template v-if="userStore.user.level < 2">
                    <RouterLink to="/staffsignup" class="text-xl">Employee Signup</RouterLink>
                  </template>
                  <template template v-if="userStore.user.level < 3">
                    <RouterLink to="/userlist" class="text-xl">User List</RouterLink>
                  </template>
                  <div>
                    <RouterLink to="/reservations/current" class="text-xl">In House</RouterLink>
                  </div>
              </div>
              <div class="menu-right">
                  <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                      <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                        Profile  
                      </RouterLink>
                  </template>

                  <template v-else>
                      <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                      <RouterLink to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</RouterLink>
                  </template>
              </div>
          </div>
      </div>
  </nav>


      <RouterView />


  <Toast />
</template>


<script>
  import axios from 'axios'
  import Toast from '@/components/Toast.vue'
  import { useUserStore } from '@/stores/user'

  export default {
      setup() {
          const userStore = useUserStore()

          return {
              userStore
          }
      },

      components: {
          Toast
      },

      beforeCreate() {
          this.userStore.initStore()

          const token = this.userStore.user.access

          if (token) {
              axios.defaults.headers.common["Authorization"] = "Bearer " + token;
          } else {
              axios.defaults.headers.common["Authorization"] = "";
          }
      },
  }
</script>