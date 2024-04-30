<template>
  <header>
    <h2>Welcome to CAPE - The Credential-Access-Playbook Exercise</h2>
  </header>

  <div class="container">
    <div class="left">
      <JsonPretty
        :data="{ jsonData }"
        :showLine="false"
        :showIcon
        :showLineNumber
      ></JsonPretty>
    </div>

    <div class="right">
      <Introduction></Introduction>
      <Task1></Task1>
      <Scenario></Scenario>
      <Task2></Task2>
      <Task3></Task3>
      <Task4></Task4>
      <Task5></Task5>
      <Questions></Questions>
    </div>
  </div>
</template>

<script>
import JsonPretty from 'vue-json-pretty';
import 'vue-json-pretty/lib/styles.css';

import playbook from './components/CyberRange_Playbook.json';
import Introduction from './components/Introduction.vue';
import Scenario from './components/Scenario.vue';
import Task1 from './components/Task_1.vue';
import Task2 from './components/Task_2.vue';
import Task3 from './components/Task_3.vue';
import Task4 from './components/Task_4.vue';
import Task5 from './components/Task_5.vue';
import Questions from './components/Questions.vue';

export default {
  name: 'App',
  components: {
    JsonPretty,
    Introduction,
    Task1,
    Scenario,
    Task2,
    Task3,
    Task4,
    Task5,
    Questions,
  },
  data() {
    return {
      jsonData: playbook,
    };
  },
};
</script>

<style>
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
}

.left {
  flex: 1;
  padding: 1rem;
  background-color: #f6f7fa;
  color: #2c3e50;
  border: 1px solid #ddd;
  width: 1000px;
  height: 800px;
  overflow-x: auto;
  overflow-y: scroll;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.right {
  flex: 1;
  padding: 1rem;
}

header {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  text-align: center;
}
.page-text {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 11pt;
  color: #2c3e50;
}

body {
  background-color: white;
}
</style>
