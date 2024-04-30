<template>
  <div class="box">
    <h3>Exercise 1 - Map the workflow sequence</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show task' }}
    </button>
    <div v-if="showInput">
      <p>
        The following BPMN model represents the incident response flow of the
        playbook.
      </p>
      <p>
        Populate the empty tasks with their ID and the empty gateways with a '+'
        for parallel flow and 'x' for an if condition.
      </p>
      <div class="container">
        <img
          src="https://i.postimg.cc/DyPXzhbh/BPMN-modell-playbook-leer.png"
        />
        <div class="task-1" :class="{ correct: isCorrect_task_1 }">
          <input
            type="text"
            v-model="inputText_task_1"
            @input="checkInput_task_1"
            class="input-field-task"
          />
        </div>
        <div class="task-2" :class="{ correct: isCorrect_task_2 }">
          <input
            type="text"
            v-model="inputText_task_2"
            @input="checkInput_task_2"
            class="input-field-task"
          />
        </div>
        <div class="task-3" :class="{ correct: isCorrect_task_3 }">
          <input
            type="text"
            v-model="inputText_task_3"
            @input="checkInput_task_3"
            class="input-field-task"
          />
        </div>
        <div class="task-4" :class="{ correct: isCorrect_task_4 }">
          <input
            type="text"
            v-model="inputText_task_4"
            @input="checkInput_task_4"
            class="input-field-task"
          />
        </div>
        <div class="task-5" :class="{ correct: isCorrect_task_5 }">
          <input
            type="text"
            v-model="inputText_task_5"
            @input="checkInput_task_5"
            class="input-field-task"
          />
        </div>
        <div class="task-6" :class="{ correct: isCorrect_task_6 }">
          <input
            type="text"
            v-model="inputText_task_6"
            @input="checkInput_task_6"
            class="input-field-task"
          />
        </div>
        <div class="gateway-1" :class="{ correct: isCorrect_gateway_1 }">
          <input
            type="text"
            v-model="inputText_gateway_1"
            @input="checkInput_gateway_1"
            class="input-field-gateway"
          />
        </div>
        <div class="gateway-2" :class="{ correct: isCorrect_gateway_2 }">
          <input
            type="text"
            v-model="inputText_gateway_2"
            @input="checkInput_gateway_2"
            class="input-field-gateway"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText_task_1: '',
      isCorrect_task_1: false,
      inputText_task_2: '',
      isCorrect_task_1: false,
      inputText_task_3: '',
      isCorrect_task_1: false,
      inputText_task_4: '',
      isCorrect_task_1: false,
      inputText_task_5: '',
      isCorrect_task_1: false,
      inputText_task_6: '',
      isCorrect_task_1: false,
      inputText_gateway_1: '',
      isCorrect_gateway_1: false,
      inputText_gateway_2: '',
      isCorrect_gateway_1: false,
      showInput: false,
    };
  },
  methods: {
    checkInput_task_1() {
      if (this.inputText_task_1.toLowerCase() === 'parallel--id010') {
        this.isCorrect_task_1 = true;
      } else if (this.inputText_task_1.toLowerCase() === '"parallel--id010"') {
        this.isCorrect_task_1 = true;
      } else {
        this.isCorrect_task_1 = false;
      }
    },
    checkInput_task_2() {
      if (this.inputText_task_2.toLowerCase() === 'single--id021') {
        this.isCorrect_task_2 = true;
      } else if (this.inputText_task_2.toLowerCase() === '"single--id021"') {
        this.isCorrect_task_2 = true;
      }else {
        this.isCorrect_task_2 = false;
      }
    },
    checkInput_task_3() {
      if (this.inputText_task_3.toLowerCase() === 'single--id022') {
        this.isCorrect_task_3 = true;
      } else if (this.inputText_task_3.toLowerCase() === '"single--id022"') {
        this.isCorrect_task_3 = true;
      }else {
        this.isCorrect_task_3 = false;
      }
    },
    checkInput_task_4() {
      if (this.inputText_task_4.toLowerCase() === 'single--id050') {
        this.isCorrect_task_4 = true;
      } else if (this.inputText_task_4.toLowerCase() === '"single--id050"') {
        this.isCorrect_task_4 = true;
      }else {
        this.isCorrect_task_4 = false;
      }
    },
    checkInput_task_5() {
      if (this.inputText_task_5.toLowerCase() === 'single--id070') {
        this.isCorrect_task_5 = true;
      } else if (this.inputText_task_5.toLowerCase() === '"single--id070"') {
        this.isCorrect_task_5 = true;
      }else {
        this.isCorrect_task_5 = false;
      }
    },
    checkInput_task_6() {
      if (this.inputText_task_6.toLowerCase() === 'single--id100') {
        this.isCorrect_task_6 = true;
      } else if (this.inputText_task_6.toLowerCase() === '"single--id100"') {
        this.isCorrect_task_6 = true;
      }else {
        this.isCorrect_task_6 = false;
      }
    },
    checkInput_gateway_1() {
      if (this.inputText_gateway_1.toLowerCase() === '+') {
        this.isCorrect_gateway_1 = true;
      } else {
        this.isCorrect_gateway_1 = false;
      }
    },
    checkInput_gateway_2() {
      if (this.inputText_gateway_2.toLowerCase() === 'x') {
        this.isCorrect_gateway_2 = true;
      } else {
        this.isCorrect_gateway_2 = false;
      }
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

.container {
  position: relative;
}

.task-1 {
  position: absolute;
  top: 15.25%;
  left: 17.5%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 10px;
  color: white;
}

.task-2 {
  position: absolute;
  top: 8.2%;
  left: 48.1%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 20px;
  color: white;
}

.task-3 {
  position: absolute;
  top: 22.2%;
  left: 48.1%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 20px;
  color: white;
}

.task-4 {
  position: absolute;
  top: 54.6%;
  left: 17.5%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 20px;
  color: white;
}

.task-5 {
  position: absolute;
  top: 45.4%;
  left: 54.7%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 20px;
  color: white;
}

.task-6 {
  position: absolute;
  top: 87%;
  left: 46.7%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 20px;
  color: white;
}

.gateway-1 {
  position: absolute;
  top: 15.1%;
  left: 31.3%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 10px;
  color: white;
}

.gateway-2 {
  position: absolute;
  top: 33.6%;
  left: 80.8%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  padding: 10px;
  font-size: 10px;
  color: white;
}

.correct {
  background-color: #81e8bd;
  padding: 1px;
}

.input-field-task {
  font-size: 14px;
  width: 95px;
  padding: 5px;
  text-align: center;
  background-color: transparent;
}

.input-field-gateway {
  font-size: 14px;
  width: 15px;
  padding: 4px;
  background-color: transparent;
  text-align: center;
}
</style>