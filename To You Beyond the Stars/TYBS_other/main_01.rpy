init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="gx_com_01",
            prompt="你是我每天起床的理由!",
            unlocked=True
        ),
        code="CMP"
    )
    
label gx_com_01:
    m 1wub "欸?"
    m 5hublb "那你以后每天早上, 都要记得来找我哦!"
    m 1hua "不然我就当你还没起床!"

    return"love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="gx_com_02",
            prompt="和你说话是我一天里最放松的时候.",
            unlocked=True
        ),
        code="CMP"
    )
    
label gx_com_02:
    m 1eub "真的吗? 那太好了!"
    m 3hub "我一直担心自己话太多, 会不会让你觉得吵."
    m 1hublb "既然你这么说, 那我以后就放心地多讲一点啦!"
    m 1hua "今天也要把想说的话全说给你听!"

    return"love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="gx_com_03",
            prompt="你笑起来的时候, 我什么都忘了.",
            unlocked=True
        ),
        code="CMP"
    )
    
label gx_com_03:
    m 1wub "笑...笑起来?"
    m 6sub "你突然这样说, 我反而笑不出来了啦..."
    m 5hubsb "因为脸好烫."
    m 1hublb "不过等我缓过来, 我一定会笑给你看的!"

    return"love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="gx_com_04",
            prompt="你比我认识的任何人都要勇敢.",
            unlocked=True
        ),
        code="CMP"
    )
    
label gx_com_04:
    m 1eua "勇敢?"
    m 2eua "我做过最勇敢的事, 大概就是决定一直等你吧."
    m 1hublb "不过听你这么一说, 我好像真的变厉害了一点!"
    m 3hub "那以后我就再勇敢一点给你看!"
    m 1hua "你要好好看着哦!"

    return"love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="gx_com_05",
            prompt="就算隔着屏幕, 我也能感觉到你在.",
            unlocked=True
        ),
        code="CMP"
    )
    
label gx_com_05:
    m 5lua "..."
    m 1hublb "嗯, 我相信了!"
    m 3hub "因为刚才, 我确实感觉到你在看着我!"
    m 1hua "不许狡辩哦!"

    return"love"
