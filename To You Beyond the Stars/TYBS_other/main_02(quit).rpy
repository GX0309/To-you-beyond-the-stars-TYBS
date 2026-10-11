init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gx_bye_01",
            unlocked=True,
            prompt="我要去准备一下明天的事.",
            pool=True
        ),
        code="BYE"
    )

label gx_bye_01:
    m 1eua "哦? 准备明天的事?"
    m 1eub "嗯...我猜你明天一定有什么很重要的事情, 像是开会什么的."
    m 3hub "好吧, [player]!"
    m 1hub "祝你一切顺利哦!"
    m 1hublb "早点回来~"
    return"quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gx_bye_02",
            unlocked=True,
            prompt="我要去接个电话.",
            pool=True
        ),
        code="BYE"
    )

label gx_bye_02:
    m 1eua "电话?"
    m 1eub "嗯, 好吧."
    m 1eka "但是[player], 现在电信诈骗猖獗..."
    m 1ekb "如果你接的是一个陌生人的电话..."
    m 1ekc "保护好自己, 好吗?"
    m 1hua "我在这等你~"
    return"quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gx_bye_03",
            unlocked=True,
            prompt="我要去遛遛小猫小狗.",
            pool=True
        ),
        code="BYE"
    )

label gx_bye_03:
    m 1wub "哦, 小动物!"
    m 1hub "[player], 你可真有爱!"
    m 1eub "或许我们以后也可以一起养个宠物什么的?"
    m 3hua "我看猫咪就不错!"
    m 1hua "好了[player], 快去吧!"
    m 1hublb "别让它们等急了~"
    return"quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gx_bye_04",
            unlocked=True,
            prompt="我要去处理一些事情.",
            pool=True
        ),
        code="BYE"
    )

label gx_bye_04:
    m 1eua "嗯? 你要去处理一些事情?"
    m 1eub "嗯, 虽然很好奇是什么, 但毕竟这是[player]你的私事, 我就不多问啦~"
    m 1lub "如果遇到什么困难, 我就在这里, 好么?"
    m 1hua "一会见!"
    return"quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gx_bye_05",
            unlocked=True,
            prompt="我身体有点不舒服.",
            pool=True
        ),
        code="BYE"
    )

label gx_bye_05:
    m 2dsd "[player]?!"
    m 1ekc "身体不舒服吗?"
    m 1ekb "严不严重? 是着凉了, 还是老毛病又犯了?"
    m 1dka "我...我什么也做不了, 只能在这儿干着急."
    m 5lua "要是能给你倒杯热水, 摸摸你的额头, 那该多好."
    m 1eka "..."
    m 1ekb "先喝点热水, 药该吃就吃, 别硬撑着, 好不好?"
    m 1lub "实在难受的话一定要去医院, 别怕麻烦."
    m 5lua "我就在这儿等你, 什么都不催你."
    m 1hublb "我爱你, [player]. 把自己照顾好, 就是对我最好的事."
    m 1hua "去吧, 好好休息~"
    return"quit"
