<template>
<div class="container">
  <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form action="" @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{error}}</p>
                    </div>

                     <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>

                </form>

            </div>
        </div>
    </div>
    
    
</template>

<script>
import axios from 'axios'
export default {
    name  : 'LogIn',
    data() {
        return{
            username : '',
            password : '',
            errors : []
        }
    },
    methods:{
        async submitForm(){
            this.$store.commit('setIsLoading', true)
            console.log(this.$store.state.isLoading)
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')

            if (!this.username.length){
                this.errors.push("Username must fill in")
            }
            if (!this.password.length){
                this.errors.push("Password must fill in")
            }

            if (!this.errors.length){
                const dataForm ={
                    username : this.username,
                    password : this.password
                    }
                
            await axios
                .post('/api/v1/token/login',dataForm)
                .then(response=>{
                    const token = response.data.auth_token
                    this.$store.commit('setToken',token)
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token
                    localStorage.setItem('token',token)
                })
                .catch(error =>{
                      if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                })
                this.$store.commit('setIsLoading', false)

            await axios
                .get('/api/v1/users/me/')
                .then(response=>{
                    this.$store.commit('setUser',{'id' :response.data.id, 'username' : response.data.username})
                    localStorage.setItem('userid',response.data.id)
                    localStorage.setItem('username',response.data.username)  
                 
                })
                .catch(err=>{
                    console.log(err)
                })

            await axios
                .get('/api/v1/teams/get_my_team/')
                .then(response=>{
                    console.log("get my team")
                    console.log(response)
                        this.$store.commit('setTeam', {
                            'id': response.data.id, 
                            'name': response.data.name,
                            'plan' :response.data.plan.name,
                            'max_leads' : response.data.plan.max_leads,
                            'max_clients': response.data.plan.max_clients
                        })
                    this.$router.push('/my-account')
                })
                .catch(err =>{
                    console.log(JSON.stringify(err))
                })
                
                

            }
        }
    }
}
</script>