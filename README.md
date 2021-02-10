# nuaa-health
南航健康打卡脚本

### 配置步骤

+ 下载ChromeDriver

  + 在Chrome浏览器地址栏中输入`chrome://version/`查看版本号
  + 根据版本号[下载](https://chromedriver.chromium.org/downloads)对应的`chromedriver.exe`，并将其放置在Chrome的安装路径`C:\Program Files (x86)\Google\Chrome\Application`下，如已存在则替换

+ 安装依赖包

  + ```
    pip install selenium
    ```

+ 克隆仓库到本地并修改配置

  + ```
    git clone git@github.com:Caleb411/nuaa-health.git
    ```

  + 修改`config.json`中的学号，密码，[Server酱](http://sc.ftqq.com/3.version)秘钥（用于微信推送打卡是否成功）

+ 直接运行脚本或创建定时任务

  + ```
    python daka.py
    ```

  + [windows中怎么添加定时任务](https://www.cnblogs.com/gcgc/p/11594467.html)

![nuaa-health](https://cdn.jsdelivr.net/gh/Caleb411/image@main/20201223/nuaa-health.jpg)

