<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{lead.title}}</h1>
            </div>

            <div class="column is-12">
                <form action="" @submit.prevent="formSubmit">
                   <div class="field">
                        <label>Company</label>
                        <div class="control">
                            <input type="text" class="input" name="company" v-model="lead.company">
                        </div>
                    </div>

                    <div class="field">
                        <label>Contact Person</label>
                        <div class="control">
                            <input type="text" class="input" name="contact_person" v-model="lead.contact_person">
                        </div>
                    </div>

                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" name='email' v-model="lead.email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="text" class="input" name="phone" v-model="lead.phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>Website</label>
                        <div class="control">
                            <input type="text" class="input" name="website" v-model="lead.website">
                        </div>
                    </div>

                    <div class="field">
                        <label>Confidence</label>
                        <div class="control">
                            <input type="number" class="input" name="confidence" v-model="lead.confidence">
                        </div>
                    </div>

                    <div class="field">
                        <label>Estimated Value</label>
                        <div class="control">
                            <input type="number" class="input" name="estimated_value" v-model="lead.estimated_value">
                        </div>
                    </div>

                    <div class="field">
                        <label>Status</label>
                        <div class="control">
                            <div class="select">
                            <select name="status" v-model="lead.status">
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
                            <select name="priority" v-model="lead.priority">
                                <option value="low">Low</option>
                                <option value="medium">Medium</option>
                                <option value="high">High</option>
                            </select>
                        </div>
                        </div>
                    </div>

                      <div class="field">
                        <label>Assigned to</label>
                        <div class="control">
                            <div class="select">
                            <select name="assigned_to" v-model="lead.assigned_to">
                                <option value="" selected>Select member</option>
                                <option v-for="member in team.members" :key="member.id" :value="member.id">{{member.username}}</option>
                            </select>
                        </div>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
                        </div>
                    </div>

                </form>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
export default {
    name :'EditLead',
    data(){
        return {
            lead :{},
            team :{
                members : [],
            }
        }
    },
    mounted(){
        this.getLead()
        this.getTeam()
    },
    methods:{
        async getLead(){
            this.$store.commit('setIsLoading',true)
            const id = this.$route.params.id
            await axios
                    .get(`/api/v1/leads/${id}/`)
                    .then(response =>{
                        this.lead = response.data
                        console.log(this.lead)
                    })
                    .catch(err =>{
                        console.log(err)
                    })                
            this.$store.commit('setIsLoading',false)
        },
        async getTeam(){
            await axios
            .get('/api/v1/teams/get_my_team/')
            .then(response=>{
                this.team = response.data
                console.log("this team")
                console.log(this.team.abc)
            })
        },

        async formSubmit(){
            this.$store.commit('setIsLoading',true)
            const id = this.$route.params.id
            await axios
                    .patch(`/api/v1/leads/${id}/`,this.lead)
                    .then(response =>{
                       this.$router.push('/dashboard/leads')
                       toast({
                        message : 'Data is updated successful',
                        type : 'is-success',
                        duration :2000,
                        position : 'bottom-right',
                        dismissible : true,
                        pauseOnHover : true
                       })
                    })
                    .catch(err =>{
                        console.log(err)
                    })

            this.$store.commit('setIsLoading',false)

        }
    }
    
}
</script>