<template lang="html">
    <div class="single-question mt-2">
        <div class="container">
             <p>Contenuto: {{ question.content }} </p>
             <p class="mb-0">Domanda aggiunta da:
                 <span class="author-name"> {{ question.author }} </span>
             </p>
              <p>{{ question.created_at }}</p>

             <p> loading answers: </p>

             <p>Numero risposte</p>


        </div>
    </div>
</template>

<script>
import {apiService} from '../common/api.service.js';

export default {
    name: "question-answers-list",

    props: {
        pk: {
            type: Number,
            required: true
        }
    },


    data() {
        return {
            question: {},
            question_body: null,
            error: null,
            usersName:[],
            answers: [],

        }
    },
    methods : {

        getQuestionData() {
            let endpoint = "http://127.0.0.1:8000/api/questions/cosa-pensate-della-musica-jazz-fgy6i7/";
            console.log(endpoint);
            apiService(endpoint)
                .then(data => {
                    this.question = data;
            })

        },

        getUsersName() {
            let endpoint = "http://127.0.0.1:8000/api/users/";
            apiService(endpoint)
              .then(data => {
                  this.usersName.push(...data.results);
              })
        },

        getQuestionAnswersList() {

//           let endpoint = "http://127.0.0.1:8000/api/questions/6/risposte/";
           let endpoint = `/api/questions/${this.pk}/risposte/`;
            apiService(endpoint)
              .then(data => {
                  this.answers.push(...data.results);
              })
        },

            },
        created() {
            this.getUsersName();
            this.getQuestionAnswersList();
            this.getQuestionData();
            document.title = "Aggiungi domanda";

        }
    }

</script>


<style lang="css" scoped>
</style>
