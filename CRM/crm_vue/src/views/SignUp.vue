<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>
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
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Reset Password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
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
import {toast} from 'bulma-toast'

export default {
    name : 'SignUp',
    data(){
        return {
            username : '',
            password1 : '',
            password2 : '',
            errors : []
        }
    },
    methods : {
        submitForm(){
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

                axios
                .post('/api/v1/users/',formData)
                .then(response => {
                    toast({
                                message: 'Account was created, please log in',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })
                    this.$router.push('/log-in')
                })
                .catch(error =>{
                   if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                            } else if (error.message) {
                                this.errors.push(error.message)
                            }
                            console.log(this.errors)
                })
            }
        }
    }
}
</script>