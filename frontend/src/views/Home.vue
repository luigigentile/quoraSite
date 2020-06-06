<template>

<div class="home-view">
    <div class="container mt-1">
<!-- FILTRO SULL'UTENTE CHE HA AGGIUNTO LA DOMANDA -->
              <div class="container  pb-2">
                <form class="form-inline" @submit.prevent="clearFilter" >
                  <div class="row form-group mb-2 ">
                      <h4 class="row form-group mb-2 " >Select Question Author</h4>
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
                     <p class="mb-0">Question added by:
                         <span
                         class="author-name">{{ question.author }}</span>
                          </p>
                    </div>


                    <div class="card-body mt-n3">
        <!-- ICONA MODIFICA -->
        <span   v-if="isOwner(question.author)">
                    <router-link title ="update question"
                          :to="{ name: 'question-editor', params: {slug: question.slug} }"
                          ><span>
                              <svg width="13" height="13" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                <path fill="#efb80b" d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z"/>
                              </svg>
                          </span>
                    </router-link>
    <!-- ICONA  ELIMINA -->
                    <router-link
                          :to="{ name: 'question-confirm-delete', params: {slug: question.slug} }"
                          ><span>
                              <svg width="14" height="14" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                <path fill="#dd4646" d="M1490 1322q0 40-28 68l-136 136q-28 28-68 28t-68-28l-294-294-294 294q-28 28-68 28t-68-28l-136-136q-28-28-28-68t28-68l294-294-294-294q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 294 294-294q28-28 68-28t68 28l136 136q28 28 28 68t-28 68l-294 294 294 294q28 28 28 68z"/>
                            </svg>
                            </span>
                    </router-link>

<!--
                    <span  @click="setIdQuestionToDelete(question.id)"  title ="display confirm delete">
                        <svg width="14" height="14" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                          <path fill="#dd4646" d="M1490 1322q0 40-28 68l-136 136q-28 28-68 28t-68-28l-294-294-294 294q-28 28-68 28t-68-28l-136-136q-28-28-28-68t28-68l294-294-294-294q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 294 294-294q28-28 68-28t68 28l136 136q28 28 28 68t-28 68l-294 294 294 294q28 28 28 68z"/>
                      </svg>
                  </span>


                    <ConfirmDeleteQuestion v-if="IsQuestionToDelete(question.id)"
                       :question="question"
                       @confirm-delete="confirmDeleteQuestion"
                      />
-->
      </span>
<!-- CONTENUTO  -->

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
                         <p class="mb-n1"> <strong>Answers: {{ question.answers_count }}</strong></p>


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
import ConfirmDeleteQuestion from '../components/ConfirmDelete.vue';

export default {
    name: "Home",

    components: {
        ConfirmDeleteQuestion,
    },
    data()  {
        return {
            firstTime: true,
            questions: [],
            questionsFiltered: [],
            usersName: [],
            next : null,
            loadingQuestions: false,
            userName : null,
            requestUser:null,
            selectedUser: null,
            displayConfirmDeleteQuestion: false,
            IdQuestionToDelete: null,
        }
    },

    methods: {
        confirmDeleteQuestion(slug) {
            if (slug) {
                let  endpoint = `/api/questions/${slug}/`;
                try {
                    apiService(endpoint,"DELETE");
                    alert("Question deleted successful")
                    this.IdQuestionToDelete = null;
                    this.question = []
                    window.location.reload()
                }catch {
                alert("Errores")
                console.log("errore");
                }
            } else {
                this.IdQuestionToDelete = null;
            }

        },
        setIdQuestionToDelete(idQuestion) {
            this.IdQuestionToDelete = idQuestion;
        },

        IsQuestionToDelete(idQuestion) {
            return this.IdQuestionToDelete === idQuestion
        },

        setDisplayConfirmDeleteQuestion() {
            this.displayConfirmDeleteQuestion = true
            },

        setRequestUser() {
            this.requestUser = window.localStorage.getItem("username")
            },

        isOwner(questionAuthor)  {
                return questionAuthor === this.requestUser
        },

        getImgUrl(pet) {
            var images = require.context('../assets/', false, /\.png$/)
            alert(images('./' + pet + ".png"))
        return images('./' + pet + ".png")
  },


         getTypeOf(obj) {
             return {}.toString.call(obj).split(' ')[1].slice(0, -1).toLowerCase();
         },
        clearFilter() {
            alert("clear")
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
    //        alert(window.localStorage.getItem("authorSelected"));
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
        this.setRequestUser();
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
