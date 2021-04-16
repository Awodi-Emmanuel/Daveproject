import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import store from '../store'
import Register from '../views/onboarding/Register'
import Login from '../views/Auth/Login'
import Posts from '../views/About'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { guest: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { guest: true }
  },
  {
    path: '/posts',
    name: 'Posts',
    component: Posts,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  mode: 'history',
  history: createWebHistory(),
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next('/posts')
      return
    }
    next()
  } else {
    next()
  }
})

export default router
