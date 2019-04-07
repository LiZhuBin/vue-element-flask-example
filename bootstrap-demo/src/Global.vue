<template>

</template>

<script>
    const URL_ROOT = "http://127.0.0.1:5000/home/";
    const URL_INFO = URL_ROOT+'info/';
    const URL_WEATHER = URL_ROOT+'weather/';
    const URL_WATER = URL_ROOT+'water/';
    const URL_NEWS = URL_INFO + 'news/';
    const URL_BOOKS = URL_INFO + 'books/';
    const URL_WECHATNEWS = URL_INFO + 'weChatNews/';
    const URL_SPORT = URL_ROOT + 'sport/';
    export default {
        name: "Global",
        URL_ROOT,
      URL_INFO,
      URL_WEATHER,
      URL_WATER,
      URL_NEWS,
      URL_BOOKS,
      URL_WECHATNEWS,
      URL_SPORT
  }

</script>

<style scoped>

</style>
