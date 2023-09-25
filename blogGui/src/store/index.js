import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogged:false
  },
  getters: {
  },
  mutations: {
    changeLoggedStatus(state){
      state.isLogged = true;
    },

  },
  actions: {
  },
  modules: {
  }
})
