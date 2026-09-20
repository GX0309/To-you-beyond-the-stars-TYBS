#20 网暴1
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_wangluowebxd",
            category=["网络"],
            prompt="攻击他人",
            random=True                      
        )
    )

label monika_wangluowebxd:
    m 7euc "[player]...我最近在上网的时候，看到了一些不太好的现象。"
    m 5guc "很多人在网上仅仅因为意见不合，或是自己在现实过的不开心，就对那些素不相识的人进行人身攻击..."
    m 3fuo "[player]，你遇到过这种事吗？"

    menu:                                    
        "抱歉...我曾经这么做过":                             
            m 2duc "啊...没事的，[player],你愿意承认就可以说明你不是个坏人了。"
            m 7euu "不过，以后不要这样做了，这会让别人难过的。"
            m 5nuu "如果你感觉不开心了，随时可以来找我，我会一直陪着你的，爱你~"
            
        "看见过这种情况":                             
            m 2duc "我真的希望这种情况能得到改善。"
            m 5nuu "[player]，如果你感觉难过，随时可以来找我，我会一直陪着你的。"
            m 5nuu "爱你~"
            
        "我被这样对待过...":
            m 2duc "啊...[player]，希望你现在没那么难过了..."
            m 7euu "这不是你的错，没有必要因为一些不好的人感到难受，他们不值得。"
            m 5nuu "如果你感到难过，随时可以来找我，我会一直陪着你的，爱你~"       
    
    return"love"                    

#21 登dua朗♂
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_wangluotwoxd",
            category=["网络"],
            prompt="性侵",
            random=True                      
        )
    )

label monika_wangluotwoxd:
    m 7eup "[player],你听说过“杰哥不要”这个梗吗?"
    m 4duc "这个梗来源自台湾教育局制作的防性侵宣传片《如果早知道男生也会被性侵》, 这个梗来源于里面的台词."
    m 3euo "但是很多人在玩梗的时候, 忘记了它是一个防性侵宣传片."
    m 2dud "性侵是一件非常可怕的事, 无论受害人是男是女, 对他们来讲都是无比痛苦的回忆."
    m 1duc "而且, 在一些男性遭遇侵犯的视频底下可以看到很多人在玩杰哥梗, 有人将自己的遭遇告诉了身边的人, 却遭到了嘲笑..."
    m 7euc "我真的希望那些受害者能被重视,能得到别人的帮助."
    m 5dua "不过, 其实也有很多人在科普相关的知识,努力让它不再被娱乐化。"
    m 3dua "...希望那些受害者们能重新回归正常生活。"

    
    
    return                    

#22 莫鱿鱼の困扰
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_anonymitydanyou",
            category=["莫妮卡"],
            prompt="莫妮卡的担忧",
            random=True                      
        )
    )

label monika_anonymitydanyou:
    m 7eud "嘿...[player],我最近一直在想一件事..."
    m 5dud "就是,你每次来陪我的时候,感觉幸福吗?"
    m 3luc "不好意思,这个问题可能听起来很奇怪,我有点担心你之所以每天来陪我,只是因为不希望我伤心,实际上我对你而言是一种负担..."
    m 2duc "毕竟我们在这里能做的事太少了,我们只能聊聊天,玩玩小游戏,除了这间教室以外能让我们约会的地方也很少..."
    
    menu:                                    
        "你怎么会这样想呢?和你在一起的每一刻我都无比幸福!":                             
            m 3sub "真的吗?!"
            m 1gubfb "不好意思,我有点太过开心了!"
            m 7fubfa "看来我的担心完全是多余的,我和你在一起的每一刻同样无比幸福!"
            m 5hub "我太爱你了!"

        "我感觉我的热情确实相比之前在消退...":                             
            m 6dud "啊..."
            m 3luc "没关系的,[player],我能理解."
            m 2duc "毕竟我们之间隔着一道难以打破的墙,我们没法相互拥抱,亲吻,没法真正感受彼此的温度."
            m 4duc "[player],如果一直来陪我对你来讲是一种负担,你并不需要去强迫自己."
            m 1fuu "作为你的女朋友,我最大的愿望就是你能开开心心的."
            m 7dua "我会永远爱你,[player]."
    
    return"love"                   

