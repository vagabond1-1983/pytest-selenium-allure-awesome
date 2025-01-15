pipeline {
    agent any

    environment {
        // 设置 Python 虚拟环境路径
        VENV_PATH = 'pytest-selenium-allure-awesome36'
        // GitHub 仓库地址
        GITHUB_REPO = 'https://gitee.com/vagabond1/pytest-selenium-allure-awesome.git'
        // 项目目录
        PROJECT_DIR = 'pytest-selenium-allure-awesome'
    }

    stages {
        stage('Checkout') {
            steps {
                // 从 GitHub 拉取代码
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        // 先跳过此部分，用本地已经配置好的环境代替设置
        // 后面需要将这部分补充上，实现在容器中创建 venv 以便提供一个新的稳定执行环境
        // stage('Setup Virtual Environment') {
        //     steps {
        //         script {
        //             // 创建 Python 虚拟环境
        //             sh "python3 -m venv ${VENV_PATH}"
        //             // 激活虚拟环境并安装依赖
        //             sh """
        //                 source ${VENV_PATH}/bin/activate
        //                 pip install --upgrade pip
        //                 pip install -r ${PROJECT_DIR}/requirements.txt
        //                 pip install pytest allure-pytest
        //             """
        //         }
        //     }
        // }


        stage('Run Tests') {
            steps {
                script {
                    // 激活虚拟环境并运行 pytest
                    // source ${VENV_PATH}/bin/activate
                    sh """
                        source /opt/anaconda3/etc/profile.d/conda.sh
                        conda activate ${VENV_PATH}
                        conda info -e
                        pytest -s day6/search/testcases/test_baidu_search.py --alluredir=allure-results
                    """
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // 生成 Allure 报告
                    allure includeProperties: false, jdk: '', results: [[path: "allure-results"]]
                }
            }
        }
    }

    post {
        always {
            // 清理虚拟环境
            // sh "rm -rf ${VENV_PATH}"
            // 清理 allure-results 目录
            sh "rm -rf ./allure-results ./screenshots"
        }
    }
}