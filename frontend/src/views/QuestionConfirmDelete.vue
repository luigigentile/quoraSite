<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h3 class = "mb-3">Are you sure you want to delete the following question</h3>

                <form @submit.prevent="onSubmit" >

                    <h3
                        class = "form-control"
                        rows="3" cols="80">
                        {{questionBody}}
                    </h3>
                    <br>
                    <button
                       class ="btn btn-outline-success"
                        type="submit"
                        >yes,I'm sure
                    </button>
                    <button
                    @click="tornaIndietro"
                    class="btn btn-outline-info ml-3">"No, take me back"
                    </button>

                </form>
            </div>
        </div>
    </div>
</template>

<script>

import { apiService } from "../common/api.service";
export default {
    name: "QuestionConfirmDelete",
    props: {
        slug: {
        type: String,
        required:false
        },
        previousQuestion: {
        type: String,
        required:false
        },
    },

    data() {
        return {
            questionBody: this.previousQuestion  || null,
            error: null,
            usersName:[],

        }
    },

    async beforeRouteEnter(to,from,next) {
        if(to.params.slug !== undefined) {
            let endpoint = `/api/questions/${to.params.slug}/`;
            await apiService(endpoint)
                    .then(data => {
                        to.params.previousQuestion = data.content;
                    })
            }
            return next();
    },
    methods : {
        tornaIndietro() {
            this.$router.push({
                name: "home",

            })
//  window.history.back()
         },

         async onSubmit() {
             let  endpoint = `/api/questions/${this.slug}/`;
             try {
                 await apiService(endpoint,"DELETE");
                 this.$router.push("/");

             }catch {
             console.log("err");
             }

         },

        },
        created() {
            document.title = "Delete Question";
        }
    }

</script>

<style lang="css" scoped>
</style>
