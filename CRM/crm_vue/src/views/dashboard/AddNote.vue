<template>
    <div class="container">
            <div class="columns is-multiline">
                <div class="column is-12">
                  <h1 class="title">Add Note</h1>
                </div>
                <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input type="text" class="input" name="name" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Body</label>
                        <div class="control">
                            <textarea type="text" class="textarea" name="body" v-model="body"></textarea>
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
