<template>
  <div id="app">
    <HelloWorld v-bind:results="results" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import axios from 'axios';

export default {
  name: 'app',
  components: {
    HelloWorld
  },
  data() {
    return {
      results: []
    }
  },
  created() {
    axios.get('http://localhost:5000')
      .then(res => {
        this.results = res.data
      });
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
