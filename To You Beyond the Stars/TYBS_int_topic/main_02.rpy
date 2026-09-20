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