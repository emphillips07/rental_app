import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import EditProfileView from '../views/EditProfileView.vue'
import EditPasswordView from '../views/EditPasswordView.vue'
import RentalListView from '../views/RentalListView.vue'
import RentalDetailsView from '../views/RentalDetailsView.vue'
import StaffSignupView from '../views/StaffSignupView.vue'
import UserListView from '../views/UserListView.vue'
import StaffListView from '../views/StaffListView.vue'
import UserDetailsView from '../views/UserDetailsView.vue'
import EditUserDetailsView from '../views/EditUserDetailsView.vue'
import RentalCreateView from '../views/RentalCreateView.vue'
import EditRentalView from '../views/EditRentalView.vue'
import ReservationsView from '../views/ReservationsView.vue'
import NewReservationView from '../views/NewReservationView.vue'
import MyReservationsView from '../views/MyReservationsView.vue'
import ReservationsListView from '../views/ReservationsListView.vue'
import EditReservationView from '../views/EditReservationView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
        path: '/',
        name: 'home',
        component: HomeView
      },
      {
        path: '/signup',
        name: 'signup',
        component: SignupView
      },
      {
        path: '/login',
        name: 'login',
        component: LoginView
      },
      {
        path: '/profile/edit',
        name: 'editprofile',
        component: EditProfileView
      },
      {
        path: '/profile/edit/password',
        name: 'editpassword',
        component: EditPasswordView
      },
      {
        path: '/profile/:id',
        name: 'profile',
        component: ProfileView
      },
      {
        path: '/rentals',
        name: 'rentals',
        component: RentalListView
      },
      {
        path: '/rentals/:id',
        name: 'rentaldetails',
        component: RentalDetailsView
      },
      {
        path: '/staffsignup',
        name: 'staffsignup',
        component: StaffSignupView
      },
      {
        path: '/userlist',
        name: 'userlist',
        component: UserListView
      },
      {
        path: '/stafflist',
        name: 'stafflist',
        component: StaffListView
      },
      {
        path: '/userlist/:id',
        name: 'userdetails',
        component: UserDetailsView
      },
      {
        path: '/userlist/:id/edit',
        name: 'edituserdetails',
        component: EditUserDetailsView
      },
      {
        path: '/create',
        name: 'create_rental',
        component: RentalCreateView
      },
      {
        path: '/:id/edit',
        name: 'rental_edit',
        component: EditRentalView
      },
      {
        path: '/reservations/inhouse',
        name: 'inhouse',
        component: ReservationsView
      },
      {
        path: '/reservations/create',
        name: 'reservation_create',
        component: NewReservationView
      },
      {
        path: '/reservations/',
        name: 'reservations',
        component: MyReservationsView
      },
      {
        path: '/reservations/list',
        name: 'reservations_all',
        component: ReservationsListView
      },
      {
        path: '/reservations/:id/edit',
        name: 'reservations_edit',
        component: EditReservationView
      },
  ]
})

export default router
