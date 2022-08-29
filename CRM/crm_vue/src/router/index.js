import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/LogIn.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import Leads from '../views/dashboard/Leads'
import AddLead from '../views/dashboard/AddLead'
import Lead from '../views/dashboard/Lead'
import EditLead from '../views/dashboard/EditLead.vue'
import AddTeam from '../views/dashboard/AddTeam'
import AddMember from '../views/dashboard/AddMember'
import AddClient from '../views/dashboard/AddClient'
import Clients from '../views/dashboard/Clients'
import Team from '../views/dashboard/Team'
import Client from '../views/dashboard/Client'
import EditClient from '../views/dashboard/EditClient'
import AddNote from '../views/dashboard/AddNote'
import EditMember from '../views/dashboard/EditMember'
import Plans from '../views/dashboard/Plans'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path : '/log-in',
    name :' LogIn',
    component : Login
  },
  {
    path :'/my-account',
    name : 'MyAccount',
    component :MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard',
    name : 'Dashboard',
    component : Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/leads',
    name : 'Leads',
    component : Leads,
    meta: {
      requireLogin: true
    }
  },
  {
    path : '/dashboard/leads/:id',
    name :'Lead',
    component : Lead,
    meta : {
      requireLogin :true
    }
  },
  {
    path :'/dashboard/editLead/:id',
    name : 'EditLead',
    component : EditLead,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/addlead',
    name : 'AddLead',
    component : AddLead,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/addTeam',
    name : 'AddTeam',
    component : AddTeam,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/addMember',
    name : 'AddMember',
    component : AddMember,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/team',
    name : 'Team',
    component : Team,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/addClient',
    name : 'AddClient',
    component : AddClient,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/Clients',
    name : 'Clients',
    component : Clients,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/Clients/:id',
    name : 'Client',
    component : Client,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/EditClients/:id',
    name : 'EditClient',
    component : EditClient,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/addNote',
    name : 'AddNote',
    component : AddNote,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/editmember/:id',
    name : 'EditMember',
    component : EditMember,
    meta: {
      requireLogin: true
    }
  },
  {
    path :'/dashboard/plans',
    name : 'Plans',
    component : Plans,
    meta: {
      requireLogin: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }

})

export default router
