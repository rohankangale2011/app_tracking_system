import Vue from 'vue'
import Router from 'vue-router'
import Candidate from '@/components/candidate'
import Dashboard from '@/components/dashboard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/candidates',
      name: 'Candidate',
      component: Candidate
    }
  ]
})
