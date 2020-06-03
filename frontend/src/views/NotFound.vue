<template lang="html">
    <div class="not-Found">
        <div class="container mt-3">
            <h1 id="notfound"> {{ messagge }}</h1>

        </div>


    </div>

</template>

<script>
export default {
    name: "NorFound",
    data() {
        return {
            messagge : "404 Pagina Non Trovata"
        }

    }
}
</script>

<style lang="css">
    #notfound {
        color:red;
        text-align: center;
}
</style>
