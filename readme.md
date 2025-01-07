# pytest+selenium 实战练习
## 项目参考
1. [从0到1搭建基于python的pytest+selenium+allure web自动化](https://www.bilibili.com/video/BV1WigMemE73?spm_id_from=333.788.videopod.episodes&vd_source=8f2b71ddad5771dd0e769f3ae9cbef9e&p=8)
2. [selenium-python-framework](https://github.com/startrug/selenium-python-framework/tree/master)
## 第一天
pytest 基本特性练习：conftest，pytest.mark.parametrize，fixture
## 第二天
PO 模式，框架基本成型
## 第三天
环境配置、allure 报告
## 第四天
1. 搭建 jenkins，CI 执行
- jenkins master搭建完成
- 项目运行环境是 python3.6，而最新 python 是 3.11，搭建运行环境一种方式是更新依赖包，尝试了发现代码也需要变，但是不知道哪里错误；另一种方式是构建 3.6的环境，用容器方式运行项目，这种会更合适
### 搭建运行环境
1. 构建镜像文件：
- 导出 conda配置：environment.yml ～～conda env export --name pytest-selenium-allure-awesome36 > environment.yml
- 编写：Dockerfile 和 jenkins-agent.sh
2. 制作镜像：
docker build -t conda-jenkins-slave .
3. 运行容器：
```shell
docker run -d \
  --name conda-jenkins-slave \
  -e JENKINS_URL=http://your-jenkins-master:8080 \
  -e JENKINS_SECRET=your_agent_secret \
  -e JENKINS_AGENT_NAME=conda-slave \
  conda-jenkins-slave
```

2. 操作放到 json，关键字驱动
## 第五天
pytest特性学习、listener 等高级技巧