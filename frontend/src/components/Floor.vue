<template>
<div class="floor">
  <p>Created by: <b style="color: red">Alexandr Belmas</b></p>
  <p>My GitHub: <a href="https://github.com/diomaxer/">https://github.com/diomaxer</a></p>
  <p>My resume: <a href="https://career.habr.com/diomaxer">https://career.habr.com/diomaxer</a></p>
</div>
</template>

<script>
export default {
  name: "Floor"
}
</script>

<style scoped>
.floor{
  height: 150px;
  background-color: #07651C;
  padding: 20px 100px;
}
p{
  margin: 0.5%;
  color: wheat;
  font-size: 20px;
}
a{
  color: blue;
  text-decoration: none;
}
</style>