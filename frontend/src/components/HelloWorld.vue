<template>
  <div>
    <h1>Response from the Backend Micro-Service</h1>
    <div v-for="result in results.results" v-bind:key="result.id">
      {{result.result}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    results: {}
  }
}
</script>

<style scoped>
</style>
