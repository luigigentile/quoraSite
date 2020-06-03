<template>
  <div id="app">
      <NavbarComponent />
      <router-view />
  </div>
</template>



<script>
    import {apiService} from './common/api.service.js';
    import NavbarComponent from './components/Navbar.vue'
    import modal from './components/modal.vue'
    export default {
        name:'App',
        components: {
            NavbarComponent
        },

        data()  {
            return {
                userUserName:null,
            }
        },

        methods : {
            async setUserinfo() {
                apiService("/api/user/")
                    .then(result => {
                        this.userUserName = result.username;
                        window.localStorage.setItem("username",this.userUserName)
                    })
                }
        },



        created() {
            this.setUserinfo();
        }
    }

</script>



<style>
body {
    height: 150%;
    font-family: "Playfair Display",serif;
}
.btn:focus {
    box-shadow: none !important;
}

</style>
