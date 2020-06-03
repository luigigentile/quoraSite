import Vue from "vue";
import Router from "vue-router";
import AnswerEditor from "./views/AnswerEditor.vue";
import Home from "./views/Home.vue";
import Question from "./views/Question.vue";
import QuestionEditor from "./views/QuestionEditor.vue";
import QuestionAnswersList from "./views/QuestionAnswersList.vue";
import AnswerConfirmDelete from "./views/AnswerConfirmDelete.vue";
import QuestionConfirmDelete from "./views/QuestionConfirmDelete.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/question/:slug",
      name: "question",
      component: Question,
      props: true
    },

    {
      path: "/questions/:pk/risposte",
      name: "question-answers-list",
      component: QuestionAnswersList,
      props: true
    },


    {
      path: "/ask/:slug?",
      name: "question-editor",
      component: QuestionEditor,
      props: true
    },
    {
      path: "/answer/:id",
      name: "answer-editor",
      component: AnswerEditor,
      props: true
    },

    {
      path: "/answer/:id",
      name: "answer-confirm-delete",
      component: AnswerConfirmDelete,
      props: true
    },

    {
      path: "/ask/:slug?",
      name: "question-confirm-delete",
      component: QuestionConfirmDelete,
      props: true
    },
    {
      path: "*",
      name: "not-found",
      component: NotFound,
     },
   ]
});
