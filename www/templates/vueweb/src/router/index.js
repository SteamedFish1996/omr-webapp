import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import upload from '@/components/upload'
import ana from '@/components/ana'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/upload',
      name: 'upload',
      component: upload
    },
    {
      path: '/ana',
      name: 'ana',
      component: ana
    },
  ]
})
