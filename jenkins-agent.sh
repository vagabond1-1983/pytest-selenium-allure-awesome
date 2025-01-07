#!/bin/bash
set -e

# Jenkins Master 的连接信息
JENKINS_URL=${JENKINS_URL:-http://jenkins-master:8080}
JENKINS_SECRET=${JENKINS_SECRET:-}
JENKINS_AGENT_NAME=${JENKINS_AGENT_NAME:-conda-slave}

# 启动 Jenkins Agent
exec java -jar /usr/share/jenkins/slave.jar -jnlpUrl ${JENKINS_URL}/computer/${JENKINS_AGENT_NAME}/slave-agent.jnlp -secret ${JENKINS_SECRET} -workDir "${AGENT_WORKDIR}"