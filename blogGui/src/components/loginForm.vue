<template>
    <div class="loginForm">
        <h2>Zaloguj</h2>

        <input v-model="email" type="email" id="loginInput" placeholder="Email">
        <input v-model="password" type="password" id="loginInput" placeholder="Password">

        <button id="loginButton" @click="logIn">Zaloguj</button>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            email: "",
            password: ""
        }
    },
    methods: {
        logIn() {
            const logData = {
                email: this.email,
                password: this.password,
                username: "new"
            }

            axios.post("http://127.0.0.1:8000/logToAccount/", logData)
            .then(res => {
                console.log(res)
            })
            .catch(err =>{
                console.log(err)
            })
        }
    },
}
</script>
<style lang="css">
    @import url('https://fonts.googleapis.com/css2?family=Inclusive+Sans&display=swap');

    .loginForm{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 38%;
        
    }

    h2 {
     font-size: 162%;
    }

    #loginInput{
        font-family: 'Inclusive Sans', sans-serif;
        border: 2px solid #0077B6;
        border-radius: 5px;
        margin-bottom: 7px;
        height: 36px;
        width: 100%;
        text-indent: 23px;
        font-size: 111%;
    }

    #loginInput::placeholder{
        font-weight: bold;
        /* font-size: 111%; */
        opacity: 0.65;
    }

    #loginButton{
        font-family: 'Inclusive Sans', sans-serif;
        width: 60%;
        height: 35px;
        background-color: #0096C7;
        border:  none;
        border-radius: 3px;
        color:  white;
        font-size:  100%;

    }
</style>