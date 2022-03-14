import {createApp} from 'vue'
import App from './App.vue'
import Vuex from "vuex";
import axios from "axios";
import {getFakeDancer} from "@/utils";


const store = new Vuex.Store({
    state: {
        dancers: [],
        style: '',
    },
    actions: {
        loadDancers: function ({commit}, style) {
            axios.get(`http://localhost:8000/dancers/?style=${style}`).then((response) => {
                commit('SET_STYLE', {style})
                commit('SET_DANCER_LIST', {dancers: response.data})
            }, (err) => {
                console.log(err)
            })
        },
        addDancer: function () {
            axios.post(`http://localhost:8000/dancers/`, getFakeDancer()).then(
                () => store.dispatch('loadDancers', this.state.style)
                , (err) => {
                    console.log(err)
                })
        }
    },
    mutations: {
        SET_DANCER_LIST: (state, {dancers}) => {
            state.dancers = dancers
        },
        SET_STYLE: (state, {style}) => state.style = style
    },
    getters: {
        stopDancers: state => {
            return state.dancers.filter(dancer => dancer.action === 'STOP')
        },
        activeDancers: state => {
            return state.dancers.filter(dancer => dancer.action === 'ACTIVE')
        },
        drinkingDancers: state => {
            return state.dancers.filter(dancer => dancer.action === 'STOP')
        },
        dancers: (state) => {
            return state.dancers
        }
    }
})

createApp(App).use(store).mount('#app')