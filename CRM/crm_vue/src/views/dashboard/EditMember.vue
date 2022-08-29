<template>
    <div class="container">
            <div class="columns is-multiline">
                <div class="column is-12">
                  <h1 class="title">Edit Member</h1>
                </div>
                <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>First name</label>
                        <div class="control">
                            <input type="text" class="input" name="name" v-model="user.first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Last name</label>
                        <div class="control">
                            <input type="text" class="input" name="body" v-model="user.last_name" >
                        </div>
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
import { toast } from 'bulma-toast'

export default {
    name : 'EditMember',
    data(){
        return{
        user : {
            
        }
        }
    },
    mounted(){
        this.getUser()
    },
    methods:{
        async getUser()
        {
            const id = this.$route.params.id
            axios
            .get(`/api/v1/teams/member/${id}/`)
            .then(response =>{
                this.user = response.data
                console.log(this.user)
            })
            .catch(err=>{
                console.log(err)
            })
        },

        async submitForm()
        {
            this.$store.commit('setIsLoading',true)
            const id = this.$route.params.id
            await axios
            .put(`/api/v1/teams/member/${id}/`,this.user)
            .then(response =>{
                console.log(response)
                toast({
                    message :'Update information successful',
                    type : 'is-success',
                    dismissible :true,
                    pauseOnHover :true,
                    duration :2000,
                    position :'bottom-right'
                    
                })
                this.$router.push('/my-account/')
            })
            .catch(err =>{
                console.log(err)
            })
            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>