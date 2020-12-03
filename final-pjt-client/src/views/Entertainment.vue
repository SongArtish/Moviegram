<template>
  <div>
    <h2>Entertainment</h2>
    <br>
    <br>
    <b-form-rating
      icon-empty="heart"
      icon-half="heart-half"
      icon-full="heart-fill"
      variant="danger"
      class="bg-dark"
      inline
    ></b-form-rating>
    <!-- icon-clear="slash-circle" show-clear-->
    <br>
    <br>
    <br>
    <br>
    <SlideToUnlock />
    <br>
    <br>
  </div>
</template>

<script>
import SlideToUnlock from '@/components/SlideToUnlock'

export default {
  name: 'Entertainment',
  components: {
    SlideToUnlock
  }
}
</script>

<style>

</style>