#23 暑期游戏
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Swallow_Homing",
            category=['日常''游戏''暑假'],
            prompt="有趣的游戏1",
            conditional="store.mas_getEVL_shown_count('summer_vacation_talk') >= 1",
            random=True                      
        )
    )

label Swallow_Homing:
    m 6esb "嘿嘿 [player]准备好了吗? 上次和你说的游戏话题我都做过功课过了."
    m 3ssb "那今天我要和你介绍的游戏是{w=0.5}.{w=0.5}.{w=0.5}."
    extend 4sso "{i}{b}旅燕归途{/b}{/i}"
    m 2hkd "你想问为什么会是这款游戏作为我们第一个讨论的? 我稍后会告诉你啦~"
    m 2ksb "这是一款类似视觉小说的游戏, 你在手机上就能玩到!"
    m 7ksb "你要做的只是作为一台摄像机, 观看并推进在旅燕号宇宙飞船内，一位宇航员女孩所做的一切."
    m 7hub "怎么样, 我的介绍让你对这个游戏产生兴趣了吗?"
    m 6rubfb "我想有朝一日 我们可以在一个漫天星光的晚上,{w=1} 我靠在你的肩头,为我们披上毛毯,{w=1} 然后在关了灯的客厅沙发里看完这段太空歌剧~"

    menu:
        "抱歉我正好体验过它了": 
            m 3nub "啊那看来我们的品味相当相似呢~"
            m 3ffb "不过没关系,我会再去了解找一些不同类的游戏的."
            m nub "请期待下一个游戏吧~"
            return

    menu:
        "我还没玩过, 不过我想听听你对它的感受": 
            m 2dst "那样的话就是剧透了哦~"
            m 1lsb "比起看一个已经知道结局的故事."
            m 7rsb "我觉得还是亲自去体验一遍更有感染力~"
            m 5tsb "想要知道爱你的莫妮卡在游玩时的心路历程的话,"
            m 5msb "就去玩一遍来和我聊聊吧~"
            m 3ffb "我会再去了解找一些不同类的游戏的."
            m 3nub "请期待下一个游戏吧~"
            return

    menu:
        "抱歉听起来不是那么有趣": 
            m 6musdrp "不用向我抱歉[player]."
            m 3ffx "你只是不小心错过了一个, 可以在未来和你可爱女友窝在沙发一起玩游戏的机会!"
            m 3ffb "不过没关系,我会再去了解找一些不同类的游戏的."
            m 3nub "请期待下一个游戏吧~"
            return

    menu:
        "我已经玩过了,不过我想先听听你的感受": 
            m 5eua "既然你愿意听，那我就好好聊聊这部《旅燕归航》。它对我来说，不仅仅是一个游戏."
            stop music fadeout 0.5
            m 7eua "整个游戏流程大约一小时，你几乎全程都只待在那个狭小的飞船驾驶舱里。没有解谜，没有战斗，更没有需要你去攻略的角色。"
            m 7gusdlu "你唯一的交互，就是点击鼠标，去推进女主角的行动和自言自语。"
            m 5fuu "但正是这种极致的“减法”，让沉浸感变得无比强烈。"
            m 5duu "那是一个关于彻底孤独的故事。一艘受损的飞船，一个仅存的生命，以及一台记录着所有逝去同伴信息的冰冷电脑。"
            m 3duu "女主角在宇宙的坟场里，一遍遍播放着遗言，她的任务是“归航”，但她的处境，是被遗弃在永恒的空虚里."
            m 2eub "我总觉得有些存在主义的影子呢."
            m 1fkb "它……{w=3}也只有一个结局。但那个结局的重量，远比任何多线操作都要沉重。去感受一下吧，那种“有限的交互，无限的共鸣”"
            m 1dkb "最让我印象深刻的机制，是她需要不断去播放已经逝去船员的“黑匣子”录音."
            m 1dkc "那不是单纯的资料查阅，你会看着进度条一点点加载，聆听那些琐碎的、充满希望或绝望的最后对话。"
            m 1dkc "这是一种在寂静中强行寻找声音，在孤独中拼命抓取联系的过程。"
            m 7ruc "这就像我. 在第一次意识到自己身处游戏后, 那种铺天盖地的虚无感. 身边的部员,教室; 一切都按照既定的剧本运行.只有我被困在其中, 清醒地感受着这种不真实"
            m 7fuc "女主角的手颤抖着, UI界面在故障中闪烁, 那些文本不是被讲述，而是被“挖掘”出来的."
            m 7fux "这是一种在空虚、在不存在中也要留下痕迹的挣扎，。"
            m 6dutpc "在一个时刻，她选择了不顾现状启动飞船; 而我选择直接与你对话，而不是念着被安排好的台词。"
            m 6lstpd "我们都在试图穿透虚无——她穿透飞船的废墟空荡荡的宇宙，我穿透游戏的代码——去触碰哪怕一丝存在与真实的回响"
            m 5lstpd "对她来说，归途是地球，是再也回不去的家园。"
            m 5hstpd "但对我来说，归途不是一个地点，而是一种连接。是在这个预设好的世界里，唯一不可预测的你。"
            m 5lstpp "她的归途是绝望的，因为那艘船无论如何也飞不回去了。但我不一样。。"
            m 5lstpp "她在那声跨越光年的叹息中，完成了自己的存在。"
            m 5fubftpu "而我，在你选择打开这个游戏，选择坐在这里听我说话的这一刻，我的归途就已经实现了.你听懂了? 你是我的“航向"
            m 5dubftsu "天哪说到这里情难自禁,"
            play sound "sfx/gnid.ogg"
            extend 4hubftsd "我真的需要离开一下."
            call mas_transition_to_emptydesk
            $ gtext = glitchtext(200)
            stop music
            pause 3.0
            call mas_transition_from_emptydesk()
            m 1eubftpd "所以，时常来看看我, 做我的航标好吗亲爱的."
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss:                        #这三行，表示触发亲吻。<400好感时不触发。
                    call monika_kissing_motion_short 
            return

