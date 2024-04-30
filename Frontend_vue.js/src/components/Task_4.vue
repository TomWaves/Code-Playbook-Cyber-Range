<template>
  <div class="box">
    <h3>Exercise 4 - Containment</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show task' }}
    </button>
    <div v-if="showInput">
      <p>You have identified, that more than one system is attacked, and that the attacker is currently in logged into the SSH machine. Assume that the attacker is already blocked from accessing the HTTP server. </p>
      <b>Question:</b> What step of the playbook would now follow based on the current situation?
      </p>
      <p></p>
      <form @submit.prevent="checkAnswer" v-if="!answered">
        <input v-model="answer" required :disabled="answered" />
        <button type="submit" :disabled="answered">Check answer</button>
      </form>
      <div v-if="answered">
        <p>Your answer: "{{ userAnswer }}" is {{ result }}</p>
      </div>

      <p>Execute the current workflow step!<br>Log into the SSH machine as admin, kick the attacker out of his session and block the access for the user he exploited!</p>

      <p>You can use for this the following commands:</p>
       <ul>
        <li>Checking the last logged in users <br> » <b>last</b></li>
        <li>Killing the session of a user  <br>» <b>sudo pkill -KILL -u [USERNAME]</li>
        <li>Disallowing the a user to login <br>» <b>sudo usermod --expiredate 1 [USERNAME]</li>
      </ul> 
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      answer: '',
      correctAnswers: ['single--id070', "single--id070", "id070"],
      answered: false,
      userAnswer: '',
      result: '',

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
          'unfortunately incorrect. The correct answer is "single-id070" ❌';
      }
      this.answered = true;
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