<template>
  <div class="box">
    <h3>Exercise 5 - Post-Incident</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show task' }}
    </button>
    <div v-if="showInput">
      <p>
        Assume you have completed all remaining steps of the playbook.<br />
        After the follow-up meeting regarding the incident, your team leader
        recommended to extend the playbook as shown in the BPMN model below:
      </p>
      <img
        src="https://i.postimg.cc/fLgjgWSG/BPMN-modell-playbook-LMS-Ex5-drawio-1.png"
      />
      <p><br>Edit the unfinished workflow steps below, so they list the three blue steps of the workflow.<br/>
        You can orient yourself at the playbook to the left.<br/>
      </p>
      <p><b>Note</b> You don't have to write a description or command object!</p>

      <div>
  </div>
      <button @click="showInput2 = !showInput2">
      {{ showInput2 ? 'Collapse' : 'Show Solution' }}
    </button>
    <div v-if="showInput2">
      <JsonPretty
        :data="jsonData"
      ></JsonPretty>
    </div>
  </div>
</template>

<script>
import JsonPretty from 'vue-json-pretty';
import 'vue-json-pretty/lib/styles.css';
import CAP_Ex_5 from './CAP_Ex_5.json';

export default {
  components: {
    JsonPretty,
  },
  data() {
    return {
      jsonData: CAP_Ex_5,
      showInput: false,
      showInput2: false,
      text: "",
    };
  },
  methods: {},
};
</script>

<style>
.box {
  margin-bottom: 1rem;
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 1rem;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 10.5pt;
  color: #2c3e50;
  width: 750px;
}
</style>
