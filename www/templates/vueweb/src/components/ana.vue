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
    <el-footer>
      <el-button style="margin-right: 10px;" type="primary" @click="down">打包下载文件</el-button>
    </el-footer>
  </el-container>
</template>
<script>
    import axios from 'axios';
    //import saveAs from 'file-saver';
    //import FileSaver from 'file-save';
    var FileSaver = require('file-saver');
    var JSZip = require("jszip");
    const getFile = url => {
    return new Promise((resolve, reject) => {
        axios({
            method:'get',
            url,
            responseType: 'arraybuffer'
        }).then(data => {
            resolve(data.data)
        }).catch(error => {
            reject(error.toString())
        })
    })
}
    export default {
        data() {
            return {
                response:[],
                src1:"",
                src2:"",
                mp3:"",
                xml:"",
            }
        },
        created(){
            this.src1=this.$route.query.iUrl;
            console.log(this.src1);
            this.src2=require("../../../../static/images/"+this.$route.query.response.newpng);
            this.mp3=require("../../../../static/result/"+this.$route.query.response.mp3);
            this.xml=require("../../../../static/result/"+this.$route.query.response.xml);
        },
        methods: {
          go(){
            this.$router.go(-1);
          },
    
          down(){
            const data = [this.mp3,this.xml] // 需要下载打包的路径, 可以是本地相对路径, 也可以是跨域的全路径
            const zip = new JSZip()
            const cache = {}
            const promises = []
            data.forEach(item => {
                const promise = getFile(item).then(data => { // 下载文件, 并存成ArrayBuffer对象
                    const arr_name = item.split("/")
                    const file_name = arr_name[arr_name.length - 1] // 获取文件名
                    zip.file(file_name, data, { binary: true }) // 逐个添加文件
                    cache[file_name] = data
                })
                promises.push(promise)
            })

            Promise.all(promises).then(() => {
                zip.generateAsync({type:"blob"}).then(content => { // 生成二进制流
                    FileSaver.saveAs(content, "download.zip") // 利用file-saver保存文件
                })
            })
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
    .el-footer {
    color: #333;
    text-align: center;
    line-height: 60px;
  }
</style>
