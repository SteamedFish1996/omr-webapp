<template>
  <el-container>
    <el-header class="header" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
      <span style="font-family:华文楷体">光学乐谱识别系统</span>
      <button class="el-icon-circle-close-outline exitButt" style="font-family:华文楷体;background-color: white" @click="goback()">&nbsp;退出系统</button>
    </el-header>
    <br>
    <el-main>
      <el-header class="header" style="font-family:华文楷体;font-size:120%;font-weight:bold;width:100%;background-color:white;border-top:1px solid #dfdfdf;color:#409dfe;">上传文件</el-header>
      <div>
        <div style="font-family: 黑体">
          <el-upload
                  class="upload-demo"
                  ref="upload"
                  drag
                  :action="imgUrl"
                  :on-success="handleAvatarSuccess"
                  :on-change="handleChange"
                  :on-remove="handleRemove"
                  :file-list="fileList"
                  :limit="1"
                  :on-exceed="handleExceed"
                  :auto-upload="false">
            <i class="el-icon-upload"></i>
            <br>
            <div class="el-upload__text">将文件拖到此处，或<em>点击选择文件</em></div>
            <div slot="tip" class="el-upload__tip" style="color:red">只能上传xxx(格式)文件，且不超过500kb</div>
          </el-upload>
        </div>
        <br>
        <div style="font-family: 黑体">
          <el-button style="margin-left: 10px;" size="small"  @click="refresh">重置</el-button>
          <el-button style="margin-left: 10px;" type="primary" size="small"  @click="submitUpload">上传</el-button>
          <el-button style="margin-left: 10px;" type="success" size="small"  @click="analysis">解析</el-button>
        </div>
        <br>
      </div>
    </el-main>
  </el-container>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                imgUrl:"http://127.0.0.1:5000/upload/",
                fileList: [],
                file:[],
                iUrl: '',
                response:[],
                length:0,
            }
        },
        created(){

        },

        methods: {
          goback(){
              this.$router.push({path:'/'})
          },
          handleAvatarSuccess(res, file) {
            this.iUrl = URL.createObjectURL(file.raw);
            console.log(this.iUrl);
             },
          handleChange(file,files){
            this.file=file;
            this.length=files.length;
            this.response=file.response;
            if(this.response){
              if(this.response.status=="200"){
                alert("上传成功");
                that.dialogVisible=false;
              }else{
                alert("上传失败，请检查文件格式并重新上传");
                that.dialogVisible=false;
              } 
              }
            },
            handleRemove(file, fileList) {
              this.length=0;
              this.response=[];
            },
            handleExceed(files, fileList) {this.$message.warning(`当前文件列表中已有文件，请重置后再上传`);},
            submitUpload() {
              console.log(this.length);
              if(this.length>0){
              this.$refs.upload.submit();
              var that=this;
              let formData = new FormData();
              formData.append("file", this.file);
              }
              else{
                alert("您还未选择文件");
              }
            },
            analysis(){
              if(this.response){
                console.log(this.iUrl);
                  if(this.response.status=="200"){
                    this.$router.push({path:'/ana',
                    query:{
                      response:this.response,
                      iUrl:this.iUrl,
                      }
                      })
              }else{
                alert("您还未上传文件");
                this.$refs.upload.clearFiles();
                this.response=[];
                that.dialogVisible=false;
              }
                }
             
            },
            refresh() {
                this.$refs.upload.clearFiles();
                this.response=[];
            },
        },
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

