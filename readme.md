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
1. 搭建 jenkins，CI 执行--不成功
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

## 第五天
1. CI运行
用镜像方式构建出jenkins slave 碰到了阻碍。申请的 ECS 性能差，调试慢。
先用本机搭建一个 jenkins，然后本地创建 job 运行。先不走镜像方式。
参看 Jenkinsfile，在配置过程中碰到了 conda 环境问题。有点懂了，每个 sh 都是独立的，环境切换后需要直接执行 python 脚本。

## 第六天
1. 框架在关键点截图
2. 失败截图

## 第七天
- 用 mybatis 的 pet 靶场，替换百度的例子：https://petstore.octoperf.com/actions/Catalog.action
1. 实现登录--done
2. 实现下单流程--done

## 第八天
1. 改造 log 方式，用全局 logger 方式，这样每个类都有一致的输出方式。配置从os.env中获取

## 第九天
- 画出框架架构图--done
- jenkinsfile更新，跑 day8--done

# 待办
- 操作放到 json，关键字驱动
- pytest特性学习、listener 等高级技巧
- jenkins slave 镜像方式运行脚本