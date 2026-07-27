init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_test_02",     
            category=['测试话题(open world)'],                         
            prompt="重置湖边变量",                             
            unlocked=True,                             
            pool=True                                  
        )
    )



label ow_test_02:
    "确定要重置湖边记录?{nw}"
    menu:
        "确定要重置湖边记录?{fast}"
        "是":
            jump return_default_lake

        "否":
            return

label return_default_lake:
    $ persistent.find_new = 0
    "变量已重置"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_test_03",     
            category=['测试话题(open world)'],                         
            prompt="增加湖边变量",                             
            unlocked=True,                             
            pool=True                                  
        )
    )





label ow_test_03:
    "确定要开启湖边记录?{nw}"
    menu:
        "确定要开启湖边记录?{fast}"
        "是":
            jump plus_default_lake

        "否":
            return

label plus_default_lake:
    $ persistent.find_new += 1
    "变量已实现"
    return
