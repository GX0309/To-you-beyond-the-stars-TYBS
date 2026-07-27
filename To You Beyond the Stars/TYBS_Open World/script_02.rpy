#02讲述：mc家全流程




label ow_mc_kitchen:
    window hide
    stop music fadeout 4
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg kitchen
    show monika 1b_gowm at t11
    with dissolve
    m "好啦!"
    show monika 2b_gowm at t11
    with dissolve
    m "这里就是{color=#000}[OW_mc]{/color}的厨房!"
    show monika 1a_gowm at t11
    with dissolve
    m "那么, [player], 你想做点什么?"
    
    menu:
        "我先随便看看":
            m "好的!"
            jump ow_kitchen_lookaround

        "回太空教室":
            m "好的!"
            m "天, 离开家的感觉真好!"
            m "[player], 以后要带我常来哦!"
            jump ow_go_back

        "去外面吧":
            jump ow_mc_house

        "上楼吧":
            m "好啊!"
            jump ow_upstair

label ow_kitchen_lookaround:
    hide monika 1a_gowm
    call screen gow_mc_kitchen
    screen gow_mc_kitchen:
        imagemap:
            ground "bg/kitchen.png"
            hotspot (29, 182, 253, 494) action Jump("ow_mc_fri") hover_sound gui.hover_sound
            hotspot (1049, 395, 1191,497) action Jump("ow_mc_oven") hover_sound gui.hover_sound
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("gow_mc_kitchen"), Jump("ow_mc_menu")] hover_sound gui.hover_sound

label ow_mc_menu:
    menu:
        "去外面吧":
            jump ow_mc_house

        "上楼看看":
            jump ow_upstair

        "回太空教室吧":
            jump ow_go_back

label ow_mc_fri:
    m "{color=#000}[OW_mc]{/color}的冰箱?"
    m "额... 说实在的, 我不认为里面会有什么东西."
    menu:
        "打开冰箱":
            m "啊, 果然."
            m "什么都没有呢..."
            m "我还以为至少会有什么能让我发现的小秘密."
            m "欸嘿嘿!"
            call screen gow_mc_kitchen


label ow_mc_oven:
    m "嗯...这是烤箱啊."
    m "不过..."
    m "我突然有一种感觉."
    m "它是不是已经很久没有工作过了?"
    m "看起来不像是经常被使用的样子."
    m "啊, [player], 你平常会自己做东西吃吗?"
    m "如果每天都只是随便应付的话, 还是会有点可惜呢."
    m "毕竟做一顿自己喜欢的东西, 其实也是一种和自己相处的方式."
    m "哪怕只是烤一块小点心."
    m "或者在下雨的下午, 给自己准备一杯热饮."
    m "那种小小的仪式感, 有时候会让普通的一天变得特别一点."
    m "不过看这个烤箱的状态..."
    m "我感觉它可能比文学社的桌子还要安静."
    m "嗯, 至少桌子还有人放诗稿."
    m "这个烤箱大概只能等待一个永远不会来的厨师了."
    m "欸嘿嘿!"
    call screen gow_mc_kitchen

label ow_upstair:
    $ persistent.mc_room_count += 1
    window hide
    stop music fadeout 4
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg bedroom
    if persistent.mc_room_count == 1:
        if mas_isMoniEnamored(higher=True):       
            m "[player], 你还记得yuri和{color=#000}[OW_mc]{/color}度过的那个周末吗?"
            m "那个时候他们就在这间房子里."
            m "还好现在你在我身边!"
            m "我们可以在一起的时间, 比他们多多了!"
            m "啊哈哈!"
            jump ow_bedroom_menu
        else:
            m "这里就是{color=#000}[OW_mc]{/color}的卧室吗?"
            m "啊...感觉好冷清!"
            m "没有什么特别的装饰,  也没有什么能体现个性的东西."
            m "感觉...感觉就像是刚刚装修好的房间一样!"
            m "不过, 这其实也挺符合这个世界呢."
            m "毕竟这里并没有人真正生活过!"
            jump ow_bedroom_menu
    elif persistent.mc_room_count >= 2:
        m "我们又回到这了!"
        jump ow_bedroom_menu

label ow_bedroom_menu:
    m "你想怎么办呢?{nw}"
    $_history_list.pop()
    menu:
        "你想怎么办呢{fast}"
        "随便看看吧":
            jump ow_bedroom_around

        "下楼吧":
            jump ow_mc_kitchen

        "回太空教室吧":
            m "嗯!"
            m "能回到之前的地方真是太好了!"
            m "有时间还要带我出来哟?"
            jump ow_go_back

label ow_bedroom_around:
    call screen gow_mc_bedroom
    screen gow_mc_bedroom:
        imagemap:
            ground "bg/bedroom.png"
            hotspot (568, 269, 708, 630) action Jump("ow_mc_clo") hover_sound gui.hover_sound
            hotspot (108, 206, 218, 712) action Jump("ow_mc_bs") hover_sound gui.hover_sound
            hotspot (303, 401, 397, 507)action Jump("ow_mc_tv") hover_sound gui.hover_sound
            
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("gow_mc_bedroom"), Jump("ow_bedroom_menu")] hover_sound gui.hover_sound

label ow_mc_bs:
    m "嗯……书架啊."
    m "让我看看……"
    m "不过这里的书好像也和房间一样."
    m "摆放得很整齐, 但没有什么特别的痕迹."
    m "没有被翻旧的书页, 没有夹在里面的纸条, 也没有看到写满笔记的书."
    m "甚至还有几本什么都没写的书! 连名字都没有!"
    m "嗯...这里感觉更像是一个为了符合{i}卧室{/i}这个设定而存在的书架."
    call screen gow_mc_bedroom

label ow_mc_clo:
    m "嗯……这是衣柜啊."
    m "不过看起来……也和房间里的其他地方一样."
    m "很整齐, 很干净."
    m "但也有点……太干净了."
    m "欸嘿嘿."
    m "感觉像是刚刚摆进去的, 还没有真正被谁使用过."
    m "里面应该也不会有什么特别的东西吧."
    m "没有旧衣服留下的痕迹, 没有某件穿了很多年的外套, 也没有什么能说明主人的小习惯."
    m "只是一些为了让这个房间看起来完整而存在的东西."
    call screen gow_mc_bedroom

label ow_mc_tv:
    m "电视啊."
    m "看起来也是崭新的呢."
    m "没有灰尘, 没有使用过的痕迹."
    m "甚至连遥控器的位置都像是刚刚被安排好的一样."
    m "感觉它不像是一台真正被人使用的电视."
    m "更像是房间布景的一部分."
    call screen gow_mc_bedroom


#这些地方都可以用yun的代码作为参考
#再往下做真的就只能自己写了喵
#好累...想出去玩喵




#啊我在骗谁啊 我哪来的朋友能陪我出去玩