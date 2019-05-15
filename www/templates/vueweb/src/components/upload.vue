<template>
  <el-container>
    <el-header class="header" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
      <span style="font-family:华文楷体">光学乐谱识别系统</span>
      <button class="el-icon-circle-close-outline exitButt" style="font-family:华文楷体;background-color: white"@click="loginOutPC()">&nbsp;退出系统</button>
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
                  action="https://jsonplaceholder.typicode.com/posts/"
                  :on-preview="handlePreview"
                  :on-change="handleChange"
                  :on-remove="handleRemove"
                  :file-list="fileList"
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
    export default {
        data() {
            return {
                fileList: [],
                file:[],
            }
        },
        created(){

        },

        methods: {
            handleChange(file){
                this.file=file;
                console.log(file);
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {
                console.log(file);
            },
            submitUpload() {
                this.$refs.upload.submit();
                var that=this;
                console.log(this.file);
                let formData = new FormData();
                formData.append("file", this.file);
                this.$axios.post('/', formData)
                    .then(function (response) {
                        alert("上传成功");
                        //that.$router.push('/emptyPage');
                        that.dialogVisible=false;
                    })
                    .catch(function (error) {
                        alert("上传失败，请检查文件格式并重新上传");
                        console.log(error);
                        that.dialogVisible=false;
                    });
            },
            analysis(){

            },
            refresh() {
                this.$refs.upload.clearFiles();
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

</style>

