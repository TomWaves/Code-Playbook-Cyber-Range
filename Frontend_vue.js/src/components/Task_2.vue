<template>
  <div class="box">
    <h3>Exercise 2 - Identification</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show task' }}
    </button>
    <div v-if="showInput">
      <p>
        Go into Wazuh and monitor your agents on any security events. You should
        recognize patterns, for initiating the playbook.
      </p>

      <!-- Question2 -->
      <p>
        <b>Question 1: </b>One agent shows an increase in security events. What
        service is this agent monitoring?
      </p>
      <form @submit.prevent="checkAnswer" v-if="!answered">
        <input v-model="answer" required :disabled="answered" />
        <button type="submit" :disabled="answered">Check answer</button>
      </form>
      <div v-if="answered">
        <p>Your answer: "{{ userAnswer }}" is {{ result }}</p>
      </div>

      <!-- Question2 -->
      <p>
        <b>Question 2: </b>Who is/are the owner/s of the exploited credentials?
      </p>
      <form @submit.prevent="checkAnswer2" v-if="!answered2">
        <input v-model="answer2" required :disabled="answered2" />
        <button type="submit" :disabled="answered2">Check answer</button>
      </form>
      <div v-if="answered2">
        <p>Your answer: "{{ userAnswer2 }}" is {{ result2 }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      answer: '',
      correctAnswers: ['http server', 'http', 'http-server'],
      answered: false,
      userAnswer: '',
      result: '',

      answer2: '',
      correctAnswers2: ['connor'],
      answered2: false,
      userAnswer2: '',
      result2: '',

      showInput: false,
    };
  },
  methods: {
    checkAnswer() {
      this.userAnswer = this.answer.toLowerCase();
      if (this.correctAnswers.includes(this.userAnswer)) {
        this.result = 'correct ✅';
      } else {
        this.result =
          'unfortunately incorrect. The correct answer is "HTTP server" ❌';
      }
      this.answered = true;
    },
    checkAnswer2() {
      this.userAnswer2 = this.answer2.toLowerCase();
      if (this.correctAnswers2.includes(this.userAnswer2)) {
        this.result2 = 'correct ✅';
      } else {
        this.result2 =
          'unfortunately incorrect. The correct answer is "Connor" ❌';
      }
      this.answered2 = true;
    },
  },
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