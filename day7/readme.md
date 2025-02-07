# 第七天
1. pet 网站登录
编写 Base 类，进行登录。登录中碰到 login 按钮是 input，先以为 click 方式不行，排查后发现是定位方式不对。
2. 框架优化
- conftest.py放到 day7的主目录下，这样 day7/pet 目录下的 case 脚本则都会加载 conftest。如果放到某个 case 目录下，则只会在此目录下加载
- 修改 ROOT 目录到项目根目录
- 修改日志和截图路径，修改为项目根目录下的 logs 和 screenshots
- 增加 log 输出到控制台方便调试场景