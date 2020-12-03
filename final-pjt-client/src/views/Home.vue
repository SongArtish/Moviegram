<template>
  <div class="home">
    <br>
    <h3>Our Vision</h3>
    <p>We are growing faster and faster</p>
    <!-- LAZY LOADING 기능 사용하기 !!! -->
    <div class="mx-5 px-5">
      <b-progress :value="barValue" variant="success" height="2rem" striped animated></b-progress>
    </div>
    <br>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Slides with custom text -->
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
        <h1>Hello world!</h1>
      </b-carousel-slide>
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="He who has a why to live can bear almost any how."
        text="Friedrich Nietzsche"
        img-src="https://picsum.photos/1024/480/?image=52"
      ></b-carousel-slide>


      <!-- Slides with image only -->
      <b-carousel-slide 
        img-src="https://picsum.photos/1024/480/?image=58"
        caption="Lost time is never found again."
        text="Benjamin Franklin"
      ></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide
        caption="He that respects himself is safe from others."
        text="Henry Wadsworth Longfellow"
      >
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="https://picsum.photos/1024/480/?image=55"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
    </b-carousel>


    <br>
    <br>
 <h3 id='home'>Our Language</h3>
    <h3> Python</h3>
    <h3> JavaScript </h3>
  <h3 id='home2'>Our Web Framework</h3>
    <h3> Django </h3>
    <h3> Vue.js </h3>
    <h3> Bootstrap </h3>
  <h3 id='home2'>Featured Music</h3>
    <h3>Guardians of the Galaxy : Awesome Mix</h3>
  <br>
  <br>
  <br>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data: function () {
    return {
      barValue: 10,
      timer: null,
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart() {
        this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    }
  },
  mounted() {
      this.timer = setInterval(() => {
        const calculation = this.barValue + 20
        this.barValue = calculation
      }, 2000)
    },
  beforeDestroy() {
      clearInterval(this.timer)
      this.timer = null
    }
}
</script>

<style>
/* #app {
  width:50%; 
  border: 3px solid black;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  user-select:none;
} */
#home { 
  /* margin-top: 3%; */
  width:80% ;
  margin-left: 10%;
  margin-bottom:5%;
  border: 3px solid white ;
  padding-right: 1px; 
  padding-right: 1px; 
  
}
#home2 { 
  width:80% ;
  margin-left: 10%;
  margin-top:8%; 
  margin-bottom:5%;
  border: 3px solid white ;

}

/* #carousel-1 {
  position: relative;
  z-index: 100;
} */
</style>
