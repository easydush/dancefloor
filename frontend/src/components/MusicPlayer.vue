<template>
  <div id="player">
    <section class="player">
      <h2 class="song-title">{{ current.title }} - <span>{{ current.artist }}</span></h2>
      <div class="controls">
        <button class="prev" @click="prev">Prev</button>
        <button class="play" v-if="!isPlaying" @click="play">Play</button>
        <button class="pause" v-else @click="pause">Pause</button>
        <button class="next" @click="next">Next</button>
      </div>
    </section>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: 'MusicPlayer',
  data() {
    return {
      current: {},
      index: 0,
      isPlaying: false,
      songs: [
        {
          title: 'Save your tears',
          artist: 'Weeknd',
          style: 'pop',
          src: require('@/assets/music/pop.mp3')
        },
        {
          title: 'HIGHEST IN THE ROOM',
          artist: 'Travis Scott',
          style: 'hip-hop',
          src: require('@/assets/music/hip-hop.mp3')
        },
        {
          title: 'Roses',
          artist: 'SAINt JHN feat. Imanbek',
          style: 'electrodance',
          src: require('@/assets/music/electrodance.mp3')
        },
      ],
      player: new Audio()
    }
  },
  methods: {
    ...mapActions({
      loadDancers: 'loadDancers',
    }),
    switchMusic() {
      this.loadDancers(this.isPlaying ? this.current.style : '')
    },
    play(song) {
      if (typeof song.src != "undefined") {
        this.current = song;
        this.player.src = this.current.src;
      }
      this.player.play();
      this.player.addEventListener('ended', function () {
        this.index++;
        if (this.index > this.songs.length - 1) {
          this.index = 0;
        }
        this.current = this.songs[this.index];
        this.play(this.current);
      }.bind(this));
      this.isPlaying = true;
      this.switchMusic();
    },
    pause() {
      this.player.pause();
      this.isPlaying = false;
      this.switchMusic();
    },
    next() {
      this.index++;
      if (this.index > this.songs.length - 1) {
        this.index = 0;
      }
      this.current = this.songs[this.index];
      this.play(this.current);
    },
    prev() {
      this.index--;
      if (this.index < 0) {
        this.index = this.songs.length - 1;
      }
      this.current = this.songs[this.index];
      this.play(this.current);
    }
  },
  created() {
    this.current = this.songs[this.index];
    this.player.src = this.current.src;
    this.switchMusic();
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: sans-serif;
  background: lightcyan;
  background: radial-gradient(circle, darkcyan, cadetblue);
}

header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
  background-color: #212121;
  color: #FFF;
}

main {
  width: 100%;
  max-width: 768px;
  margin: 0 auto;
  padding: 25px;
}

.song-title {
  color: #53565A;
  font-size: 32px;
  font-weight: 700;
  text-transform: uppercase;
  text-align: center;
}

.song-title span {
  font-weight: 400;
  font-style: italic;
}

.controls {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px 15px;
}

button {
  appearance: none;
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}

button:hover {
  opacity: 0.8;
}

.play, .pause {
  font-size: 20px;
  font-weight: 700;
  padding: 15px 25px;
  margin: 0 15px;
  border-radius: 8px;
  color: #FFF;
  background-color: #CC2E5D;
}

.next, .prev {
  font-size: 16px;
  font-weight: 700;
  padding: 10px 20px;
  margin: 0 15px;
  border-radius: 6px;
  color: #FFF;
  background-color: #FF5858;
}

.playlist h3 {
  color: #212121;
  font-size: 28px;
  font-weight: 400;
  margin-bottom: 30px;
  text-align: center;
}
</style>