<template>
    <div class="container">
            <div class="columns is-multiline">
                <div class="column is-12">
                  <h1 class="title">Add Lead</h1>
                </div>
                <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Company</label>
                        <div class="control">
                            <input type="text" class="input" name="company" v-model="company">
                        </div>
                    </div>

                    <div class="field">
                        <label>Contact Person</label>
                        <div class="control">
                            <input type="text" class="input" name="contact_person" v-model="contact_person">
                        </div>
                    </div>

                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" name='email' v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="text" class="input" name="phone" v-model="phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>Website</label>
                        <div class="control">
                            <input type="text" class="input" name="website" v-model="website">
                        </div>
                    </div>

                    <div class="field">
                        <label>Confidence</label>
                        <div class="control">
                            <input type="number" class="input" name="confidence" v-model="confidence">
                        </div>
                    </div>

                    <div class="field">
                        <label>Estimated Value</label>
                        <div class="control">
                            <input type="number" class="input" name="estimated_value" v-model="estimated_value">
                        </div>
                    </div>

                    <div class="field">
                        <label>Status</label>
                        <div class="control">
                            <div class="select">
                            <select name="status" v-model="status">
                                <option value="new">New</option>
                                <option value="contacted">Contacted</option>
                                <option value="inprogress">In Progress</option>
                                <option value="lost">Lost</option>
                                <option value="won">Won</option>
                            </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label>Priority</label>
                        <div class="control">
                            <div class="select">
                            <select name="priority" v-model="priority">
                                <option value="low">Low</option>
                                <option value="medium">Medium</option>
                                <option value="high">High</option>
                            </select>
                        </div>
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
    name : 'AddLead',
    data(){
        return {
            company : '',
            contact_person : '',
            email : '',
            phone : '',
            estimated_value: 0,
            confidence: 0,
            website: '',
            status: 'New',
            priority: 'Medium',
        }
    },
    methods:{
        async submitForm(){
            this.$store.commit('setIsLoading',true)
            const dataForm = {
                company : this.company,
                contact_person : this.contact_person,
                email : this.email,
                phone : this.phone,
                estimated_value: this.estimated_value,
                confidence: this.confidence,
                website: this.website,
                status: this.status,
                priority: this.priority
            }

            await axios
            .post("/api/v1/leads/",dataForm)
            .then(response=>{
                toast({
                    message : 'Create leads successful',
                    type :'is-success',
                    dismissible : true,
                    pauseOnHover :true,
                    duration :2000,
                    position :'bottom-right'

                })
                this.$router.push('/dashboard/leads')

            })
            .catch(error =>{
                console.log(error)
            })
            this.$store.commit('setIsLoading',false)

        }
    }
}
</script>