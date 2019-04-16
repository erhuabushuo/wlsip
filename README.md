## 安装

    yum install sipp # apt install sipp
    python3 setup.py install


## 参数

    $ wlsip --help
    Usage: wlsip [OPTIONS] LOCALHOST SERVERHOST

    Options:
    --scenario [register|uas|uac]
    --max_call_count INTEGER
    --max_currency INTEGER
    --cps INTEGER
    --help                         Show this message and exit.

* scenario: 可选参数register,uas, uac
* max_call_count: 最大呼叫数
* max_currency: 最大并发数
* cps: 每秒呼叫数
* LOCALHOST: 本地网口地址
* SERVERHOST: 服务器地址，47.96.84.248:518

## 用例

### 注册

100并发进行注册

    wlsip --scenario register --max_call_count 100 --max_currency 100 --cps 100 192.168.0.102 47.96.84.248:518

### 呼叫

被叫注册上去

    wlsip --scenario uas --max_call_count 100 --max_currency 100 --cps 100 192.168.0.102 47.96.84.248:518

主叫发起呼叫

    wlsip --scenario uac --max_call_count 100 --max_currency 100 --cps 100 192.168.0.102 47.96.84.248:518


## 测试结果


    ----------------------------- Statistics Screen ------- [1-9]: Change Screen --
    Start Time             | 2019-04-16	17:15:55:902	1555406155.902319            
    Last Reset Time        | 2019-04-16	17:15:56:951	1555406156.951196            
    Current Time           | 2019-04-16	17:15:56:951	1555406156.951264            
    -------------------------+---------------------------+--------------------------
    Counter Name           | Periodic value            | Cumulative value
    -------------------------+---------------------------+--------------------------
    Elapsed Time           | 00:00:00:000              | 00:00:01:048 # 总耗时            
    Call Rate              |    0.000 cps              |   47.710 cps # cps：每秒呼叫数            
    -------------------------+---------------------------+--------------------------
    Incoming call created  |        0                  |        0     # 向内发起的请求数         
    OutGoing call created  |        0                  |       50     # 向外发起的请求数           
    Total Call created     |                           |       50     # 总请求数            
    Current Call           |        0                  |                          
    -------------------------+---------------------------+--------------------------
    Successful call        |        0                  |       50     # 成功呼叫数            
    Failed call            |        0                  |        0     # 失败呼叫数            
    -------------------------+---------------------------+--------------------------
    Call Length            | 00:00:00:000              | 00:00:00:045             
    ------------------------------ Test Terminated --------------------------------

执行完后会在当前目录生成周期性详细的结果统计：**[register|uac|uas]_stat.csv**，其字段意义如下：

     StartTime:脚本开始运行的时间日期
     LastResetTime: 最后生成统计数据的时间
     CurrentTime:当前统计的日期和时间
     ElapsTime:已运行的时间
     CallRate:呼叫速率,每秒
     IncomingCall:呼入的呼叫数量
     OutcomingCall:呼出的呼叫数量
     TotalCallCreated:总共生成的呼叫个数
     CurrentCall:正在进行的呼叫
     SuccessfulCall:成功的呼叫
     FailedCall:失败的呼叫
     FailedCannotSendMessage:不能发送消息的呼叫(传输层问题)
     FailedMaxUDPRetrans:重试达到最大次数导致的失败呼叫
     FailedUnexpectedMessage:未如脚本所料的错误呼叫
     FailedRegexpDoesntMatch:由于正则表达式应该匹配而没有匹配而造成失败的呼叫
     FailedRegexpShouldntMatch:由于正则表达式不应该匹配而匹配造成失败的呼叫
     FailedRegexpHdrNotFound:由于正则表达式没有找到匹配项导致的失败的呼叫
     FailedOutboundCongestion:由于 TCP 拥塞而导致失败的呼叫
     FailedTimeoutOnRecv:由于接收超时而导致失败的呼叫
     FailedTimeoutOnSend:由于发送超时而导致失败的呼叫
     OutOfCallMsgs:不能与存在的呼叫匹配的消息个数
     Retransmissions:重传输的个数
     AutoAnswered:自动应答并回复 200ok 的消息的个数