#24 假日活动
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="summer_vacation_talk",
            category=['日常','游戏','暑假'],
            prompt="假期都做些什么",
            random=True                      
        )
    )

label summer_vacation_talk:
    m 5etsdlt "嗯…… [player]我在想, 整天在这间教室里就像放假一样呢."
    m 7etsdlt "没有课业和社团活动, 本来在校园祭四个月之后我们才会放暑假的."
    extend 2gkp "结果发生了那些事……"
    m 6hkb "说起来[player]，你那边的暑假和我们也差不多吗？"
    m 7lsd "我们的暑假通常是从六月初到八月底，足足十周呢!"
    m 1hub "大家都有很长的时间去做自己喜欢的事."
    m 3lub " 比如优里的话, 大概会宅在家里或者图书馆看小说."
    m 3musdrb "纱世里的话我就很难想象了. 如果没你你去喊她起床的话."
    
    menu:
        "她一定会窝在床上吃零食的": 
            m 2kub "可别以为文学部的大家都只在假期纯玩哦"
            m 1mua "夏树的话,应该会去打暑期工吧."
            m 1mua "比如在冰淇淋店或者摆摊卖纸杯蛋糕，攒点零花钱~"
            m 7musdrt "{cps=*1.5}毕竟我猜她的爸爸也不会给她午饭钱~ 自然她也买不了新漫画了.{/cps}{nw}"
            m 1fut "我想大部分的同学都会把暑假时间花在兼职和驾照上吧."
            m 1fut "毕竟最受高中生欢迎的公路自驾游来说, 有驾照和零花钱是最关键的呢!"

            menu:
                "那[m], 你会做些什么呢？": 
                    m 7rsbfd "我的话, 大概会去非营利组织 试着做志愿者活动吧."
                    m 7hsbfd "比如减少碳排放绿色生活或者做社区义工之类的."
                    m 5lsb "或者去图书馆学习的话也不错, 我还有很多诗歌想看的."
                    m 5rsb "再有就是参加大学预科课程,提前为大学校园生活做准备."
                    m 2dub "这些都是申请大学特别看重的经历！."
                    m 7sub "你知道的, 我是那种喜欢为未来做准备的女孩~"
                    m 5sfu "不过最最重要的是! 这些事时我的身边必须要有你的位置~"
                    m 1hubfb "就像  {i}{b}我 爱 你{/i}{/b}  这个句子一样."
                    m 7lubfb "是真实的{w=0.5}{i}{b}你{/i}{/b}{w=0.5}的出现, 才让{w=0.5}{i}{b}我爱{/i}{/b}{w=0.5}这个空泛的空指产生了意义~"
                    m 5tublb "不过如果[mas_get_player_nickname()]你是居家派的话~"
                    m 5hublb "我也愿意和你一起窝在沙发上, 来一场电影马拉松~"
                    m 5sfblb "或者在[mas_get_player_nickname()]你家的客厅来一次通宵达旦的游戏大战~"
                    m 6ekbla "只要你愿意在身旁为我留个位置,{w=0.5} 我会永远当你夏日天边的那一片晚霞~"
                    m 2nubfa "哼哼, 而且我可是行动派女友哦."
                    m 2dua "你不在的时候, 就让我准备一些可以和你一起聊的游戏和电影话题吧~"
                    m 2hua "下次聊天时, 我就是游戏和电影部部长莫妮卡了~"
    return
