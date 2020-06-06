<template lang="html">

    <div class="single-question mt-2">
        <div v-if="notFound" class="container">
            <h1>Question not Found </h1>
        </div>
        <div v-else class="container">
<!-- CONTENUTO E AUTORE DELLA DOMANDA -->
             <h4>Question: {{ question.content }} </h4>
             <QuestionActions
             v-if="isOwner"
             :slug="slug"
             />
             <p class="mb-0">Question Added By:
                 <span class="author-name"> {{ question.author }} </span>
             </p>
             <p>{{ question.created_at }}</p>

<!-- CONTROLLA SE L'UTENTE HA GIA RISPOSTO ALLA DOMANDA -->
            <template v-if="userHasAnswered">
<!--                <p>Hai risposto a questa domanda</p>  -->
            </template>
<!-- MOSTRA IL FORM DELLA RISPOSTA NEL CASO CHE L'UTENTE PREMA IL TASTO "Rispondi alla Domanda" -->
            <template v-else-if="showForm">
                <form class="card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Add an answer to the question
                    </div>
                    <div class="card-block">
                        <textarea
                            v-model = "newAnswerBody"
                            class ="form-control"
                            placeholder = "Add an answer"
                            rows="5">
                        </textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button  class="btn btn-sm btn-success">
                         Add Answer </button>
                    </div>
                </form>
                <p class = "error mt-2">{{ error }}</p>
            </template>
<!-- MOSTRA IL BUTTON "Rispondi alla domanda" -->
            <div v-else>
                <button
                    class = "btn-btn-sm btn-success"
                    @click="showForm=true"
                    >answer the question
                </button>
            </div>
<!-- VISUALIZZA IL COMPONENTE ANSWER  NEL CASO CHE ABBIA RISPOSTO ALLA DOMANDA-->
              <hr>
               <AnswerComponent
                  v-for="(answer, index) in answers"
                  :answer="answer"
                  :requestUser="requestUser"
                  :key="index"
                  @delete-answer="deleteAnswer"
                  />
                 <p v-show="loadingAnswers"> loading answers: </p>
             <button
                v-show="next"
                @click="getQuestionAnswers"
                class="btn btn-sm btn-outline-success"
                >Carica Ancora
             </button>


        </div>
    </div>
</template>

<script>
import {apiService} from '../common/api.service.js';
import AnswerComponent from '../components/Answer.vue';
import QuestionActions from '../components/QuestionActions.vue';


export default {
    name: "Question",

    props: {
        slug: {
            type: String,
            required: true
        }
    },

    components: {
        AnswerComponent,
        QuestionActions,
    },

    data() {
        return {
            question: {},
            loadingAnswers:false,
            answers: [],
            userHasAnswered: false,
            showForm: false,
            newAnswerBody:null,
            error: null,
            next: null,
            requestUser:null,
            requestUrl :null,
        }
    },
    computed: {
        isOwner()  {
//            return this.question.author === this.requestUser;
        return false
        },
        notFound() {
            return this.question["detail"];
        }

    },

    methods : {
        setPageTitle(title) {
            document.title = title;
            },
        setRequestUser() {
            this.requestUser = window.localStorage.getItem("username")
            },

        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            console.log(endpoint);
            apiService(endpoint)
                .then(data => {
                    this.question = data;
                    this.userHasAnswered = data.user_has_answered;
                    this.setPageTitle(data.content);
                })

            },

        async getQuestionAnswers() {
          let endpoint = `/api/questions/${this.slug}/answers/`;

          console.log("sto caricando le risposte")
           if (this.next) {
               endpoint = this.next;
           }
           this.loadingAnswers = true;
            apiService(endpoint)
              .then(data => {
                  this.answers.push(...data.results);
                  this.loadingAnswers = false;
                  if (data.next) {
                      this.next = data.next;
                  } else {
                      this.next = null;
                  }
              })

        },

        async onSubmit() {
            if (this.newAnswerBody) {
                console.log("sto aggiungendo  una risposta")
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint, "POST", { body: this.newAnswerBody })
                console.log("ho aggiunto una risposta")
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                alert("Risposta aggiunta con successo")
                this.getQuestionAnswers();
        //        window.location.reload()


               if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "Il campo non può essere vuoto!"
            }
        },


        async deleteAnswer(answer) {
            let endpoint = `/api/answers/${answer.id}/`;
            try {
                await apiService(endpoint, "DELETE");
                // this.answers.splice(this.answers.indexOf(answer), 1);
                this.$delete(this.answers, this.answers.indexOf(answer));
                this.userHasAnswered = false;
            }
            catch (err) {
                console.log(err);
            }
        }

            },
        async created() {
            this.getQuestionAnswers();
            this.getQuestionData();
            this.setRequestUser();
            document.title = "Add Question";

        }
    }

</script>


<style lang="css" scoped>
</style>
