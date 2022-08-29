<template>
<div class="container">
    <div class="columns is-multiline">
        <div class="column is-12">
            <div class="title">Leads</div>
            <p><strong>Plan: </strong>{{this.$store.state.team.plan}}</p>
            <p><strong>Max_Leads: </strong>{{this.$store.state.team.max_leads}}</p>
            <p><strong>Max_Clients: </strong>{{this.$store.state.team.max_clients}}</p>
            <div class="buttons">
                <router-link to="/dashboard/addlead" v-if="this.$store.state.team.max_leads > numLeads" class="button is-light">Add Lead</router-link>
                <router-link to="/dashboard/plans" class="button is-light">Change Plan</router-link>
            </div>
           
         

            <form action="" @submit.prevent="getLeads">
                <div class="field has-addons">
                    <div class="control">
                        <input type="text" class="input" v-model="query">
                    </div>

                    <div class="control">
                        <button class="button is-success">Search</button>
                    </div>
                </div>
            </form>
            
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Company</th>
                        <th>Contact person</th>
                        <th>Assigned To</th>
                        <th>Status</th>
                        <th>Action</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="lead in leads" :key="lead.id">
                        <td>{{lead.company}}</td>
                        <td>{{lead.contact_person}}</td>
                        <td>{{lead.assigned_to}}</td>
                        <td>{{lead.status}}</td>
                        <th><router-link :to="{name : 'Lead',params :{id : lead.id}}">Detail</router-link></th>
                    </tr>
                </tbody>
            </table>

            <div class="buttons">
                <div class="button is-light" v-if="buttonPrevious" @click="GoToPrevious">Previous</div>
                <div class="button is-light" v-if="buttonNext" @click="GoToNext">Next</div>
            </div>
        </div>
    </div>

</div>
    
</template>

<script>
import axios from 'axios'
export default {
    name : 'Leads',
    data(){
        return {
            leads : [],
            buttonNext : false,
            buttonPrevious : false,
            curentpage :1,
            query : '',
            numLeads :0
        }
    },

    mounted(){
        this.getLeads()
    },

    methods :{
        GoToPrevious(){
            this.curentpage = this.curentpage -1
            this.getLeads()
        },

        GoToNext(){
            this.curentpage = this.curentpage +1
            this.getLeads()
        },

        async getLeads(){
            this.$store.commit('setIsLoading',true)
            this.buttonNext = false
            this.buttonPrevious = false
           
            await axios
                    .get(`/api/v1/leads/?page=${this.curentpage}&search=${this.query}`)
                    .then(response =>{
                        this.leads = response.data.results
                        this.numLeads = response.data.count
                        console.log("numlog")
                        console.log(this.numLeads)
                        console.log(this.$store.state.team)
                        if (response.data.next){
                            this.buttonNext = true
                        }

                        if (response.data.previous){
                            this.buttonPrevious = true
                        }
                    })
                    .catch(error =>{
                        console.log("error")
                        console.log(JSON.stringify(error))
                    })
            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>