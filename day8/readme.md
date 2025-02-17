# 第八天
改造 log 方式，用全局 logger 方式，这样每个类都有一致的输出方式。
参见：day8/utils/log.py，使用 loguru框架声明一个全局 logger。其他模块引用即可。
另外将 config.json变更为.env，做全局环境配置用。这样配置开关可以从 os.env中轻松读取。另外跟 CI 结合后可以动态配置。