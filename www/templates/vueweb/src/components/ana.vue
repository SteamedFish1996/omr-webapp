<template>
  <el-container>
        <el-header id="header">
      <el-button class="el-icon-back" @click="go()"></el-button>
      <p>文件解析</p>
    </el-header>
    <br>
    <el-main>   
     <div>
      <div class="block" style="width:40%;float:left">
          <span class="demonstration">原文件</span>
        <br>
        <img :src="src1" style="width: 100%;">
      </div>
      <div class="block" style="width:40%;float:right">
        <span class="demonstration">解析后的文件</span>
        <br>  
      <img :src="src2" style="width: 100%;" >
      </div>
     </div>
    </el-main>
  </el-container>
</template>
<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                response:[],
                src1:"",
                src2:"",
            }
        },
        created(){
            this.src2=require("../../../../static/images/"+this.$route.query.response.newUrl);
            this.src1=this.$route.query.iUrl;
            console.log(this.src1);
            console.log(this.src2);
        },
        methods: {
          go(){
            this.$router.go(-1);
          },
        }
    }
</script>
<style scoped>
  .header{
    height: 60px;
    color: #409dfe;
    line-height: 60px;
    font-size: 25px;
    text-align: left;
  }
  .exitButt{
    position: absolute;
    border: none;
    color: #409dfe;
    font-size: 15px;
    height: 60px;
    right: 50px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
  }
    .el-header .el-icon-back{
    position: absolute;
    width: 60px;
    height: 55px;
    background-color: #409dfe;
    border-color: #409dfe;
    color: white;
    left: 10px;
    top: 10px;
  }
  .el-header .el-icon-back:hover{background-color: #409dfe;border-color: #409dfe;}
  .el-header .el-icon-back:focus{background-color: #409dfe;border-color: #409dfe;}
  .el-header{
    margin: 0px;
    padding: 0px;
    background-color: #409dfe;
    color:white;
    font-size: 20px;
    line-height: 22px;
    text-align: center;
  }
</style>
