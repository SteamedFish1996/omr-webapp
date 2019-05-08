# 静态文件
动态 web 应用也会需要静态文件，通常是 CSS 和 JavaScript 文件。理想状况下， 你已经配置好 Web 服务器来提供静态文件，但是在开发中，Flask 也可以做到。 只要在你的包中或是模块的所在目录中创建一个名为 static 的文件夹，在应用中使用 /static 即可访问。

给静态文件生成 URL ，使用特殊的 'static' 端点名:

    url_for('static', filename='style.css')

这个文件应该存储在文件系统上的 static/style.css