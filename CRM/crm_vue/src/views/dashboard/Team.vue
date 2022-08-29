<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Team {{team.name}}</h1>
            </div>
            <div class="column is-12">
                <h2 class="subtitle">Member</h2>
                <template v-if = "team.created_by.id === parseInt(this.$store.state.user.id)">
                    <router-link :to="{'name' :'AddMember'}" class="button is-primary">AddMember</router-link>
                </template>
                
                <table class="table is-fullwith">
                    <thead>
                        <th>Username</th>
                        <th>Fullname</th>
                    </thead>
                    <tbody>
                        <tr v-for="member in team.members" :key ='member'>
                            <td>{{member.username}}</td>
                            <td>{{member.first_name}} {{member.last_name}}</td>
                        </tr>
                    </tbody>

                </table>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name : 'Team',
    data(){
        return {
            team : {
                members : [],
                created_by : {}
            }
        }
    },
    mounted(){
        this.getTeam()
    },
    methods :{
        async getTeam(){
            this.$store.commit('setIsLoading',true)
            await axios 
                .get('/api/v1/teams/get_my_team/')
                .then(response =>{
                    this.team = response.data
                    console.log(this.team)
                     console.log(this.$store.state.user.id)
                })
                .catch(err=>{
                    console.log(this.err)
                })
            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>