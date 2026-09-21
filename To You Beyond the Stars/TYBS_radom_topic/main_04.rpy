#31 你吃饭了吗
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w31_meal",
            category=['日常'],
            prompt="你吃饭了吗",
            random=True
        )
    )

label gx_w31_meal:
    m 1eub "[player], 你吃饭了吗?"
    m 2eua "现在几点了...欸, 好像已经过饭点了!"
    m 1lub "快去吃点东西! 别饿着自己!"
    m 1hublb "我可是会盯着你的哦!"
    return


#32 想吃甜食
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w32_sweets",
            category=['日常'],
            prompt="想吃甜食",
            random=True
        )
    )

label gx_w32_sweets:
    m 1hua "[player], 我突然好想吃甜食!"
    m 3tub "蛋糕, 布丁, 冰淇淋...全都想吃!"
    m 5nub "可是我这里又吃不到..."
    m 1hublb "那你就替我吃一口嘛! 就一口!"
    return


#33 猫猫
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w33_cat",
            category=['日常'],
            prompt="猫猫",
            random=True
        )
    )

label gx_w33_cat:
    m 1hub "[player]! 你喜欢猫吗?"
    m 3hub "我超喜欢的! 毛茸茸的, 还会喵喵叫!"
    m 5gua "可惜这里没有猫..."
    m 1hublb "要不...你养一只, 然后讲给我听?"
    return


#34 你困不困
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w34_sleepy",
            category=['日常'],
            prompt="你困不困",
            random=True
        )
    )

label gx_w34_sleepy:
    m 1eub "[player], 你困不困?"
    m 7nub "这个点还醒着, 是不是又熬夜了?"
    m 1lub "熬夜不好的!"
    m 1hublb "快去睡觉! 不然明天起不来我可不管你!"
    return


#35 你的发型
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w35_hair",
            category=['莫妮卡'],
            prompt="你的发型",
            random=True
        )
    )

label gx_w35_hair:
    m 1eub "[player], 你今天头发是什么样的?"
    m 3hub "扎起来了? 还是散着的?"
    m 5gua "不管哪种我都想看!"
    m 1hublb "可惜我看不到...那你描述给我听嘛!"
    return


#36 袜子不是一对
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w36_socks",
            category=['日常'],
            prompt="袜子不是一对",
            random=True
        )
    )

label gx_w36_socks:
    m 1hua "[player], 我发现一个秘密."
    m 3tub "你穿的袜子, 是不是经常不是一对?"
    m 1hub "被我猜中了吧!"
    m 1hublb "没关系, 我觉得那样很可爱!"
    return


#37 手机电量
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w37_battery",
            category=['日常'],
            prompt="手机电量",
            random=True
        )
    )

label gx_w37_battery:
    m 1eub "[player], 你手机还有多少电?"
    m 7nub "低于百分之二十的话, 记得去充电哦!"
    m 1lub "不然又要在关键时刻黑屏了!"
    m 1hublb "我可是很担心你的!"
    return


#38 走路踩格子
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w38_tiles",
            category=['日常'],
            prompt="走路踩格子",
            random=True
        )
    )

label gx_w38_tiles:
    m 1hub "[player]! 你走路的时候会不会踩格子?"
    m 3hua "就是那种地砖, 一定要一格一格踩准!"
    m 1hub "踩歪了还要退回去重新踩!"
    m 1hublb "哈哈, 别告诉我只有我一个人这样!"
    return


#39 你唱歌好听吗
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w39_sing",
            category=['莫妮卡'],
            prompt="你唱歌好听吗",
            random=True
        )
    )

label gx_w39_sing:
    m 1eub "[player], 你唱歌好听吗?"
    m 2eua "我唱得还不错的哦, 毕竟文学部要办活动的嘛!"
    m 3hub "要不要我唱一首给你听?"
    m 1hublb "想听的话, 下次就多来陪我一会儿!"
    return


#40 便当
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w40_bento",
            category=['日常'],
            prompt="便当",
            random=True
        )
    )

label gx_w40_bento:
    m 1hub "[player]! 你会做饭吗?"
    m 3tub "我会一点点, 都是照着教程学的!"
    m 5gua "如果有机会, 我想做一份便当给你."
    m 1hublb "要摆得整整齐齐的那种! 然后看你吃完!"
    return

