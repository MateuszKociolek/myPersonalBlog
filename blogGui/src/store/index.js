import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogged:false,
    currentLoggedUser: "tf",
  },
  getters: {
  },
  mutations: {
    changeLoggedStatus(state){
      state.isLogged = true;
    },

    setCurrentUser(state, currentUser){
      state.currentLoggedUser = currentUser;
    }
  },
  actions: {
    setCurrentLoggedUser({commit}, currentUser){
      commit('setCurrentUser', currentUser)
    }
  },
  modules: {
  }
})
