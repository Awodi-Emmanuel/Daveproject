import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/home/HomePage'
import LoginPage from '../views/login/LoginPage'
import RegisterPage from '../views/register/RegisterPage'
import CompleteRegistrationPage from '../views/register/CompleteRegistration'
import NotFoundPage from '../views/error/404'

const routes = [

  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/complete-registration', component: CompleteRegistrationPage },
  { path: '/404', component: NotFoundPage },

  // otherwise redirect to home
  { path: '/:catchAll(.*)', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/register']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('loginSuccess')
  console.log(loggedIn)

  if (authRequired && !loggedIn) {
    return next('/login')
  }
  next()
})

export default router
