<template>
  <div >
    
  <Carousel :autoplay="5000" :wrap-around="true" class="carousel">
    <Slide v-for="slide in slides" :key="slide.id" class="slide-info">
      <div>
        <img :src="`../src/assets/${slide.src}`"/>
        <span style="position: absolute; top: 30%; left: 50%;">Some text..</span>
      </div>
    </Slide>
    

    <template #addons>
      <Pagination />
    </template>
  </Carousel>
</div>
</template>

<script>
import { defineComponent } from 'vue'
import { Carousel, Pagination, Slide } from 'vue3-carousel'

import 'vue3-carousel/dist/carousel.css'

export default defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
  },

  setup() {
    const slides = [
      {id: 1, src: "Home1.jpg"},
      {id: 2, src: "Home2.jpg"},
      {id: 3, src: "Home3.jpg"},
    ];

    return { slides };
  },
})
</script>

<style lang="scss" scoped>
.carousel {
  position: relative;
  max-height: 70vh;
  height: 70vh;

  .slide-info {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    max-height: 80%;
    height: 80%;

    img {
      min-width: 100%;
      height: 80%;
      object-fit: cover;
    }
  }
}
</style>