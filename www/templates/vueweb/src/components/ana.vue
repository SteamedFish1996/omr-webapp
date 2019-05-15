<template>
  <el-container>
    <el-header class="header" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
      <span style="font-family:华文楷体">光学乐谱识别系统</span>
      <button class="el-icon-circle-close-outline exitButt" style="font-family:华文楷体;background-color: white">&nbsp;退出系统</button>
    </el-header>
    <br>
    <el-main>
      <el-header class="header" style="font-family:华文楷体;font-size:120%;font-weight:bold;width:100%;background-color:white;border-top:1px solid #dfdfdf;color:#409dfe;">解析文件</el-header>
     <div>
      <div class="block" style="width:40%;float:left">
          <span class="demonstration">原文件</span>
          <el-image :src="src1"></el-image>
      </div>
      <div class="block" style="width:40%;float:right">
        <span class="demonstration">解析后的文件</span>
        <el-image :src="src2">
          <div slot="placeholder" class="image-slot">
            加载中<span class="dot">...</span>
          </div>
        </el-image>
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
            this.src2=this.$route.query.response.newUrl;
            this.src1=this.$route.query.iUrl;
            console.log(this.file);
        },
        methods: {}
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

</style>