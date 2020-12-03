<template>
  <div>
    <img src="@/assets/iphone.png" alt="" style='width: 25%; height: 25%; display: inline;'>
    <vue-glide style='display: inline;'>
      <vue-glide-slide @glide:swipe-end="toMovie">Slide to Unlock</vue-glide-slide>
    </vue-glide>
  </div>
</template>

<script>
export default {
  name: 'SlideToUnlock',
  methods: {
    toMovie: function () {
      this.$router.push({ name:'MovieRecommend' })
    }
  }
}
</script>

<style>

</style>