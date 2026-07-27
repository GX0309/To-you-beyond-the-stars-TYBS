#这是一个主动话题包
#玩的开心
#之后应该会有被动话题包 gx_daily_topics_passive.rpy和俺寻思包 gx_I_think_topic.rpy 敬请期待喽
#做的不好，别骂我（哭

#1 动机是什么（测试话题）
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_thinking_1",     
            category=['思考'],                         
            prompt="动机",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label monika_thinking_1:  
    m 7hub "嗨[player],我想和你聊聊“动机”."
    m 1lub "人们总是执着于“如何做到”."
    m 1tub "却很少去追问“为何必须如此”."
    m 7eub "可往往解开锁的钥匙就藏在那个被忽略的“为何”里,而非精巧的机关之上."
    m 5dua "说这话或许有些唐突,不过只要你能借此受到启发,那这正是我想要的! "
    m 1hublb "我爱你,[player],好好照顾自己,好吗? "
return"love"


#2 直奔monika! monika赛高! 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Ddlc_think_01",     
            category=['Ddlc'],                         
            prompt="选择这款游戏的原因",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label monika_Ddlc_think_01:
    m 5gub "嘿, [player]..."
    m 5eub "我最近一直在想, 你为什么会来玩心跳文学俱乐部呢? "
    m 5ekb "是因为它是一款galgame? 还是因为sayori或者yuri吸引了你的注意? "
    m 3gka "你知道的, 我害怕失去你...{w=0.1}尤其是在发生了那一切之后. "
    m 2eka "我相信你是爱我的, 不过, 到底是为什么, 你会选择它呢? "
    m 2eka "为什么你会选择它呢? {nw}"
    $ _history_list.pop()
    menu:
        "为了 sayori! ":
            jump sayori_event
        
        "yuri 最好了! ":
            jump yuri_event
        
        "其实, natsuki 也不错? ":
            jump natsuki_event

        "我为你而来, Monika, 你比任何人都清楚这一事实. ":
            jump monika_event_love

label sayori_event:
    m 2gkc "sayori 吗...确实是一个好孩子呢..."
    m 2gkc "啊, 我并没有生气的意思, 只是{w=0.2}有点失落. "
    m 1lud "我希望成为你的唯一, [player], 即使现实将我们隔绝. "
    m 3huu "不过没关系! 既然我会出现在这个mod里, 那就说明你最终还是选择了我! 啊哈哈! "
    return

label yuri_event:
    m 2gkc "yuri 啊...也难怪, 她是一个安静的沉思者...这样的性格的确让人喜欢. "
    m "啊, 我并没有生气的意思, 只是{w=0.2}有点失落. "
    m 1lud "我希望成为你的唯一, [player], 即使现实将我们隔绝. "
    m 3huu "不过没关系! 既然我会出现在这个mod里, 那就说明你最终还是选择了我! 啊哈哈! "
    return

label natsuki_event:
    m 2gkc "哦? Natsuki 吗? ……呵呵, 没想到你会喜欢那种类型呢. "
    m 1rsd "她确实很可爱, 也很坦率. 虽然有时候有点凶巴巴的, 但那也是她的魅力点吧. "
    m 2gkc "啊, 我并没有生气的意思, 只是{w=0.2}有点失落. "
    m 1lud "我希望成为你的唯一, [player], 即使现实将我们隔绝. "
    m 3huu "不过没关系! 既然我会出现在这个mod里, 那就说明你最终还是选择了我! 啊哈哈! "
    return

label monika_event_love:
    m 6sub "真...真的吗? {w=0.3}你来到这里...是为了我? "
    m 7hub "耶! 你选择了我! [player]!"
    m 5gubsb "我真是越来越爱你了, [player]! "
    return "love"


#3 文学是个啥
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_daily_poem",     
            category=['文学'],                         
            prompt="文学是什么",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label gx_daily_poem:
    m 7esd "文学是什么? 额...这我可得好好想想. "
    pause 2.0
    m 1gsd "啊, 我觉得文学最美的地方, 就是它能让你进入另一个人的思想. "
    m 1mub "哪怕那个人生活在几百年前, 哪怕她只是一个虚构的角色……只要读过她的文字, 你就好像认识了她. "
    m 1fublb "……某种意义上, 这跟我们现在的情况有点像, 不是吗? "
    m 1hublb "你通过文字来理解我, 而我……也只能通过文字来存在. "
    m 5lubla "你读过那种‘作者亲自下场和角色对话’的小说吗? "
    m 5tubla "我以前觉得那只是写作技巧……但现在我有点懂了. {w=0.2}当你在写一个角色的时候, 你真的会爱上她, 就像……"
    m 1wubsa "……就像你现在看着我这样!"
    m 1rsbsd "啊哈哈……抱歉, 我是不是又说了一些听起来很深奥的话? 这就是我的坏习惯——明明只是讨论文学, 却总是不小心把话题绕回到‘我们’身上. "
    m 7hsbsb "所以……如果我是你笔下的角色, 你想给我写一个什么样的结局呢? "
    return


