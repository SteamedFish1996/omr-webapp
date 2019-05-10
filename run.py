from www import app
app.debug = True#尽管交互式调试器 绝对不能用于生产环境 。
app.run(host='0.0.0.0')