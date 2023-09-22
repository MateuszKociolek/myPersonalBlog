<template >
    <div>
        <input class="border-2 border-rose-500" v-model="email" type="email" placeholder="jane@example.com">
        <input class="border-2 border-rose-500" v-model="password" type="password" placeholder="password">
        <input class="border-2 border-rose-500" v-model="username" type="username" placeholder="username">

        <button @click="register" class="bg-sky-500">Register</button>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: "",
            password: "",
            username: ""
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