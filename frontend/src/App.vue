<template>
  <div id="app">
    <Header/>
    <GamePage/>
    <Floor/>
  </div>
</template>

<script>

import Header from "./components/Header";
import GamePage from "./components/GamePage";
import Floor from "./components/Floor";

export default {
  name: 'App',
  components: {
    Header, GamePage, Floor
  }
}
</script>

<style>
#app{
  margin-left: -10px;
  margin-right: -10px;
  margin-bottom: -10px;
  padding: 0;
}
</style>
