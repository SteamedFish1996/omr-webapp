<template>
    <div :style="back">
      <div class="header">
        <span style="font-family:华文楷体">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;光学乐谱识别系统</span>
      </div>
      <el-card>
        <span class="loginSpan">登录</span>
        <el-form :model="LoginData" :rules="rules">
          <el-form-item prop="username" label="用户名">
            <el-input class="loginInput" v-model="LoginData.username" placeholder="请输入用户名" clearable></el-input>
          </el-form-item>
          <el-form-item prop="password" label="密码">
            <el-input class="loginInput" type="password" v-model="LoginData.password" placeholder="请输入密码" clearable></el-input>
          </el-form-item>
          <div style="float:right">
          <el-link type="primary">还没有账号？</el-link>
          |
           <el-link type="primary">忘记密码？</el-link>
           </div>
          <el-button class="buttomButt" type="primary" @click="login()">登录</el-button>
        </el-form>
      
      </el-card>
    </div>
</template>

<script>
export default {
  name: 'login',
  data(){
          return{
          back:{
            backgroundImage: "url(" + require("../assets/background2.png") + ")",
            backgroundRepeat: "no-repeat",
            backgroundSize: "350px auto",
            backgroundPosition:"220px 100px"
          },
            LoginData:{
              username:'',
              password:'',
              identity:'2',
            },
            rules:{
              username:[
                { required:true ,message:'用户名不能为空！',trigger: 'blur' }
              ],
              password:[
                { required:true ,message:'密码不能为空！',trigger: 'blur'}
              ]
            },
          }
      },
      methods:{
          login(){
            var _this=this;
            this.$axios({
              method:'post',
              url:'http://127.0.0.1:5000/add',
              data:{
                account:this.LoginData.username,
                password:this.LoginData.password,
              }
            }).then(function (response) {
              _this.$store.commit("SET_AUTH",response);
                  alert("登录成功！");
                  _this.$router.push("/ana");
              })
              .catch(error=>{console.log(error);});
          }
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
  .el-card{
    margin: 100px 800px;
    height: 360px;
    width: 320px;
    padding: 0px 20px;

  }
  .loginSpan{
    height: 20px;
    font-size: 20px;
    color: #606266;
  }
  .el-form{
    margin-top: 20px;
  }
  .el-form-item{
    magin:5px 0;
  }
  .buttomButt{
    height: 40px;
    width: 100%;
    font-size: 18px;
    margin-top: 10px;
  }
  .el-radio__label{
    font-size: 25px;
  }
  .loginInput .el-input__inner{
    height: 60px;
    font-size:20px;
    /*margin: 30px 0px 10px 0px;*/
  }
</style>
