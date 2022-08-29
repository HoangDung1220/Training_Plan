<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add member</h1>
                <div class="column is-6">
                    <form action="" @submit.prevent="submitForm">

                        <div class="field">
                            <label>Email</label>
                            <div class="control">
                                <input type="email" class="input" name="username" v-model="username">
                            </div>
                        </div>

                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input type="password" class="input" name="password1" v-model="password1">
                            </div>
                        </div>

                        <div class="field">
                            <label>Repeat Password</label>
                            <div class="control">
                                <input type="password" class="input" name="password2" v-model="password2">
                            </div>
                        </div>

                        <div class="field">
                            <button class="button is-success">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name : 'AddMember',
    data(){
        return {
            username : '',
            password1 : '',
            password2 : '',
            errors : []
        }
    },
    methods:{
        async submitForm(){
              if (!this.username.length){
                this.errors.push("Please fill field 's username")
            }
            if (!this.password1.length){
                this.errors.push("Please fill field 's password")
            }
            if (this.password1!=this.password2){
                this.errors.push("Password1 isn't match repeat password")
            }

            if (!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password1
                }

                await axios
                .post('/api/v1/users/',formData)
                .then(response =>{
                    toast({
                        message : 'Account is created successfully',
                        type :'is-success',
                        dismissible : true,
                        pauseOnHover :true,
                        duration : 2000,
                        position :'bottom-right'

                    })
                    axios
                        .post('/api/v1/teams/add_member/',{'email':this.username})
                        .then(response=>{
                            console.log(response)
                            this.$router.push('/dashboard/team')
                        })
                        .catch(err=>{
                            console.log(err)
                        })
                        })
                .catch(err =>{
                    console.log(err)
                })

                

            }

        }
    }

}
</script>