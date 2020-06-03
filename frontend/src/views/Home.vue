<template>

<div class="home-view">
    <div class="container mt-1">
<!-- FILTRO SULL'UTENTE CHE HA AGGIUNTO LA DOMANDA -->
              <div class="container  pb-2">
                <form class="form-inline" @submit.prevent="clearFilter" >
                  <div class="row form-group mb-2 ">
                      <h4 class="row form-group mb-2 " >Seleziona Utente </h4>
                      <span class="form-group  ml-4">
                        <select id = "SelectUser" class="form-group mb-2"
                           v-model='selectedUser'
                           @change="getSelectedUserQuestion">
                           <option> All </option>
                          <option
                               v-for="user in usersName"
                              :key="user.pk"
                                > {{ user.username }} </option>
                          </select>
                          </span>
                    </div>
                </form>
                 </div>
<!-- AGGIUNGE LE DOMANDE POSTE DALL'UTENTE USER -->
            <div v-for="question in questionsFiltered"
                 :key="question.pk" >
                 <div class="card  border-primary rounded mb-1">
                     <div class="card-header">
                     <p class="mb-0">Domanda aggiunta da :
                         <span
                         class="author-name">{{ question.author }}</span>
                          </p>
                    </div>
                    <div class="card-body mt-n3">
                        <router-link
                        :to="{ name: 'question', params: { slug: question.slug } }"
                        class="question-link">
                        {{ question.content }}
                        </router-link>
                        <router-link
                            :to="{ name: 'question-answers-list', params: { pk: question.id } }"
                            class="question-answers-list">
                            id = {{ question.id }}
                        </router-link>
                         <p class="mb-n1"> <strong>Risposte: {{ question.answers_count }}</strong></p>
                    </div>
                 </div>
            </div>
<!-- FINE AGGIUNGE LE DOMANDE POSTE DALL'UTENTE USER -->


<!-- PULSANTE CARICA ANCORA
             v-show="next"
 -->
        <div class="my-2">
          <p v-show="loadingQuestions">...loading...</p>
          <button
            v-show="next"
             @click="getQuestions"
             class="btn btn-sm btn-outline-success"
             >Carica Ancora
          </button>
        </div>
    </div>
</div>
</template>

<script>
import {apiService} from '../common/api.service.js';
export default {
    name: "Home",
    data()  {
        return {
            firstTime: true,
            questions: [],
            questionsFiltered: [],
            usersName: [],
            next : null,
            loadingQuestions: false,
            userName : null,
            selectedUser: null,
        }

    },

    methods: {
         getTypeOf(obj) {
             return {}.toString.call(obj).split(' ')[1].slice(0, -1).toLowerCase();
         },
        clearFilter() {
            this.questionsFiltered = this.questions;
        },
        filterQuestions() {
            if (document.getElementById('SelectUser').selectedIndex ===0) {
                this.questionsFiltered = this.questions;
                return
            }
            let i =0;
            this.questionsFiltered= [];
             for (i=0 ; i<this.questions.length ;  i++) {
                 if(this.questions[i].author == this.selectedUser) {
                     this.questionsFiltered.push(this.questions[i]);
                 }
            }
    //        alert(this.questions[1]);
        },

        getSelectedUserQuestion() {
            this.getUsersName();
            this.filterQuestions();
            this.setFirstTimeFalse()
        },

        setFirstTimeFalse() {
            this.firstTime = false
        },

        getUsersName() {
            let endpoint = "api/users/";
            this.usersName = [];
            apiService(endpoint)
              .then(data => {
                  this.usersName.push(...data.results);
              })
        },

        getUserName() {
            let endpoint = "api/user/";
            apiService(endpoint)
              .then(data => {
                 this.userName = data.username;
              })
        },

        getQuestions() {
            let endpoint = "api/questions/";
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingQuestions = true;
            apiService(endpoint)
              .then(data => {
                      this.questions.push(...data.results);
                      this.questionsFiltered = this.questions;
              this.loadingQuestions = false;
                  if (data.next) {
                      this.next = data.next;
                  } else {
                      this.next = null;
                  }
              })
        }
    },
    created() {
        this.getQuestions();
        this.getUsersName();
//        this.getQuestionAnswers();
        document.title = "QuestionTime";
    }

};
</script>

<style media="screen">
    .author-name {
        font-weight: bold;
        color: #DC3545;
    }
    .question-link {
        font-weight: bold;
        color: black;
    }
    .question-link:hover {
        color: #343A40;
        text-decoration: none;
    }
</style>
