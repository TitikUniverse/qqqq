<template>
<div class="block">
    <div class="wrapper mt-4 ml-4"> <!-- Этот относится к...-->
        <div class="row">
                <div class="col-sm-6 mx-auto">
                    <form>
                        <div v-show="step === 1" class="step">
                        <br>
                        <h1 style="font-size:33px;">Войти</h1>
                        
                            <br>
                            <div class="login">
                                <input v-model="login" type="text" class="input" placeholder="Ваш email" >
                            </div>
                            

                            <div class="login">  
                                <input v-model="password" type="password" for="passwordConfirm" class="input" placeholder="Пароль">
                            </div>
                            <br>


                            <router-link to="/chats" class="orange btn" @click.prevent="signIn">Войти</router-link>

                            <br>
                            <br>

                            <a @click="nextStep"  style="color:blue; font-size: 15px; font-family: Roboto;">Забыли пароль?</a>
                        </div> <!-- class step -->


                        <div v-show="step === 2" class="step">
                        <h1 style="font-size:33px; font-family:">Забыли пароль</h1>
                        
                            <br>
                            <div class="login">
                                <input type="text" class="form-control input" placeholder="Ваш никнейм">
                            </div>

                            <div class="login">  
                                <input type="email" class="form-control input" placeholder="Ваша почта">
                            </div>
                            <br>

                            <button @click="nextStep" type="button" class="btn" id="orange">Получить код</button>

                            <br>
                            <br>
                            <a @click="backStep" style="font-size: 15px; font-family:Roboto; color: blue; "> Вернуться назад</a>

                            </div> <!-- class step -->


                            <div v-show="step === 3" class="step">
                            <h3 style="font-size: 33px; font-family:">Введите код</h3>
                            <div class="form-group col s4">
                                <input type="number" class="form-control"  placeholder="  0000-0000 " id="exampleInputNumber1" > <!--В данном форме вводиться код, который пользователь получил на почту-->
                            </div>
                            
                            <br>
                            <br>
                            <br>

                            <div class="col s12">
                                <button @click="nextStep" s type="button" class="btn btn-primary">Далее</button>
                            </div>
                        </div> <!-- class step -->


                        <div v-show="step === 4" class="step">
                            <h3 style="font-size: 33px; font-family:">Введите новый пароль</h3>

                             <div class="login">  
                                <input type="password" for="passwordConfirm" class="form-control input" placeholder="Пароль" >
                            </div>

                             <div class="login">  
                                <input type="password" for="passwordConfirm" class="form-control input" placeholder="Подтвердите пароль" >
                            </div>
                             <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                                <label class="form-check-label" for="exampleCheck1">Посмотреть пароль</label>
                            </div>
                            
                            
                            
                            <router-link to="/profile" class="btn btn-primary">Готово</router-link> 
                        </div>        
                        
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
            step: 1,
            login: '',
            password: ''
        }
    },
    methods: {
        nextStep() {
            this.step++
        },
         backStep() {
            this.step--
        },
        signIn() {
            const path = 'http://localhost:5000/login';
            payLoad = {login: this.login, password: this.password}
            axios.post(path, payLoad)
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error) => {
                // eslint-отключение следующей строки
                console.log(error);
                
                });
        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans+Extra+Condensed:ital,wght@1,900&display=swap');
</style>
