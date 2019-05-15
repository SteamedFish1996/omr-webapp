import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import upload from '@/components/upload'
import ana from '@/components/ana'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
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
