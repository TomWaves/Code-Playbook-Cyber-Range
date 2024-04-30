<template>
  <div class="box">
    <h3>Feedback</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show questions' }}
    </button>
    <div v-if="showInput">
      <p><b>Thank you very much for participating in CAPE!</b></p>
      <p>
        For feedback to the training, please take some time and complete the
        following formular.
      </p>

      <iframe
        width="640px"
        height="480px"
        src="https://forms.office.com/e/RsdzrTvuU3?embed=true"
        frameborder="0"
        marginwidth="0"
        marginheight="0"
        style="border: none; max-width: 100%; max-height: 100vh"
        allowfullscreen
        webkitallowfullscreen
        mozallowfullscreen
        msallowfullscreen
      >
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showInput: false,
    };
  },
};
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
