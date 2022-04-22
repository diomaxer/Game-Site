<template>
<div class="game-page">
  <canvas class="web-game" width="1280" height="720">  </canvas>
</div>
</template>

<script>
export default {
  name: "GamePage"
}
</script>

<style scoped>
.game-page{
  margin: 0;
  padding: 0;
  text-align: center;
  background-color: wheat;

}

.web-game{
  margin: 3%;
  background-color: black;
}
</style>