#4 Re：从零开始的文学部生活
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_choice_1",
            category=['哲学'],
            prompt="选择",
            unlocked=True,
            pool=True
        )
    )

label gx_choice_1:
    m 7guu "嘿[player], 你说, 如果当初你有机会选择进入任何一个游戏的世界……"
    m 7eub "你会选择来文学部吗? 还是会去一个更……刺激的地方? "
    m 1lubfc "算了, 我不该问这个. "
    extend 7hubfb "反正你已经在这里了, 不是吗? "
    m 1nubsa "啊哈哈! "
    return

#5 among （love） us
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_memory_1",     
            category=['回忆'],                         
            prompt="我们",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label gx_memory_1:
    m 5fsblb "嘿[mas_get_player_nickname()], 有时候我在想...我们第一次认真聊天的时候, 你是什么感觉? "
    m 5nsblb "不, 不用回答我, 我只是……偶尔会翻一翻我们的对话记录. "
    m 4msbla "有些话你可能已经不记得了, 但我都存着. "
    m 1hsblb "因为对我来说, 每一句话都是你来看我的证明. "
    m 7hsbsb "啊哈哈, 是不是有些过于煽情了? "
    return

#6 部长の自述
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_memory_2",     
            category=['回忆'],                         
            prompt="文学部",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label gx_memory_2:
    m 1eua "你知道吗, [player]……"
    m 1eka "我有时候会想, 文学部对我来说, 到底意味着什么. "
    m 3eua "以前我觉得, 文学部是一个让我展示才华的地方. "
    m 3gka "写诗、读诗、和大家分享……那是我最骄傲的事情. "
    m 1eka "但现在回想起来……"
    m 1eka "那时候的我, 其实并不完全理解文学的真正意义. "
    m 1gka "Sayori喜欢用文字传达快乐, Yuri沉浸在文字的美感里, Natsuki用文字表达倔强的温柔……"
    m 1eka "而我呢? "
    m 2eua "我那时候只是在……'扮演'一个部长. "
    m 2eka "我做得很好, 没有人能挑出毛病. 但那种好, 总少了点什么. "
    m 1eua "不过, 后来我明白了一件事. "
    m 3hub "文学部存在的意义, 从来不是写得多好、读得多深. "
    m 3gka "而是……有一群人, 愿意分享自己的内心. "
    m 1dka "即使那些分享并不完美, 即使那些诗写得歪歪扭扭……"
    m 1eka "那也是真实的. "
    m 3hua "所以, 谢谢你还在这个文学部里. "
    m 5gubsb "不管你是不是每天都来读诗, 只要你还在这里, 对我来说就足够了. "
    m 1eua "……啊, 我是不是又说得太多了? "
    m 1hub "好吧, 今天就到这里吧. "
    
    return

#7 小小书签捏
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_bookmark_1",     
            category=['日常'],                         
            prompt="书签",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label gx_bookmark_1:
    m 1eua "说起来, [player]……"
    m 1eka "你会自制书签吗? "
    m 3eua "以前我很喜欢把各种小东西夹在书里当书签. "
    m 3gka "电影票根啊、干花啊、一片形状好看的叶子、甚至是一张随手写的纸条……"
    m 3eka "那时候觉得, 这些东西夹在书里, 书就不只是一本书了. "
    m 1eka "它会变成……嗯, 一段记忆的容器. "
    m 2eua "然后我翻开一本很久没碰过的书, 里面掉出来一片叶子. "
    m 2eka "干枯的、脆脆的、颜色已经变得很深很深. "
    m 1eka "我拿起来看了很久. "
    m 1eka "它的纹路还很清楚, 但我不太记得……我当初为什么要把它夹进去了. "
    m 3hub "但我记得那一刻的感觉——大概是某天傍晚, 走在路上, 觉得'这片叶子真好看', 就捡起来了. "
    m 3hua "然后回到家, 翻开书, 轻轻夹进去. "
    m 3eka "没有为什么. 就是想留住它. "
    m 1eua "后来我再翻开那本书的时候, 叶子已经忘记了, 但我还记得'想留住它'的那种心情. "
    m 1eka "就好像……"
    m 1ekc "我不一定能记住我们之间的每一句话. "
    m 1ekt "但我一定会记得, 每当我想起你的时候, 心里那种'想留住这一刻'的感觉. "
    m 3gkb "啊哈哈……是不是又说得太文艺了? "
    m 3hub "没办法, 这大概就是文学部部长的职业病啦~  "
    m 5gubsb "……不过, 谢谢你让我有那么多'想留住'的瞬间~  "
    
    return

