
al<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted(){
    var _this = this
    window.onresize = () => {
      _this.$store.state.screenWidth = document.documentElement.clientWidth
      _this.$store.state.screenHeight = document.documentElement.clientHeight
      _this.$store.state.isMobile = navigator.userAgent.toLowerCase().match(/(phone|pad|pod|iphone|ipod|ios|ipad|android|mobile|blackberry|iemobile|mqqbrowser|juc|fennec|wosbrowser|browserng|webos|symbian|windows phone)/i) !== null
      _this.$store.state.isVertical = document.documentElement.clientWidth < document.documentElement.clientHeight
    }
  },
}
</script>

<style>

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  .activeInput .el-input__inner{
    height: 50px;
    font-size: 20px;
  }
  .bottomButt{
    height: 50px;
    width: 85vw;
    font-size: 20px;
    background-color: #494e8f;
    border-color: #494e8f;
    color: white;
  }
  .bottomButt:hover{
    background-color: #8084b1;
    border-color: #8084b1;
    color: white;
  }
  .bottomButt:focus{
    background-color: #8084b1;
    border-color: #8084b1;
    color: white;
  }
</style>
