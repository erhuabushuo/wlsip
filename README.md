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