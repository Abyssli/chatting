'''
    群聊聊天室思路分析
        1.技术点的确认
            *转发模型, 客户端-->服务端-->转发给其他客户端
            *网络模型:UDP通信
            *保存用户信息[(name,addr),()]  {name:addr}
            *收发关系处理:采用多进程分别进行收发操作

        2.结构设计
            *采用什么样的封装结构:函数
            *编写一个功能,测试一个功能
            *注意注释和结构的设计

        3.分析功能模块,制定具体编写流程
            *搭建网络连接(通信连接作为一个较高的优先级,优先制定)

            *进入聊天室
                客户端:
                    1.输入姓名
                    2.将姓名发送给服务器
                    3.接受返回的结果
                    4.如果不允许则重复输入姓名

                服务端:
                    1.接受姓名
                    2.判断姓名是否存在
                    3.将结果给客户端
                    4.如果允许进入聊天室增加用户信息
                    5.通知其他用户

            *聊天
                客户端:*创建新的进程
                      *一个进程循环发送消息
                      *一个进程循环接受消息
                服务端:
                      *接受请求,判断请求类型
                      *将消息转发给其他用户

            *退出聊天室:
                    客户端:
                      *输入quit或者ctrl-c退出
                      *将请求发送给服务端
                      *结束进程
                      *客户端收到EXIT退出进程
                    服务端:
                      *接受消息
                      *将退出消息告知其他人
                      *给该用户发送"EXIT"
                      *删除用户

            *管理员消息

        4.协议
            *如果允许进入聊天室,那么服务端发送"OK"给客户端
            *如果不允许进入聊天室,服务端发送不允许的原因
            *请求类别:
                L --> 进入聊天室
                C --> 聊天信息
                Q --> 退出聊天室
            *用户存储结构:字典{name:addr}
            *客户端如果输入quit或者ctrl-c,点击esc表示退出
'''