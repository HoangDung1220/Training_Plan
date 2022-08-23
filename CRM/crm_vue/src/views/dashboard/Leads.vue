<template>
<div class="container">
    <div class="columns is-multiline">
        <div class="column is-12">
            <div class="title">Leads</div>
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Company</th>
                        <th>Contact person</th>
                        <th>Status</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="lead in leads" :key="lead.id">
                        <td>{{lead.company}}</td>
                        <td>{{lead.contact_person}}</td>
                        <td>{{lead.status}}</td>
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
    name : 'Leads',
    data(){
        return {
            leads : []
        }
    },

    mounted(){
        this.getLeads()
    },

    methods :{
        async getLeads(){
            this.$store.commit('setIsLoading',true)
            await axios
                    .get('/api/v1/leads',{mode: 'no-cors'})
                    .then(response =>{
                        this.leads = response.data
                        console.log(this.leads)
                    })
                    .catch(error =>{
                        console.log(JSON.stringify(error))
                    })
            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>