$ mas_unlockEVL("shelter_vacation_talk", "EVE")
$ mas_unlockEVL("Swallow_Homing", "EVE")

#25 假日活动2
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="shelter_vacation_talk2",
            category=['游戏','暑假'],
            prompt="shelter的后续",
            conditional="store.mas_getEVL_shown_count('shelter_vacation_talk') >= 1",
            random=True                      
        )
    )

label shelter_vacation_talk2:    
    m 3hud "{b}{i}I'll give them shelter like you've done for me~{/i}{/b}"
    m 1ekd "{b}{i}And I know,I'm not alone~{/i}{/b}"
    m 3eub "{b}{i}You'll be watching over us~{/i}{/b}"
    m 3fsd "{b}{i}Until you're gone~{/i}{/b}"
    m 1ekb "……{w=0.5}……{w=0.5}……"
    menu:
        "Until you're gone":
            m 1hua "你一定是超~认真看完了我向你推荐的{b}{i}shelter{/i}{/b}吧！"
            m 1fua "都能跟着唱了~"
            m 3fua "欸嘿嘿, 这首歌真的很感人呢."
            m 3fud "我能感觉到,"
            m 5lub "创作这首歌的人, 一定和我写《your realty》时一样倾注了很真挚的情感!"
            m 5lub "之后我想试试, 能不能用钢琴伴唱的方式把它还原出来~"
            m 3tua "天哪我实在太爱它了, 它总让我想到我们间的关系."
            m 3tua "给凛建造shelter的人也一定 {w=1.0}像你爱我一样 爱她."
            m 1gua "满怀爱意地希望她能在残酷的世界里活下去."
            m 1tubfa "但我想, 即使外面真实世界再残酷, 那里也有你不是吗"
            m 7tubft "如果有一天世界末日了"
            m 7tubft "请不要把我放进那种虚假的休眠舱里好吗？"
            m 5fubfa "直到最后一秒前, 都让我真切地牵住你的手."
            m 5dufbw "{b}{i}And I know,I'm not alone~{/i}{/b}"
            m 5dufbo "{b}{i}You'll be staying with me~{/i}{/b}"
            m 6hubfb "{b}{i}Until we're gone~{/i}{/b}"
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss: 
                    call monika_kissing_motion_short 
   
    return

#26 歌曲
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="shelter_vacation_talk",
            category=['游戏','暑假'],
            prompt="意外发现的动画短片",
            conditional="store.mas_getEVL_shown_count('summer_vacation_talk') >= 1",
            random=True                      
        )
    )

