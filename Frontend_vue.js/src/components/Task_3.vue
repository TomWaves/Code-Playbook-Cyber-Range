<template>
  <div class="box">
    <h3>Exercise 3 - Analysis</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show task' }}
    </button>
    <div v-if="showInput">
      <p>
        <b>Question 1:</b> The workflow step "single--id021" tasks you to
        analyze the targeted system. Visit the website hosted on the HTTP server
        and look for information. What system is under potential threat? The
        answer is an <b>IP</b> address.
      </p>
      <form @submit.prevent="checkAnswer" v-if="!answered">
        <input v-model="answer" required :disabled="answered" />
        <button type="submit" :disabled="answered">Check answer</button>
      </form>
      <div v-if="answered">
        <p>Your answer: "{{ userAnswer }}" is {{ result }}</p>
      </div>

      <p>
        <b>Question 2: </b> Because another system is potentially threatened,
        the playbook tasks you with the step "single--id050. Go into Wazuh once
        again, look for an event indicating an attack and write the
        <b>rule.description</b> as answer.<br />Note: It incident indicator may
        not be listed in the playbook.
      </p>
      <form @submit.prevent="checkAnswer2" v-if="!answered2">
        <input v-model="answer2" required :disabled="answered2" />
        <button type="submit" :disabled="answered2">Check answer</button>
      </form>
      <div v-if="answered2">
        <p>Your answer: "{{ userAnswer2 }}" is {{ result2 }}</p>
      </div>

      <p>
        <b>Question 3: </b> Is the attacker currently in second system? Answer
        with yes or no!<br />Note: The last events should be of enough
        information.
      </p>
      <form @submit.prevent="checkAnswer3" v-if="!answered3">
        <input v-model="answer3" required :disabled="answered3" />
        <button type="submit" :disabled="answered3">Check answer</button>
      </form>
      <div v-if="answered3">
        <p>Your answer: "{{ userAnswer3 }}" is {{ result3 }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      answer: '',
      correctAnswers: ['172.21.0.6'],
      answered: false,
      userAnswer: '',
      result: '',

      answer2: '',
      correctAnswers2: [
        'sshd: authentication success.',
        'sshd: authentication success',
        //'sshd: authentication failed.',
        //'sshd: authentication failed',
        //'pam: user login failed.',
        //'pam: user login failed',
        'pam: login session opened.',
        'pam: login session opened',
      ],
      answered2: false,
      userAnswer2: '',
      result2: '',

      answer3: '',
      correctAnswers3: ['yes'],
      answered3: false,
      userAnswer3: '',
      result3: '',

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
          'unfortunately incorrect. The correct answer is "172.21.0.6" ❌';
      }
      this.answered = true;
    },
    checkAnswer2() {
      this.userAnswer2 = this.answer2.toLowerCase();
      if (this.correctAnswers2.includes(this.userAnswer2)) {
        this.result2 = 'correct ✅';
      } else {
        this.result2 =
          'unfortunately incorrect. Correct answers would be "sshd: authentication success" or "pam: login session opened" ❌';
      }
      this.answered2 = true;
    },
    checkAnswer3() {
      this.userAnswer3 = this.answer3.toLowerCase();
      if (this.correctAnswers3.includes(this.userAnswer3)) {
        this.result3 = 'correct ✅';
      } else {
        this.result3 =
          'unfortunately incorrect. The attacker is currently in the machine ❌';
      }
      this.answered3 = true;
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
