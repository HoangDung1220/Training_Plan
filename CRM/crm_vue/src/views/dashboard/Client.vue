<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{client.name}}</h1>
              
                    <router-link :to="{name:'EditClient',params:{id:1}}" class="button is-info">Update Client</router-link>

           
            </div>
                <div class="column is-6">
                    <div class="box">
                        <h2 class="subtitle">Details</h2>
                          <p><strong>Created at: </strong>{{client.created_at}}</p>
                          <p><strong>Modified at: </strong>{{client.updated_at}}</p>
                    </div>
                </div>

                <div class="column is-6">
                    <div class="box">
                        <h2 class="subtitle">Contact information</h2>
                        <p><strong>Contact person: </strong>{{client.contact_person}}</p>
                        <p><strong>Email: </strong>{{client.email}}</p>
                        <p><strong>Phone: </strong>{{client.phone}}</p>
                        <p><strong>Website: </strong>{{client.website}}</p>
                    </div>
                </div>
            </div>
            <div class="column is-12">
                <router-link to="/dashboard/addNote">Add Note</router-link>
            </div>
        </div>
   
</template>

<script>
import axios from 'axios'
export default {
    name : 'Client',
    data(){
        return{
            client : {}
        }
    },
    mounted(){
        this.getClient()
    },
    methods:{
        getClient(){
            const id = this.$route.params.id
            axios 
            .get(`/api/v1/clients/${id}/`)
            .then(response=>{
                this.client = response.data
            })
            .catch(err =>{
                console.log(err)
            })
        }

    }
}
</script>