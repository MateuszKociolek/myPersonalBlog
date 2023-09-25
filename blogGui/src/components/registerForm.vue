<template >
    <div class="flex flex-col items-center">
        <p class="mb-6 font-bold text-3xl text-transparent bg-clip-text bg-gradient-to-r from-sky-700 to-sky-400 mt-6">Register</p>

        <input class="mb-6 border-solid border-2 border-sky-500 w-80 h-10 rounded-md pl-[14px]" v-model="email" type="email" placeholder="jane@example.com">
        <input class="mb-6 border-solid border-2 border-sky-500 w-80 h-10 rounded-md pl-[14px]" v-model="password" type="password" placeholder="password">
        <input class="mb-6 border-solid border-2 border-sky-500 w-80 h-10 rounded-md pl-[14px]" v-model="username" type="username" placeholder="username">

        <div class="flex">
            <button @click="register" class="bg-sky-500 mr-4 h-10 w-32 rounded text-slate-50 font-mono duration-300 hover:bg-sky-700">Register</button>
            <div class="ml-4">
                <p class="text-xs">If you already registered</p>
                <router-link class="font-blod text-xs text-transparent bg-clip-text bg-gradient-to-r from-sky-700 to-sky-400" to="/login">Log In</router-link>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: "",
            password: "",
            username: "",
        }
    },
    methods: {
        register(){
            const regData = {
                email: this.email,
                password: this.password,
                username: this.username
            }

            axios.post("http://127.0.0.1:8000/create_user", regData)
            .then(res => {
                console.log(res)
                this.email = ""
                this.password = ""
                this.username = ""

                this.$store.commit('changeLoggedStatus');
            })
            .catch(err => {
                console.log(err)
            })

        }
    },
}
</script>

<style>
    
</style>