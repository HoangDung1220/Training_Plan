<template>
<div class="container">
    <div class="columns is-multiline">
        <div class="column is-12">
            <div class="title">Clients</div>
            <router-link to="/dashboard/addClient">Add Clients</router-link>
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Contact person</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="client in clients" :key="client.id">
                        <td>{{client.name}}</td>
                        <td>{{client.contact_person}}</td>
                        <td><router-link :to="{name:'Client',params:{id:client.id}}">Detail</router-link></td>
                       
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
    name : 'Clients',
    data(){
        return {
            clients : []
        }
    },

    mounted(){
        this.getClients()
    },

    methods :{
        async getClients(){
            this.$store.commit('setIsLoading',true)
            await axios
                    .get('/api/v1/clients/')
                    .then(response =>{
                        this.clients = response.data
                        console.log(this.clients)
                    })
                    .catch(error =>{
                        console.log(JSON.stringify(error))
                    })
            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>