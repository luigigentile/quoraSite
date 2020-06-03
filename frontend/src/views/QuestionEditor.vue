<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class = "mb-3">Aggiungi una  domanda </h1>

                <form @submit.prevent="onSubmit" >
                    <textarea
                    v-model= "questionBody"
                    class = "form-control"
                    placeholder = "Cosa vuoi chiedere?"
                    rows="3" cols="80">
                    </textarea>
                    <br>
                    <button
                    class = 'btn btn-success'
                    type="submit"
                    > Pubblica domanda
                    </button>

                    <button
                    @click="tornaIndietro"
                    class="btn btn-sm btn-primary ml-3">
                    Torna Indietro
                    </button>


                </form>
                <p class = 'muted error mt-2'> {{ error }}</p>


                <p class='muted error mt-2'></p>
            </div>

        </div>

    </div>

</template>

<script>




import { apiService } from "../common/api.service";
export default {
    name: "QuestionEditor",
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
                name: "home"
            })
//                   window.history.back()
         },

        onSubmit() {
            if (!this.questionBody) {
                this.error = "Il campo non puo essere vuoto"
            } else if (this.questionBody.length > 240) {
                    this.error = "il campo non puo superare i 240 caratteri"
            } else {
                let endpoint = "/api/questions/";
                let method = 'POST';
                if (this.previousQuestion) {
                    method = 'PUT';
                    endpoint += `${this.slug}/`;
                }
                apiService(endpoint,method,{ content:this.questionBody })
                    .then(question_data => {
                        this.$router.push({
                            name:'question',
                            params: { slug: question_data.slug }

                        })
                    })
            };


            }
        },
        created() {
            document.title = "Aggiungi domanda";
        }
    }

</script>

<style lang="css" scoped>
</style>
