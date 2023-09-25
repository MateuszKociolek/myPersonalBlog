<template>
    <div class="flex flex-col items-center">
        <p class="font-bold text-3xl text-transparent bg-clip-text bg-gradient-to-r from-sky-700 to-sky-400 mt-6">Log In</p>

        <input v-model="email" type="email" class="mb-6 mt-6 border-solid border-2 border-sky-500 w-80 h-10 rounded-md pl-[14px]" placeholder="Email">
        <input v-model="password" type="password" class="mb-6 border-solid border-2 border-sky-500 w-80 h-10 rounded-md pl-[14px]" placeholder="Password">

        
        <div class="flex ">
            <button class="bg-sky-500 h-10 w-28 rounded text-slate-50 font-mono duration-300 hover:bg-sky-700" @click="logIn">Log In</button>
            <div class="ml-4">
                <p class="text-xs">If you dont have account</p>
                <router-link class="font-blod text-xs text-transparent bg-clip-text bg-gradient-to-r from-sky-700 to-sky-400" to="/register">Sign In</router-link>
            </div>
        </div>

        <p class="text-red-600">{{ errMsg }}</p>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            email: "",
            password: "",
            errMsg: ""
        }
    },
    methods: {
        logIn() {
            const logData = {
                email: this.email,
                password: this.password,
                username: ""
            }

            axios.post("http://127.0.0.1:8000/logToAccount/", logData)
            .then(response => {
                
                const current_user_logged = response.data.res[0]["username"];
                console.log(current_user_logged)
                this.$store.dispatch('setCurrentLoggedUser', current_user_logged);

                if(Object.keys(response.data.res).length === 0) {
                    this.errMsg = "Incorrect email or password"
                }else{
                    
                    this.$router.push("/")
                    this.$store.commit('changeLoggedStatus');
                }
            })
            .catch(err =>{
                console.log(err)
                
            })

        }
    },
}
</script>
<style>
</style>