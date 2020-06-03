<template lang="html">
  <div class="question-actions">


    <router-link
      class="btn btn-sm btn-success mr-1"
      :to="{ name: 'question-editor', params: {slug: slug} }"
      ><span>Modifica </span>
    </router-link>

    <router-link
      :to="{ name: 'question-confirm-delete', params: {slug: slug} }"
      class="btn btn-sm btn-outline-danger"
      ><span>Elimina</span>
   </router-link>



<!-- ELIMINA IL RECORD SENZA ALCUNA CONFERMA
    <button
        class="btn btn-sm btn-outline-danger"
        @click="deleteQuestion"
        >Elimina
    </button>
    -->



  </div>
</template>

<script>
import {apiService} from '../common/api.service.js';
export default {
    name:"QuestionActions",
    props: {
        slug: {
        type: String,
        required:false
        },
    },


    methods: {
        async deleteQuestion() {
            let  endpoint = `/api/questions/${this.slug}/`;
            alert(endpoint)
            try {
                await apiService(endpoint,"DELETE");
                alert("eliminato")
                this.$router.push("/");

            }catch {
                alert("errore")
                console.log("err");
            }

        }
    }
}
</script>

<style lang="css" scoped>
</style>
