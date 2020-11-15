<template>
  <div class='v-user-chat'>
    <div class="skrol">
      
     <button
              class="buts"
              v-on:click="createimg"
          ><img id="btn" src="@/assets/s1.png" class="s1"></button>
          <button
          class="buts"
          v-on:click="createimg"
      ><img id="btn2" src="@/assets/s2.png" class="s1"></button>
      <button
          class="buts"
          v-on:click="createimg"
      ><img id="btn3" src="@/assets/s3.png" class="s1"></button>
      <button
          class="buts"
          v-on:click="createimg"
      ><img id="btn4" src="@/assets/s4.png" class="s1"></button>
        </div>
      </div>
</template>

<script>
  import vMessage from './v-message'
  import {mapActions} from 'vuex'
  export default {

  }
  
  


  
</script>

<style lang="scss">
</style>
