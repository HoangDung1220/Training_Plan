<template>
<div class="container">
    <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="title">Add Team</h2>
        </div>
        <div class="column is-6">
            <form action="" @submit.prevent="submitForm">
            <div class="field">
                <label>Name</label>
                <div class="control">
                    <input type="text" class="input" v-model="nameTeam">
                </div>
            </div>

            <div class="field">
                 <button class="button is-success">Submit</button>
            </div>
            </form>
        </div>
    </div>
</div>
    
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name : 'AddTeam',
    data(){
        return{
        nameTeam : '',
        errors : []
        }
    },
    methods :{
        async submitForm(){
            this.$store.commit('setIsLoading',true)
            if (!this.nameTeam.length){
                this.errors.push('Please fill in field name team')
            }

            if (!this.errors.length){
                const data ={
                    name : this.nameTeam
                }
                await axios
                        .post('/api/v1/teams/',data)
                        .then(response=>{
                            console.log(response)
                            toast({
                                message : 'Create success a team',
                                type : 'is-success',
                                dismissible : true,
                                pauseOnHover : true,
                                duration : 2000,
                                position : 'bottom-right'
                            })
                            this.$store.commit('setTeam',{'id':response.data.id,'name':response.data.name})
                            this.$router.push('/dashboard')
                            console.log(localStorage.getItem('team_name'))
                        })
                        .catch(err =>{
                            console.log(err)
                        })
            }
            this.$store.commit('setIsLoading',false)
            
        }
    }
}
</script>