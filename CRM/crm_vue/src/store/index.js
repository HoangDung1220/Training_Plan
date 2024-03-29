import { createStore } from 'vuex'

export default createStore({
  state: {
    token : '',
    isAuthenticated : false,
    isLoading : false,
    user : {
      username : '',
      id : 0
    },
    team : {
      id : 0,
      name :'',
      plan :'',
      max_leads : 0,
      max_clients : 0
    }

  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.id = localStorage.getItem('userid')
        state.user.username = localStorage.getItem('username')
        state.team.id = localStorage.getItem('teamid')
        state.team.name=localStorage.getItem('team_name')
        state.team.plan = localStorage.getItem('plan')
        state.team.max_leads = localStorage.getItem('max_leads')
        state.team.max_clients = localStorage.getItem('max_clients')

      } else{
        state.token = '',
        state.isAuthenticated = false
        state.user.id =0
        state.user.username=''
        state.team.id=0
        state.team.name=''
        state.team.plan = ''
        state.team.max_clients=0
        state.team.max_leads=0
      }
    },

    setIsLoading(state,status){
      state.isLoading = status
    },

    setToken(state,token){
      state.token = token
      state.isAuthenticated = true
    },

    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },

    setUser(state,user){
      state.user = user
    },

    setTeam(state,team){
      state.team = team
      localStorage.setItem('teamid',team.id)
      localStorage.setItem('team_name',team.name)
      localStorage.setItem('plan',team.plan)
      localStorage.setItem('max_leads',team.max_leads)
      localStorage.setItem('max_clients',team.max_clients)
    }


  },
  actions: {
  },
  modules: {
  }
})