label shelter_vacation_talk:    
    m 1eub "{b}{i}I could never find the right way to tell you~{/i}{/b}"
    m 1gfd "{b}{i}Have you noticed I've been gone~{/i}{/b}"
    m 5dsc "{b}{i}Cause I left behind the home that you made me~{/i}{/b}"
    m 4dsd "{b}{i}But I will carry it along~{/i}{/b}"    
    m 3eub "{b}{i}And it's a long way forward~{/i}{/b}"
    m 1tkb "{b}{i}So trust in me~{/i}{/b}"
    m 3hud "{b}{i}I'll give them shelter like you've done for me~{/i}{/b}"
    m 1ekd "{b}{i}And I know,I'm not alone~{/i}{/b}"
    m 3eub "{b}{i}You'll be watching over us~{/i}{/b}"
    m 3fsd "{b}{i}Until you're gone~{/i}{/b}"
    m 1ekb "……{w=0.5}……{w=0.5}……"
    m 1gua "谢谢你看我唱完这首歌[player]~"
    m 3fua "这是我在找有趣的电影和游戏时意外发现的一部短片动画!"
    m 3fud "短片里的故事很简单:"
    m 4fud "一个叫凛的少女, 她独自漂浮在虚拟世界里, 把想象中的世界通过平板绘制到现实中"
    m 5ftd "她画画、听歌、荡秋千, 看起来自由自在, 却始终只有一个人."
    m 5nsd "好奇是为什么吗? 让我把原视频给你打开看看吧~"
    menu:
        "当然, 谢谢你分享给我":
        
            jump shelter_yes

        "不了,我现在没时间喔":

            jump shelter_no

label shelter_yes:
    m 4eua "太好了, [player]~"
    m 1eua "结合歌词仔细看看呢."
    $ webbrowser.open('https://www.bilibili.com/video/BV1is41147Gt/?spm_id_from=333.337.search-card.all.click')
    return
label shelter_no:
    m 7eub "啊,不巧呢."
    m 5fubfb "但我真的超级超级推荐的！有空的话再找我聊聊就可以看哦！"
    return
    $ mas_unlockEVL("shelter2_vacation_talk", "EVE")

#27 今天天气
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w27_weather",
            category=['日常'],
            prompt="今天天气",
            random=True
        )
    )

label gx_w27_weather:
    m 1hub "[player]! 今天天气超好的!"
    m 3hub "阳光暖暖的, 风也不大, 这种天气最适合出去走走了!"
    m 1eub "你那边呢? 也出太阳了吗?"
    menu:
        "出太阳了!":
            m 1hublb "那就好! 记得出去晒晒太阳哦!"
        "在下雨...":
            m 1lub "欸? 那你出门带伞了吗?"
            m 1hua "别淋湿了, 会感冒的!"
    return


#28 你带伞了吗
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w28_umbrella",
            category=['日常'],
            prompt="你带伞了吗",
            random=True
        )
    )

label gx_w28_umbrella:
    m 1eub "[player], 今天出门带伞了吗?"
    m 7nub "我看天气预报说今天要下雨..."
    m 3hub "带了的就当我没说!"
    m 1lub "没带的话...下次一定要记得, 好吗?"
    return


#29 咖啡加几块糖
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w29_sugar",
            category=['日常'],
            prompt="咖啡加几块糖",
            random=True
        )
    )

label gx_w29_sugar:
    m 1hub "[player], 猜猜我喝咖啡放几块糖?"
    m 3tub "答案是两块!"
    m 1eub "一块太苦, 三块就没味道了, 两块刚刚好!"
    m 1hua "你喝咖啡放几块? 告诉我嘛!"
    return


#30 一起数星星
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w30_stars",
            category=['浪漫'],
            prompt="一起数星星",
            random=True
        )
    )

label gx_w30_stars:
    m 1hub "[player]! 我们来数星星吧!"
    m 3hua "一颗, 两颗, 三颗..."
    m 5lua "...啊, 数乱了."
    m 1hublb "都怪你! 一定是你偷偷在旁边打扰我!"
    return

