<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Detail {{lead.company}}</h1>
                <div class="buttons">
                    <router-link :to="{ name : 'EditLead',params :{ id : 5}}">Edit</router-link>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>
                    <p><strong>Status :</strong> {{lead.status}}</p>
                    <p><strong>Priority :</strong> {{lead.priority}}</p>
                    <p><strong>Confidence :</strong> {{lead.confidence}}</p>
                    <p><strong>Estimated value :</strong> {{lead.estimated_value}}</p>
                    <p><strong>Created At :</strong> {{lead.created_at}}</p>
                    <p><strong>Updated At :</strong> {{lead.updated_at}}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>
                    <p><strong>Contact Person : </strong> {{lead.contact_person}}</p>
                    <p><strong>Email :</strong> {{lead.email}}</p>
                    <p><strong>Phone :</strong> {{lead.phone}}</p>
                    <p><strong>Website :</strong> {{lead.website}}</p>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios';
export default {
    name : 'Lead',
    data(){
        return{
            lead : {}
        }
    },
    mounted(){
        this.getLead()
    },
    methods : {
        async getLead(){
            this.$store.commit('setIsLoading',true)
            const id = this.$route.params.id
            await axios
                .get(`/api/v1/leads/${id}/`)
                .then(response=>{
                    this.lead = response.data
                    console.log(this.lead)
                }
                )
                .catch(error =>{
                    console.log(error)
                })
            this.$store.commit('setIsLoading',false)
        },

    }
}
</script>