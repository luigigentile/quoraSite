<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Edit your answer</h1>
                <form @submit.prevent="onSubmit">
                    <textarea
                        v-model="answerBody"
                        class="form-control"
                        rows="3">
                    </textarea>
                    <br>
                    <button
                        class="btn btn-sm btn-success"
                        type="submit"
                        >Publish Question
                    </button>
                    <button
                    @click="tornaIndietro"
                    class="btn btn-sm btn-primary ml-3">
                    No, take me back
                    </button>

            </form>
                <p class="error mt-2">{{ error }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
    name: "AnswerEditor",

    props: {
        id: {
            type: Number,
            required: true
        },
        previousAnswer: {
            type: String,
            required: true
        },
        questionSlug: {
            type: String,
            required: true
        }
    },

    async beforeRouteEnter(to, from, next) {
        // rispetto a method + created, risulta molto utile quanto si lavora
        // con risorse pesanti e importanti (es. immagini)
        let endpoint = `/api/answers/${to.params.id}/`;
        await apiService(endpoint)
                .then(data => {
                    to.params.previousAnswer = data.body;
                    to.params.questionSlug = data.question_slug;
                })
        return next();
    },

    data() {
        return {
            answerBody: this.previousAnswer,
            error: null
        }
    },
    methods: {

        tornaIndietro() {
            this.$router.push({
                name: "question",
                params: { slug: this.questionSlug }
            })
//                   window.history.back()
         },
        onSubmit() {
            if (this.answerBody) {
                let endpoint = `/api/answers/${this.id}/`;
                apiService(endpoint, "PUT", { body: this.answerBody })
                .then(() => {
                    this.$router.push({
                        name: "question",
                        params: { slug: this.questionSlug }
                    })
                })

            } else {
                this.error = "Il campo non può essere vuoto!";
            }
        }
    }
    // methods: {
    //     async getAnswerData() {
    //         let endpoint = `/api/answers/${this.id}/`;
    //         await apiService(endpoint)
    //                 .then(data => {
    //                     this.answerBody = data.body;
    //                 })
    //     }
    // },
    // created() {
    //     this.getAnswerData();
    // }
}
</script>
