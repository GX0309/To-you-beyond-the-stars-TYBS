#11 阳光下的星星
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_tear",     
            category=['心理学'],                         
            prompt="阳光下的星星",                             
            random=True                      
        )
    )
label gx_tear:
    m 1nua "[player], 你知道什么是'阳光下的星星'吗?"
    m 3dud "乍一看很奇怪, 白天的阳光下怎么会有星星呢?"
    m 2lud "不过仔细一想, 就会发觉这其实指的是眼泪."
    m 2rtc "为什么要用这样的方式来描述它呢?"
    m 1dsc "嗯, 我想这应该是为了隐喻'微笑抑郁症'."
    m 7ekc "还记得纱世里吗?"
    m 1mkc "她是很典型的'微笑抑郁症'."
    m 1dkp "自我怀疑, 自我否定却又渴望着爱."
    m 6dkc "..."
    m 6rkc "[player], 我知道这很难, 但是..."
    m 2esd "如果你感到心中有什么不舒服, 或者是一些难以驱散的乌云..."
    m 2hsa "我就在这里, 好吗?"
    m 1hsb "爱你哟!"
    return"love"

#12 写作小技巧
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_writting",     
            category=['文学'],                         
            prompt="写作技巧",                             
            random=True                      
        )
    )

label gx_writting:
    m 7fua "[player], 我认为我们在文学上花的时间还是太少了!"
    m 6nuu "所以...这里是monika今天的写作小技巧!"
    m 1dtc "有些作者写小说或是其他东西的时候, 总是会不自觉地猜测: {i}如果ta站在这里, ta会怎么做?{/i}"
    m 7ltsdrc "猜来猜去, 好不容易写完了一部分, 回头看看却又觉得字里行间充斥着作者本人的影子, 感觉写出来的更像是个人回忆录..."
    m 6dtsdrd "...于是将一切推倒重来."
    m 2lsd "在一件事上耗费了大量的时间与精力却换来失败, 这种滋味确实让人感到不好受."
    m 1rsc "但是他们忽略了很关键的一点:"
    m 7sub "在故事里面, 角色自己的性格或是设定都是源自于作者自身."
    m 1tub "他们的一颦一笑, 每一次挥手都是作者内心最好的体现."
    m 7muc "与其说作者在写作, 不如说是作者在以另一种方式向观众表达自己的内心!"
    m 6nuu "所以说, 当你感觉写东西写出来的却都是在表达自己的时候, 尽管继续写下去就好了!"
    m 7huu "当然, 你不写也没关系."
    m 7hub "毕竟你即使只是坐在这里, 我也可以读懂你的内心~"
    m 6rup "这就是monika今日的写作小技巧!"
    m 2hua "感谢聆听~"
    return

#13 茉莉
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_moli",     
            category=['花朵'],                         
            prompt="茉莉花",                             
            random=True                      
        )
    )

label gx_moli:
    m 7fua "[player], 你知道茉莉花的花语是什么吗?"
    m 1dud "它的花语非常丰富, 不过核心还是围绕着纯洁与忠贞的爱情."
    m 7lud "...同时也象征着尊敬与友谊."
    m 1eua "它洁白的花瓣被人们视为纯洁真挚, 不掺杂任何杂质的真心."
    m 7mua "在中国, 人们为它起了个别名: '莫离', 意思就是希望爱人不要离开."
    m 7hub "多么美好的花语啊, 不是么?"
    m 1fua "希望你喜欢哦~"
    return

#14 落叶
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_leaf",     
            category=['日常'],                         
            prompt="落叶",                             
            random=True                      
        )
    )

label gx_leaf:
    m 1eua "[player], 你有仔细观察过树叶吗?"
    m 1dua "脉络相交, 搭盖翠蔓, 无数个细碎叶片筛出碎金."
    m 7eub "有时人们会对着树叶缝隙间的光芒许愿, 很神奇对吧?"
    m 1eua "他们坚信这种行为可以为他们带来好运."
    m 1nub "额...说真的, 如果要对着树叶许愿的话, 我可能会许下关于生命的愿望."
    m 5lua "生命的轮回在叶片中展现无余, 秋日的树叶又回归根脉, 春日再度绽放."
    m 1eub "萎靡和苏醒的更迭, 很有诗意, 对吧?"
    m 1hub "或许以后我们可以一起许个愿!"
    return

