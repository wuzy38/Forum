# Forum
基于Django和MySQL开发的论坛管理系统

## 目录 
-Forum  
　-urls.py　　　　　　　　　　&ensp; 访问路径的设计，处理HTML文件和url路径之间的关系  
-app　　　　　　　　　　　　　应用，account和forumapp  
　-account　　　　　　　　　 　关于账号的设计  
　　-views.py　　　　　　　　　账号视图，对于账号逻辑的设计。包括了注册，登录，显示用户信息  
　-forumapp　　　　　　　　　 关于论坛的设计  
　　-views.py　　　　　　　　　论坛视图，对于论坛逻辑的设计。包括了主界面，板块，帖子  
-SQL　　　　　　　　　　　　　数据库，使用MySQL数据库，使用pymysql建立连接访问mysql数据库forum  
　-sql.py　　　　　　　　　　　提供访问数据的接口，有插入用户信息，获取用户信息的接口。  
　-论坛数据库关系图.png　　 　   forum数据库的关系模型   
-HTML  
　-templates　　　　　　　　　HTML文件的模板，根据应用的views.py文件传过来的数据，生成具体的HTML文件  
　　-home.html　　　　　　　　主界面的模板  
　　-plate.html　　　 　　　　　 板块的模板  
　　-theme.html　　　　　　　　帖子的模板  
　　-register.html　　　 　　 　　用户注册的模板  
　　-login.html　　　　 　 　　　用户登录的模板  
　　-person_imformation.html 　 个人信息的模板  
-实验报告  
　-db_ex8.pdf　　 　　 　　　　更具体的设计过程  