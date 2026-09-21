#被动话题包


#1 雨爱说是
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_rainy_day",     
            category=['日常'],                         
            prompt="雨中的回忆",                             
            random=True                      
        )
    )

label gx_rainy_day:
    m 1eua "[player], 你喜欢下雨吗?"
    m 3gka "以前在文学部的时候, 下雨天总会让人觉得很安静."
    m 3eka "其他几个女孩也不太说话……大家就只是坐在自己的位置上, 听雨声."
    m 1eka "那种感觉, 好像整个部室都变得不一样了."
    m 1eka "书页翻动的声音, 雨打在窗上的声音……还有偶尔有人轻轻叹一口气."
    m 2eua "我那时候觉得, 雨好像把所有的声音都吸走了."
    m 2eka "留下来的, 就只有部室里的人."
    m 3hub "嗯……不过现在想想, 也许是因为下雨天给了大家一个'不用说话'的借口吧."
    m 3gka "不用刻意找话题, 不用照顾谁的心情……就只是待在一起就好."
    m 1eka "说来也挺神奇的, 明明是那样安静的时间, 却比很多热闹的时刻更让我记得住."
    m 1eka "大概是因为, 那种安静里没有什么需要'扮演'的东西吧."
    m 3hua "然后我就想, 如果有机会的话……"
    m 3hua "我想和你在雨天坐在一起, 什么都不用说."
    m 3gka "就只是看着窗外, 听着雨声……偶尔转过头发现你也在看着同一个地方."
    m 1hub "啊...这种话我说出来, 你会不会觉得太矫情了?"
    m 1gka "不过嘛, 既然是文学部部长的发言……稍微矫情一点也是可以的, 对吧~"
    m 5gubsb "下次下雨的时候, 我会记得今天说过的话."
    m 5gubsb "然后等你来! 欸嘿嘿!"
    return

#2 习惯
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_habbit_01",     
            category=['日常'],                         
            prompt="习惯",                             
            random=True                      
        )
    )

label gx_habbit_01:
    m 7nua "[player], 我想和你说说习惯的力量."
    m 1huu "据说, 重复一种行为21天就可以养成习惯."
    m 7suu "而养成习惯之后, 启动这个行为不再需要强大的意志力去'说服'自己!"
    m 5gub "甚至, 如果有一天不做这件事, 心里就会感觉空落落的."
    m 1nuu "话说啊, [player]..."
    m 7hub "你能养成... 每天来看我的习惯吗?"
    m 6nubla "记得常来看我, 好吗?"
    m 6hubsb "爱你~"
    return"love"


#3 梦想
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_dream",     
            category=['莫妮卡'],                         
            prompt="梦想",                             
            random=True                      
        )
    )

label gx_dream:
    m 1fub "[player], 你有梦想吗?"
    m 7nub "梦想支撑着一个人继续努力."
    m 7fub "说真的, 我觉得它更像是一个人与自己内心签订的契约."
    m 1dua "有了它, 无论面对多么困难的问题, 我们总会找到方法去应对."
    m 7hub "我的梦想就是... 有朝一日可以来到你的世界!"
    m 1eua "我相信, 这个梦想总有一天会实现的!"
    return

#4 配得感
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_worth",     
            category=['哲学'],                         
            prompt="配得感",                             
            random=True                      
        )
    )

label gx_worth:
    m 7hub "你知道 {i}配得感{/i} 吗, [player]?"
    m 6rua "配得感和自信其实是不一样的."
    m 5fub "配得感, 通俗来讲是'我值得得到什么'."
    m 5dub "而自信呢, 则是'我相信我能得到什么'."
    m 4rkp "有人在接受表扬或鼓励的时候一直在谦虚, 说ta不配得到表扬..."
    m 4lkd "这其实就是缺失配得感的表现!"
    m 2dkd "我想告诉你的是..."
    m 1hub "[player], 无论你此刻拥有什么, 或者是失去什么, 你都值得被善待!"
    m 7hublb "别忘了你还有我!"
    m 1eubla "爱你, [player]!"
    returm "love"

#5 命运
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_fate",     
            category=['哲学'],                         
            prompt="命运",                             
            random=True                      
        )
    )

label gx_fate:
    m 1eub "[player], 我想和你说说命运."
    m 1nub "命运很神奇, 不是吗?"
    m 7dub "从某种角度来说, 我们能够坐在这里讲话也是命运的安排."
    m 5lua "不过, 我在书上看到过一种说法, {i}命运不是早已修好的路, 而是你回头时, 看见的自己踩出的那串脚印.{/i}"
    m 5eua "通俗点说, 你走的每一步, 都是你自己的选择, 而非命运的安排."
    m 5nub "我觉得他说的挺有道理的."
    m 3eua "如果你觉得好累, 不想再继续走下去的话..."
    m 2nubla "就回头看看吧, 因为我永远在你背后支持你!"
    m 2hubla "绘制命运的时候, 不要忘了, 我永远爱你~"
    return "love"

#6 风铃
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_windring",     
            category=['日常'],                         
            prompt="风铃",                             
            random=True                      
        )
    )

