<template>
  <nav class="bg-blue-300">
    <div class="container mx-auto flex items-center justify-between">
      <div class="flex items-center justify-center">
        <img :src="'../src/assets/palm logo.png'" class="h-16 w-16"/>
        <RouterLink to="/" class="text-white text-3xl font-bold px-4 hover:text-orange-300">Best Beach Rentals</RouterLink>
      </div>
      
      <div class="menu-right relative z-50">
      <template v-if="userStore.user.isAuthenticated && userStore.user.id">
              
                <button @mouseenter="openDropdown" @mouseleave="closeDropdown" class="bg-orange-300 hover:bg-orange-500 text-white font-bold py-2 px-4 rounded inline-flex items-center">
                  <span>{{ userStore.user.name }}</span>
                <svg class="w-4 h-4 ml-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 12l-7-7 1.5-1.5L10 9l5.5-5.5L17 5z" clip-rule="evenodd"></path></svg>
                </button>
                
                <div v-if="isOpen" @mouseenter="openDropdown" @mouseleave="closeDropdown" class="origin-top-right absolute right-0 w-56 rounded-md shadow-lg bg-white">
                  <div class="" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
                    <div v-if="userStore.user.level > 2" class="bg-white p-1">
                      <RouterLink to="/profile/edit" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">Edit Profile</RouterLink>
                    </div>
                    <div v-if="userStore.user.level > 2" class="bg-white p-1">
                      <RouterLink to="/reservations/" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">My Reservations</RouterLink>
                    </div>
                    <div v-if="userStore.user.level < 3" class="bg-white p-1">
                      <RouterLink to="/reservations/inhouse" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">In House</RouterLink>
                    </div>
                    <div v-if="userStore.user.level < 3" class="bg-white p-1">
                      <RouterLink to="/reservations/list" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">View Reservations</RouterLink>
                    </div>
                    <div v-if="userStore.user.level < 2" class="bg-white p-1">
                      <RouterLink to="/create" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">Create Rental</RouterLink>
                    </div>
                    <div v-if="userStore.user.level < 2" class="bg-white p-1">
                      <RouterLink to="/staffsignup" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">Employee Signup</RouterLink>
                    </div>
                    <div v-if="userStore.user.level < 3" class="bg-white p-1">
                      <RouterLink to="/userlist" class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900" role="menuitem">User List</RouterLink>
                    </div>
                    <div class="bg-white p-1">
                      <div class="block p-2 rounded-md bg-orange-300 text-sm hover:bg-blue-300 hover:text-gray-900"><button @click="logout">Log Out</button></div>
                    </div>
                  </div>
                </div>   
    </template>                
               

    
      
        
                  

                  <template v-else>
                      <RouterLink to="/login" class="mr-4 py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Log In</RouterLink>
                      <RouterLink to="/signup" class="py-4 px-6 bg-orange-300 text-white font-bold rounded-lg">Sign Up</RouterLink>
                  </template>
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
  import logo from '../src/assets/palm logo.png';

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

      data() {
        return {
          isOpen: false
        };
      },

      methods: {
        openDropdown() {
      this.isOpen = true;
    },
    closeDropdown() {
      this.isOpen = false;
    },

        logout() {
            console.log('Log out')

            this.isOpen = !this.isOpen

            this.userStore.removeToken()

            this.$router.push('/login')
        },
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