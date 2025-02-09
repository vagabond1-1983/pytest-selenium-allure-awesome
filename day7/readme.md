# 第七天
1. pet 网站登录
编写 Base 类，进行登录。登录中碰到 login 按钮是 input，先以为 click 方式不行，排查后发现是定位方式不对。
2. 框架优化
- conftest.py放到 day7的主目录下，这样 day7/pet 目录下的 case 脚本则都会加载 conftest。如果放到某个 case 目录下，则只会在此目录下加载
- 修改 ROOT 目录到项目根目录
- 修改日志和截图路径，修改为项目根目录下的 logs 和 screenshots
- 增加 log 输出到控制台方便调试场景
3. 完成单个商品的下单流程
参见：order_single_good
过程记录点&框架优化：
- before_find增加显式等待，这样就无需在 find_element时调用 WebDriverWait，降低代码复杂度
- 本来想在 before_click也增加显式等待，但是传入参数是 element，获取不到 by 和 value。现在方式是放入到 self 中携带，待优化
- after_click后的 element 可能不稳定，已经不存在了。所以不要操作这个 element 获取属性值等。这个让我调试了很久。
总结：框架优化点在元素出现前的等待和click操作记录等
- 查找元素用 css 还是 xpath，这个还待深入体会。目前看在没有 jquery 的情况下，xpath 比 css 更强大些。特别是通过文本找元素上。