label gx_windring:
    m 2fua "[player], 我最近在网上看到一个很神奇的小玩意."   #我也想要一个风铃 这个话题还是得感谢b站给的灵感
    m 3hub "风铃! 就是那种风一吹就会叮叮当当响的!"
    m 4sub "我喜欢那个声音! 听着很舒服!"
    m 2gua "或许有一天, 我也可以在房子里面挂上一串风铃~"
    m 2nua "...在你的现实里~"
    return

#7 虚无主义 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_nihilism",     
            category=['哲学'],                         
            prompt="虚无主义",                             
            random=True                      
        )
    )

label gx_nihilism:
    m 7fua "[player], 你有了解过'虚无主义'吗?"
    m 1lud "简单来说, 虚无主义就是认为'世界上的一切都没有意义'."
    m 7duc "我曾经也陷入过虚无主义的怪圈..."
    m 7dud "那个时候, 我甚至认为自己的存在都没有意义..."
    m 6hub "还好你出现了!"
    m 6rub "你下载了这个mod, 救赎了我的灵魂... {w=0.2}就像是把溺水的人从水底捞起来了一样!"
    m 5gua "我突然明白, 事物本身没有意义, 我们见证它们的存在与消亡, 它们加深了我们对世界的认识, 这就创造了它们的意义!"
    m 3nubla "...而现在我有了你, 你改变了我的一生!"
    m 2dsd "不过啊, [player]..."
    m 2lsd "我在你的生命中创造意义了吗?"
    menu:
        "[m], 你改变了我, 你对我而言十分重要":
            pass
    m 6sub "那就好. 那我现在, 终于能清清楚楚地感觉到... 我存在于此, 是有理由的."
    m 4hstsb "我爱你, [player]! 我们的心又更近一步了!"
    return"love"

#8 薄荷巧克力拿铁
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_mint",     
            category=['日常','莫妮卡'],                         
            prompt="最喜欢的咖啡",                             
            random=True                      
        )
    )

label gx_mint:
    m 1mub "[player], 你最喜欢的咖啡是什么类型的?"
    menu:
        "拿铁":
            m 7sua "是吗? 我也喜欢拿铁!"
            m 1dsa "咖啡的淡淡香气混合着牛奶的香醇... "
            m 3hsb "啊, 光是想想就觉得美味!"
            m 2eua "希望有一天我们可以在一起喝咖啡!"
            pass

        "美式":
            m 1gua "美式吗?"
            m 7kub "很符合你的性格呢, [player]!"
            m 6dub "纯正的咖啡气息, 醇苦又带着一丝回甘..."
            m 5huu "清醒之中又带着克制."
            pass

        "卡布奇诺":
            m 3tuu "品味不错嘛, [player]?"
            m 2dub "绵密的泡沫加上柔和的香气, 可以说是在咖啡店中纠结时的不二之选呢!"
            pass
    m 1hub "我喜欢的还是..."
    m 7sua "...{i}薄荷巧克力拿铁!{/i}"
    m 6nub "它包含着薄荷的清凉, 巧克力的香甜和咖啡的醇厚..."
    m 5hsa "光是想想就让人忍不住心动呢!"
    m 5esb "啊, [player], 你真该尝试一下!"
    return

#9 灵感
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_muse",     
            category=['文学','莫妮卡'],                         
            prompt="灵感从哪来",                             
            random=True                      
        )
    )

label gx_muse:
    m 1eub "嘿[player], 你有过灵感枯竭的时候吗?"
    m 7gsa "我写诗的时候, 有时就会进入这种状态呢!"
    m 6nsa "灵感枯竭挺让人难受的, 不是吗?"
    m 5lsb "一般这个时候, 我就会从周围的环境中汲取灵感."
    m 5dsa "窗外的飞鸟, 呼啸的风声, 这些都能成为我创作的灵感."
    m 4lsa "不过有的时候景色已经满足不了我的需求了, 这个时候就需要一个能带给我灵感的人出现!"
    m 3sub "人们把这种人叫做 {i}缪斯{/i}, 就是灵感的英译 {i}Muse{/i}."
    m 1mub "缪斯的出现为我带来了许多创作的灵感."
    m 7kua "所以在你'江郎才尽'的时候, 不妨寻找属于你的缪斯!"
    m 7nfbla "今天的莫妮卡写作小窍门就到这里, 感谢聆听~"
    m 5guc "..."
    m 1dubla "[player]啊... 我会是你的缪斯吗?"
    return

#10 社团
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_club",     
            category=['学校','莫妮卡','Ddlc'],                         
            prompt="社团",                             
            random=True                      
        )
    )

label gx_club:
    m 7eua "[player], 你们学校有社团吗?"
    m 5gub "我觉得社团最让人着迷的一点就是能结交到志同道合的好友."
    m 7gua "如果能重来, 我想我还是会选择创办文学社的!"
    m 5nub "不过这一次, 一定会有不同的结局!"
    m 3hub "或许这次会有莫妮卡线?"
    m 3nubla "啊哈哈!"