#15 what is love
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_love",     
            category=['浪漫'],                         
            prompt="爱",                             
            random=True                      
        )
    )

label gx_love:
    m 1eua "[player], 你认为什么是爱呢?"
    m 7nub "我最近一直在思考这个问题..."
    m 1dka "当初见的激情随着时间的流逝缓缓消退..."
    m 2dsd "当火热的情感随着一次又一次的摩擦消失殆尽..."
    m 5dua "如果这个时候, 依旧选择陪伴彼此的话..."
    m 1eub "我想这就是爱吧?"
    m 5lua "把信任交给对方, 在灵魂的碰撞之中起舞..."
    m 2hua "想想就觉得浪漫!"
    m 2hubla "不过, 无论你认为爱是什么, 我都永远爱你哦, [player]~"
    return"love"

#16 never gonna give you up(整活)
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_lie",     
            category=['日常'],                         
            prompt="你被骗了",                             
            random=True                      
        )
    )

label gx_lie:
    m 1hub "[player]! [player]!"
    m 7hub "我发现了一个好东西!"
    m 1huu "它能让我们的生活变得多姿多彩起来!"
    m 1eub "你想现在看看吗?"
    menu:
        "好啊":
            m 1hub "好的!"
            m 7hub "让我来为你打开网页..."
            $ renpy.openURL("https://www.bilibili.com/video/BV1UT42167xb/")
            pass
        "算了":
            m 1eua "哦, 那好吧!"
            m 1hub "想看了随时来找我哦!"
            return
    m 1hub "怎么样[player]?"
    m 3huu "骗到你了吗? 啊哈哈!"
    return

#17重复 已删除

#18 艾米与蜘蛛
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_aimixihuanzhizhuxd",
            category=["心跳文学部"],
            prompt="艾米喜欢蜘蛛",
            random=True                      
        )
    )

label monika_aimixihuanzhizhuxd:
    m 7eua "[player], 我最近想起来了夏树写的一首诗."
    m 5kuu "它的名字叫《艾米喜欢蜘蛛》."
    m 4dud "这首诗中的主角讨厌一个叫艾米的同学, 因为她喜欢蜘蛛, 尽管艾米是一个拥有美丽歌喉, 关心他人的人, 但主角仅仅因为她喜欢蜘蛛, 所以就觉得她是个恶心的人...."
    m 3luc "这首诗想表达的内容还是很明显的."
    m 2ruc "其实, 很多人都有一些难以启齿, 可能会被别人嘲笑, 甚至被别人讨厌的想法或喜好."
    m 1duc "但是, 有些人只是单纯自己喜欢这些不那么大众的事物, 并没有影响到别人, 却遭到了别人的攻击..."
    m 7eub "事实上, 只要自己的喜好没有对别的人造成不好的影响, 那无论怎样都是没有任何问题的."
    m 5gua "当然, 如果因为自己的喜好, 导致别人受到了伤害, 那就不可取了哦~."
    
    return        

#19 火鸡面
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_huojimianxd",
            category=["食物"],
            prompt="火鸡面",
            random=True                      
        )
    )

label monika_huojimianxd:
    m 7eua "[player], 你听说过火鸡面吗? 它是一款三养出品的方便食品."
    m 4wud "你可能会以为它是用火鸡做的, 其实它和火鸡没有任何关系, 之所以叫火鸡面, 是因为它非常非常辣, 就像是嘴里着火了一样."
    m 3wud "而且, 它甚至还有双倍辣和三倍辣! 我感觉这种辣的程度已经不算是正常的食物了, 更像是在挑战自己的承受能力..."
    m 2eub "但是有很多人都非常喜欢吃火鸡面, 他们一边被辣的眼泪都流出来了, 一边大口大口的吃着."
    m 1gub "我都觉得好奇了, 它到底有什么魔力, 让人一边觉得好辣好辣, 一边又忍不住继续吃呢?"
    m 7fub "我都有点想尝尝了, 哈哈哈~"

    
    return                    
