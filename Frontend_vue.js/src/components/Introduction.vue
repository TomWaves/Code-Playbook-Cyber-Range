<template>
  <div class="box">
    <h3>Introduction to the CACAO Standard</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show introduction' }}
    </button>
    <div v-if="showInput">
      <p>CACAO (=collaborative automated course of action operations) is a recently emerging standard for incident response playbooks that utilizes JSON format. This facilitates sharing the playbook with security partners and is readable by both humans and machines.</p>
      <p>A CACAO playbook is divided into different areas: Metadata, Workflow, Targets, Data Markings and Extensions.</p>


      <p><b>Metadata</b> is listed at the beginning of each playbook and describes the general information of the playbook. It describes for example the:</p>
      <ul>
        <li>name, playbook type and description</li>
        <li>creator, dates for creation/modification</li>
        <li>the priority information on the incident</li>
      </ul> 
      
      <p><b>Worklfow</b> contains a series of action steps, which are processed sequentially, in parallel, or both depending on the type of steps. Additionally the workflow sequence can contain condition like if, while or swich. Values of the workflow steps contain usually information on:</p>
      <ul>
        <li>type of the step (start, end, single, parallel, condition, etc.)</li>
        <li>name and description of the step</li>
        <li>the following step upon completion of the current one</li>
        <li>the steps for the a condition</li>
      </ul>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showInput: false,
    }
  }
}
</script>

<style>
.box {
  margin-bottom: 1rem;
  background-color: white;
  border: 1px solid #ddd;
  padding: 1rem;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 10.5pt;
  color: #2c3e50;
  width: 750px;
}
</style>