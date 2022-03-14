<template>
  <div id="app">
    <header>
      <h1>Dance club</h1>
    </header>
    <main>
      <div>
        <MusicPlayer></MusicPlayer>
      </div>
      <div class="content">
        <div v-for="dancer in dancers" v-bind:key="dancer.name">
          <span class="name">{{ dancer.name }}</span>
          <span>{{ dancer.movement }}</span>
        </div>
        <div v-if="dancers.length < 1">
          <span>No dancers</span>
        </div>
        <div class="controls">
          <button class="add" @click="add">Add dancer</button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import MusicPlayer from "@/components/MusicPlayer";
import {mapActions, mapGetters} from "vuex";

export default {
  components: {MusicPlayer},
  computed: {
    ...mapGetters(["dancers"])
  },
  methods: {
    ...mapActions({
      addDancer: 'addDancer',
    }),
    add() {
      this.addDancer()
    }
  }
}
</script>
<style>
.name {
  color: lightcyan;
  padding-right: 5px;
}

.controls {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px 15px;
}

.add {
  font-size: 16px;
  font-weight: 700;
  padding: 10px 20px;
  margin: 0 15px;
  border-radius: 6px;
  color: #FFF;
  background-color: lightseagreen;
}
</style>
