
<template lang="html">
    <div class="Single answer">

        <p class="text-muted">

        <strong> l'autore {{ answer.author }}</strong> ha risposto il  {{ answer.created_at }}
        </p>
        <p>{{ answer.body }}</p>
        <div v-if="isAnswerAuthor()" >
            <router-link
            :to="{ name: 'answer-editor', params: {id:answer.id} }"
            class="btn btn-sm btn-success mr-1"
            ><span>Modifica</span>
            </router-link>

            <button
                 class="btn btn-sm btn-outline-danger"
                 @click="triggerDeleteAnswer"
                 >Cancella
            </button>
        </div>
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
        userHasAnswered: {
            type: Boolean,
            required:true
        },
    },

    methods: {
    isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        },
        triggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer);
        },

    },
}


</script>




<style lang="css" scoped>
</style>
