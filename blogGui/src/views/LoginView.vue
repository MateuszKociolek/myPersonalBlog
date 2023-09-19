<template lang="">
    <div class="container">
        <loginForm/>
    </div>
</template>

<script>
import loginForm from '@/components/loginForm.vue';

export default {
    components:{
        loginForm
    }   
}
</script>

<style>
    .container{
        display: flex;
        /* flex-direction: column; */
        justify-content: center;
    }
</style>