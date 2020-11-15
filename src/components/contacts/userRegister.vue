<template>

  <div class="block">
    <div class="wrapper mt-4 ml-4"> <!-- Этот относится к...-->
      <div class="row">
        <div class="col-sm-6 mx-auto">
          <form>
            <br>
            <h1 style="font-size:33px; font-family:">Регистрация</h1>
            <div >
              <br>
              <div class="login" >
                <input class="input" v-model="nick"  placeholder="Ваш никнейм" >
              </div>


              <div class="login">
                <input class="input" v-model="login" placeholder="E-mail" >
                
              </div>

              <div class="login">  
                <input class="input" v-model='password' type="password" placeholder="Пароль">
              </div>
              <div>
                <small>Придумайте сложный пароль и запомните его</small>
              </div>
              <br>
              <router-link  @click.prevent="registrIn" class="btn btn-primary orange" to="/profile" >Регистрация</router-link>

              <br>
              <br>
              <pre><small i style="font-size: 15px;">Уже зарегистрированы?  <router-link to="/login" style="font-size: 15px;">Войти</router-link></small></pre>
            </div> <!-- class step -->          
          </form>
        </div> <!-- к этому классу col-sm-6 -->
      </div> <!-- к классу row (типа ряд)-->
    </div><!-- этому -->

  </div>


</template>

<script>
import axios from 'axios';
export default {
  data() {
        return {
            login: '',
            password: '',
            nick: '',
            msg: ''
        }
    },
    methods: {
        registrIn() {
            const path = 'http://localhost:5000/registration';
            payLoad = {login: this.login, password: this.password}
            axios.post(path, payLoad)
                .then((res) => {
                    //this.msg = res.data;
                    console.log(this.msg)
                })
                .catch((error) => {
                // eslint-отключение следующей строки
                console.log(error);
                
                });
        }
    }
}
 
</script>

<style skoped>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans+Extra+Condensed:ital,wght@1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Marck+Script&display=swap');
