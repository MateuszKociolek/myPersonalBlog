<template>
    <div class="loginForm">
        <h2>Zaloguj</h2>

        <input type="text" id="loginInput">
        <input type="text" id="loginInput">

        <button id="loginButton">Zaloguj</button>
    </div>
</template>
<script>
export default {
    
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
        border: 2px solid #0077B6;
        border-radius: 5px;
        margin-bottom: 7px;
        height: 36px;
        width: 100%;
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