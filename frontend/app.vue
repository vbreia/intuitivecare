<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <SearchOperadoras />
  </div>
</template>

<script>
import SearchOperadoras from './components/SearchOperadoras.vue';

export default {
  components: {
    SearchOperadoras,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>