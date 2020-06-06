
<template lang="html">
    <div class="Single answer">

        <p class="text-muted">

        <strong> The author {{ answer.author }}</strong> answered at   {{ answer.created_at }}
        </p>
        <p>
        <span v-if="isAnswerAuthor">
            <router-link
                :to="{ name: 'answer-editor', params: {id:answer.id} }"
                ><span>
                    <svg width="13" height="13" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                      <path fill="#efb80b" d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z"/>
                    </svg>
                </span>
            </router-link>

        <router-link
                    :to="{ name: 'answer-confirm-delete', params: {id:answer.id} }"
                    ><span>
                        <svg width="14" height="14" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                          <path fill="#dd4646" d="M1490 1322q0 40-28 68l-136 136q-28 28-68 28t-68-28l-294-294-294 294q-28 28-68 28t-68-28l-136-136q-28-28-28-68t28-68l294-294-294-294q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 294 294-294q28-28 68-28t68 28l136 136q28 28 28 68t-28 68l-294 294 294 294q28 28 28 68z"/>
                      </svg>
                      </span>
        </router-link>
     </span>
     {{ answer.body }} </p>



<!-- ELIMINA IL RECORD SENZA ALCUNA CONFERMA
            <a
            v-bind:href="answerUrlToDelete"
            class="btn btn-sm btn-outline-danger ml-4"
            >Elimina
            </a>




        <div v-lse class="like-answer">
            <button
            @click="toogleLike"
            class = "btn btn-sm"
            :class= "{
                'btn-danger': userLikedAnswer,
                'btn-outline-danger': !userLikedAnswer
                }">

                <span>Mi piace</span>
            </button>

        </div>
-->

    </div>


</template>

<script>


export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type:Object,
            required:true
        },
        requestUser: {
            type: String,
            required:true
        },
    },


    data() {
        return {
            userLikedAnswer : this.answer.user_has_voted,
            likesNumber: this.answer.likes_count,
            answerUrlToDelete: null,
            }
        },

        computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
            },
        },

    methods: {
//        toogleLike() {
//           this.userLikedAnswer === false
//                ? this.likeAnswer()
//                : this.unLikeAnswer()
//        },
//        likeAnswer() {
//            this.userLikedAnswer = true;
//            this.likesNumber += 1
//            let endpoint = `/questions/answer/${this.answer.id}/like/`;
//            apiService(endpoint,"POST");
//        },
//        unLikeAnswer() {
//            this.userLikedAnswer = false;
//            this.likesNumber -= 1
//            let endpoint = `/questions/answer/${this.answer.id}/like/`;
//            apiService(endpoint,"DELETE");
//        },
//


        getUrl() {
            let endpoint = `/questions/answer/${this.answer.id}/delete/`;
            this.answerUrlToDelete=endpoint;
        },


        triggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer);
        },

    },

    created() {
        this.getUrl();
    }


}

</script>


<style lang="css" scoped>
</style>
