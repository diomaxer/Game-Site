<template>
  <div class="hat">
    <h1 class="page-name">viDIO games: <b style="color: red">{{game.name}}</b> </h1>
  </div>
</template>

<script>
export default {
  name: "Header",
  data(){
    return{
      game: {}
    }
  },
  mounted() {
    fetch('http://0.0.0.0:5000/v1/games/1')
    .then(response => response.json())
    .then(json => {
      this.game = json
    })
  }
}
</script>

<style scoped>
.hat {
  text-align: left;
  margin-top: 3%;
  margin-bottom: 0.5%;
  padding-left: 8%;
  color: wheat;
  font-size: 45px;
}
.page-name{
  position: relative;
  margin: 0;
}
</style>