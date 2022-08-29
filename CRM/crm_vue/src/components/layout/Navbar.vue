<template>
    <nav class="navbar is-dark">
        <div class="navbar-menu">
            <div class="navbar-end">
                <router-link to="/dashboard/leads" class="navbar-item">Lead</router-link>
                <router-link to="/dashboard/team" class="navbar-item">Team</router-link>
                <router-link to="/dashboard/Clients" class="navbar-item">Client</router-link>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!this.$store.state.isAuthenticated">
                            <router-link to='/sign-up' class='button is-success'><strong>Sign up</strong></router-link>
                            <router-link to="/log-in" class="button is-light">Log in</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/my-account" class="button is-info">My Account</router-link>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    
</template>

<script>
export default {
    name : "Navbar"
}
</script>