# 使用官方 Miniconda 镜像
FROM datadevops/conda-jenkins-slave:latest

# 复制 Conda 环境文件
COPY environment.yml /tmp/environment.yml

# 创建 Conda 环境
RUN conda env create -f /tmp/environment.yml

# 激活环境并设置默认命令
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

# 设置工作目录
WORKDIR /app

# 下载 Jenkins Agent（Slave）工具
ARG JENKINS_AGENT_VERSION=4.11
RUN mkdir -p /usr/share/jenkins && \
    curl -fsSL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${JENKINS_AGENT_VERSION}/remoting-${JENKINS_AGENT_VERSION}.jar -o /usr/share/jenkins/slave.jar

# 创建 Jenkins 用户
RUN useradd -m -d /home/jenkins -s /bin/bash jenkins && \
    chown -R jenkins:jenkins /app

# 设置 Jenkins 用户的环境变量
USER jenkins
ENV AGENT_WORKDIR=/home/jenkins/agent

# 创建 Jenkins Agent 工作目录
RUN mkdir -p ${AGENT_WORKDIR}

# 暴露 Jenkins Agent 端口（可选）
EXPOSE 50000

# 设置 Jenkins Agent 启动脚本
COPY jenkins-agent.sh /usr/local/bin/jenkins-agent.sh
RUN chmod +x /usr/local/bin/jenkins-agent.sh

# 设置默认命令为启动 Jenkins Agent
ENTRYPOINT ["/usr/local/bin/jenkins-agent.sh"]