
<template lang="html">
    <div class="Single answer">

        <p class="text-muted">

        <strong> l'autore {{ answer.author }}</strong> ha risposto il  {{ answer.created_at }}
        </p>
        <p>{{ answer.body }}</p>
        <div v-if="isAnswerAuthor" >
            <router-link
                :to="{ name: 'answer-editor', params: {id:answer.id} }"
                class="btn btn-sm btn-success mr-1"
                ><span>Modifica</span>
            </router-link>

       <router-link
                :to="{ name: 'answer-confirm-delete', params: {id:answer.id} }"
                class="btn btn-sm btn-outline-danger"
                ><span>Elimina</span>
     </router-link>
     </div>

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
