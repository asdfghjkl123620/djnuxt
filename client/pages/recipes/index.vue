<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>吃貨天堂</h3>
          <nuxt-link ot="/recipes/add" class="btn btn-info">添加食譜</nuxt-link>
        </div>
      </div>
      <template v-for="recipe in recipes">
        <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <recipe-card :on-delete="deleteRecipe" :recipe="recipe" />
        </div>
      </template>
    </div>
  </main>
</template>

<script>
export default {
  head () {
    return {
      title: '首頁'
    }
  }
}
</script>

<style>
header{
  min-height: 100vh;
  background-image: linear-gradient(
    to right,
    rgba(0, 0, 0, 0.9),
    rgba(12, 5, 5, 0.4)
  ),
   url("/images/banner.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-family: cursive;
  font-size: 5rem;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
