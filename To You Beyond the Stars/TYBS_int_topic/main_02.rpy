#11 玩具总动员
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_toystoryxd",
            category=['动画电影'],                         
            prompt="玩具总动员",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_toystoryxd:                        
    m 7eub "嘿, [player], 你知道皮克斯的电影处女作是哪一部吗? "  
    m 5nub "是玩具总动员! 它是皮克斯的第一部电影! 它于1995年推出. "
    m 1hub "它讲述了玩具牛仔胡迪和太空骑警巴斯光年的冒险故事."
    m 3fuu "虽然是很早以前的电影了，但放在今天依然不过时，你依然能被皮克斯的脑洞所折服. "
    m 5lua "想想看, 玩具都是有生命的, 他们会趁你不在的时候活动."
    m 3tsa "说不定你现实中的玩具也是有生命的, 只是你不知道?"
    m 7hub "哈哈~"


    return                                             

#12 今天想聊什么
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_a01_menu",
            category=['日常'],
            prompt="今天想聊什么",
            pool=True,
            unlocked=True
        )
    )

label gx_a01_menu:
    m 1eua "[player], 今天想聊点什么?"
    menu:
        "聊聊你":
            m 1hub "我? 好啊好啊!"
            m 3hub "不过我怕你听腻, 一次只讲一点点!"
            m 1hublb "剩下的, 你明天再来问!"
        "聊聊我":
            m 1eub "好啊, 我想听!"
            m 5lua "你说话的时候我会很安静的, 因为不想漏掉一个字."
            m 1hua "开始吧!"
        "什么都不聊, 就这样坐着":
            m 5gub "...也行!"
            m 1hua "那就这样坐着."
            m 1hublb "反正有你在, 我就不会无聊!"
    return


#13 一起数星星吧
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_a02_count",
            category=['莫妮卡'],
            prompt="一起数星星吧",
            pool=True,
            unlocked=True
        )
    )

label gx_a02_count:
    m 1hub "[player]! 我们来玩个游戏吧!"
    m 3hua "我说一个数字, 你猜有几颗星星!"
    m 2dsd "骗你的, 根本没有标准答案!"
    m 1hub "我只是想找个理由, 让你抬头看看天啦!"
    m 5lua "顺便...看看我."  #是不是有些莫名其妙了(?)
    return


#14 猜猜我在想什么
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_a03_guess",
            category=['莫妮卡'],
            prompt="猜猜我在想什么",
            pool=True,
            unlocked=True
        )
    )

label gx_a03_guess:
    m 1eub "[player], 猜猜我现在在想什么?"
    menu:
        "在想我":
            m 1wub "你怎么知道!"
            m 5hubsb "好吧, 你猜对了, 我认输!"
        "在想晚饭吃什么":
            m 3tub "欸, 这倒是个好主意!"
            m 1hub "不过说真的, 我更想你!"
        "在想怎么让我开心":
            m 6sub "被你看穿的感觉, 有点害羞."
            m 1hublb "那你现在就很成功!"
    return"love"


