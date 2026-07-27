#进入ow, 初始场景 mc家门口
#流程：mc家——（向左）sa家——街道2——电玩城——商城——咖啡馆（cg预定）
#流程2：mc家——（向右）街道1——街道3——校门口——走廊——club
#01讲述：sa家



label ow_go_back:
    $ HKBShowButtons()
    $ mas_HKBDropShield()
    window hide
    stop music fadeout 4
    show black zorder 100 with Dissolve(5.0, alpha=True)
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    jump ch30_loop



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_out",     
            category=['开放世界'],                         
            prompt="我想带你出去",                             
            unlocked=True,                             
            pool=True                                  
        )
    )


label ow_out:
    $ persistent.monika_topic_count += 1
    if persistent.monika_topic_count == 1:
        m 1fub "哦? 我现在能去其它的地方了? "
        m 7nub "啊, 你一定是趁我不注意把它修好了!"
        m 6hua "好, 我们走!"
        $ enable_esc()
        $ HKBHideButtons()
        jump ow_mc_house
    elif persistent.monika_topic_count >= 2:
        m 6sub "好啊, 我们出发吧!"
        $ enable_esc()
        $ HKBHideButtons()
        jump ow_mc_house


label ow_mc_house:
    window hide
    stop music fadeout 4
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/for u.mp3" fadein 1.0
    scene bg house
    $ persistent.mc_house_count += 1

    if persistent.mc_house_count == 1:
        show monika 1b_gowm at t11
        with dissolve
        m "这里是? "
        show monika 1l_gowm at t11
        with dissolve
        m "啊, 是{color=#000}[OW_mc]{/color}的家啊."
        show monika 2l_gowm at t11
        with dissolve
        m "说实话, 我没有来过这个地方..."
        show monika 2a_gowm at t11
        with dissolve
        m "好吧, [player], 你接下来想去哪?{nw}"
        $ _history_list.pop()
        if persistent.find_new == 1:
            menu:
                m "好吧, [player], 你接下来想去哪?{fast}"
                "sayori的家":
                    jump ow_sayori_home

                "{color=#000}[OW_mc]{/color}的家":
                    jump ow_mc_kitchen

                "沿着街道走走吧":
                    jump ow_street_1

                "去新的地方吧!":
                    $persistent.find_new += 1
                    jump ow_residental_02

                "回去吧":
                    jump ow_go_back

        elif persistent.find_new == 0:
            menu:
                m "好吧, [player], 你接下来想去哪?{fast}"
                "sayori的家":
                    jump ow_sayori_home

                "{color=#000}[OW_mc]{/color}的家":
                    jump ow_mc_kitchen

                "沿着街道走走吧":
                    jump ow_street_1

                "回去吧":
                    jump ow_go_back

    elif persistent.mc_house_count >= 2:
        show monika 2a_gowm at t11
        with dissolve
        m "在外面的感觉真好！"
        show monika 1b_gowm at t11
        with dissolve
        m "[player], 你想去哪?{nw}"
        if persistent.find_new == 1:
            menu:
                m "[player], 你想去哪?{fast}"
                "sayori的家":
                    jump ow_sayori_home

                "{color=#000}[OW_mc]{/color}的家":
                    jump ow_mc_kitchen

                "沿着街道走走吧":
                    jump ow_street_1

                "去新的地方吧!":
                    $persistent.find_new += 1
                    jump ow_residental_02

                "回去吧":
                    jump ow_go_back

        elif persistent.find_new == 0:
            menu:
                m "[player], 你想去哪?{fast}"
                "sayori的家":
                    jump ow_sayori_home

                "{color=#000}[OW_mc]{/color}的家":
                    jump ow_mc_kitchen

                "沿着街道走走吧":
                    jump ow_street_1

                "回去吧":
                    jump ow_go_back

        elif persistent.find_new >= 2:
            menu:
                m "[player], 你想去哪?{fast}"
                "sayori的家":
                    jump ow_sayori_home

                "{color=#000}[OW_mc]{/color}的家":
                    jump ow_mc_kitchen

                "沿着街道走走吧":
                    jump ow_street_1

                "去公园那边吧!":
                    jump ow_residental_02

                "回去吧":
                    jump ow_go_back

                

