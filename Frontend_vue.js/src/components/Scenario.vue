<template>
  <div class="box">
    <h3>Scenario information</h3>
    <button @click="showInput = !showInput">
      {{ showInput ? 'Collapse' : 'Show scenario information' }}
    </button>
    <div v-if="showInput">
      <p>You will take on the role of a security analyst and handle a Security Information and Event Management (SIEM) system.</p><br>

      <p><b>Wazuh</b>
      <p>Wazuh is open-source SIEM tool, which allows the monitoring of different devices in your network. On each device is a Wazuh Agent installed, which can be monitors different log files.<br><br>If the files log events with a possible releation to an incident, Wazuh shows these events in the <b>Security events</b> or <b>MITTRE ATT&amp;CK</b> dashboard. <br><br>You can also select a specific agent for monitoring.</p>

      <!-- Link in Line 16 war nur ein Quick-Fix, da es Probleme beim Einbetten des Bildes gab; Bild ist enthalten im Folder: https://github.com/TomWaves/Code-Playbook-Cyber-Range/blob/main/Metainformationen%20Szenario/Screenshot%202023-03-02%20at%2012-07-26%20Wazuh%20-%20Wazuh.png
      <div class="photo">  
      <img
          src="https://i.postimg.cc/ZqBYh3q6/Screenshot-2023-03-02-at-12-07-26-Wazuh-Wazuh.png"
        />
      </div>
        -->

      <p><b><br>Scneario network:</b> 
      <p>The network consists of one HTTP server and a Linux machine with SSH access. Below are the known credentials for both machines:</p>
      
      <div class="container">
        <div class="left_1">
        <p><b>HTTP server</p>
        <table>
          <tr>
            <th>Username&emsp;&ensp;</th>
            <th>Password&ensp;</th>
          </tr>
          <tr>
            <td>marius</td>
            <td>marshall</td>
          </tr>
          <tr>
            <td>connor</td>
            <td>sergeant</td>
          </tr>
        </table> 
        </div>

        <div class="right_1">
        <p><b>SSH port</p>
          <table>
            <tr>
              <th>Username&emsp;&ensp;</th>
              <th>Password&ensp;</th>
            </tr>
            <tr>
              <td>admin</td>
              <td>admin</td>
            </tr>
            <tr>
              <td>connor</td>
              <td>cKennway</td>
            </tr>
            <tr>
              <td>marshall</td>
              <td>mLinus</td>
            </tr>
            <tr>
              <td>marius</td>
              <td>mPolo</td>
            </tr>
            <tr>
              <td>clara</td>
              <td>cFilia</td>
            </tr>
            <tr>
              <td>christina</td>
              <td>cAbruzzo</td>
            </tr>
          </table> 
        </div>
      
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
  },
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

.photo {
  cursor: pointer;
}

.photo img {
  width: 600px;
  height: 400px;
}

.left_1 {
  padding: 1rem;
  background-color: #f6f7fa;
  color: #2c3e50;
  border: 1px solid #ddd;
  width: 160px;
  height: 175px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 10pt;
}

.right_1 {
  padding: 1rem;
  background-color: #f6f7fa;
  color: #2c3e50;
  border: 1px solid #ddd;
  width: 160px;
  height: 175px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 10pt;
  position: absolute;
  top: 0%;
  left: 30%;
}
</style>