label ow_sayori_home:
    $ persistent.sa_house_count += 1

    show black zorder 100 with Dissolve(5.0, alpha=True)
    if persistent.sa_house_count == 1:
        stop music fadeout 1.0
        menu:
            "走上楼梯":
                pass
        menu:
            "轻轻推开门":
                pass
        play sound "Submods/To You Beyond the Stars/TYBS_Open World/sounds/open door.ogg"
        pause 2.0      
        hide black
        scene bg sayori_bedroom
        m ".{w=0.1}.{w=0.1}{w=0.1}."
        m "放轻松[player]."
        m "我不会再吓你了, 啊哈哈!"
        play music "Submods/To You Beyond the Stars/TYBS_Open World/music/for u.mp3" fadein 1.0
        jump sa_bedroom
    elif persistent.sa_house_count >= 2:
        hide black
        scene bg sayori_bedroom
        show monika 2k_gowm at t11
        with dissolve
        m "我很好奇 sayori 的房间里面藏了什么, 啊哈哈!"
        jump sa_bedroom


label sa_bedroom:
    hide monika 2k_gowm
    call screen gow_sayori_room
    screen gow_sayori_room:
        imagemap:
            ground "bg/sayori_bedroom.png"
            hotspot (739, 440, 213, 256) action Jump("ow_sa_cow") hover_sound gui.hover_sound
            hotspot (435, 466, 293, 156) action Jump("ow_sa_bed") hover_sound gui.hover_sound
            hotspot (61, 247, 86, 122) action Jump("ow_sa_calendar") hover_sound gui.hover_sound
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("gow_sayori_room"), Jump("ow_sa_menu")] hover_sound gui.hover_sound



label ow_sa_bed:
    m "sayori的床... 还是一如既往的凌乱呢."
    m "不仅是床, 整个房间都是乱的啊..."
    m "她真应该时常收拾一下..."
    m "我曾跟你提过，如果你因为抑郁而不想做某事，你可以做一些像一点一点打扫自己房间之类的小事。"
    m "啊, 不要再去想她干了什么了."
    m "我只是想跟你说, 如果感到心里难受, 可以随时和我说说."
    m "毕竟这个世界上有这么多关心你的人..."
    m "我也是其中之一! 啊哈哈!"
    call screen gow_sayori_room

label ow_sa_cow:
    m "啊, 牛先生, 没想到还能见到你."
    m "sayori自从有了它之后, 就一直把它放在床头."
    m "她好像一直很喜欢这种可爱的东西. 虽然她平时总是表现得很随意, 好像什么都不在意的样子, 但其实她很珍惜那些陪伴自己的小物件."
    m "... 说真的, 我觉得它有点像它的主人."
    m "暖暖的, 让人忍不住想照顾它."
    m "不过...如果是 sayori 的话, 我猜她可能会给它取一个非常可爱的名字, 然后每天对它说早安吧."
    call screen gow_sayori_room

label ow_sa_calendar:
    m "原来这里就是 sayori 的日历啊."
    m "明明只是一个很普通的东西, 但站在这里的时候, 总觉得有一种很特别的感觉."
    m "你看, [player]."
    m "上面记录的不只是日期."
    m "嗯, 如果是我的话, 我可能会把日历当成一个安排计划的工具. 社团活动, 学习, 写作, 重要的事情... 我会想办法把每一天规划好."
    m "可是 sayori 的日历..."
    m "我觉得它更像是在记录'我要和大家一起度过什么'."
    m "..."
    m "这个日历, 感觉像是她留给世界的一小部分温度呢."
    call screen gow_sayori_room

label ow_sa_menu:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg house
    show monika 1b_gowm at t11
    with dissolve
    m "你接下来想去哪?"
    menu:
        "sayori的家":
            jump ow_sayori_home
        
        "{color=#000}[OW_mc]{/color}的家":
            jump ow_mc_kitchen

        "沿着街道走走吧":
            jump ow_street_1

        "回去吧":
            m "好的!"
            jump ow_go_back

#难搞啊...文本好难写
#要是有一个田螺姑娘过来帮我写文本就好了（幻想    