
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_find_new",
            category=['开放世界'],
            prompt="新地方",
            random=True
        )
    )

label ow_find_new:
    m 4eud "[player], 我最近在外面发现了一个全新的地方!"
    m 7hua "如果你有时间的话, 一定要带我去看看哟!"
    $ persistent.find_new += 1
    return

label ow_residental_02:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg residential_02
    hide black
    if persistent.find_new == 2:
        show moika 3j_gowm at t11
        with dissolve
        m "哇! 全新的景色!"
        show monika 7t_gowm at t11
        with dissolve
        m "来吧[player], 我们往前走走!"
        jump park

    if persistent.find_new >= 3:
        show monika 10b_gowm at t11
        with dissolve
        m "啊, 树先生, 你们好啊!"
        show monika 5a_gowm at t11
        with dissolve
        m "[player], 我们走!"
        jump park

label park:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg park
    hide black
    $ persistent.park_count += 1
    if persistent.park_count == 1:
        show monika 5j_gowm at t11
        with dissolve
        m "[player]! 是公园欸!"
        show monika 7t_gowm at t11
        with dissolve
        m "{cps=*2}我都快忘了上一次去公园是什么时候...{/cps}{nw}"
        show monika 5a_gowm at t11
        with dissolve
        m "[player], 我们干点什么呢?{nw}"
        jump park_menu
    else:
        show monika 10a_gowm at t11
        with dissolve
        m "外面的感觉真不错!"
        show monika 5a_gowm at t11
        with dissolve
        m "[player], 咱们干点什么呢?{nw}"
        jump park_menu

label park_menu:
    m "[player], 咱们干点什么呢?{fast}"
    menu:
        "我们在附近转转吧":
            $ persistent.lake_count += 1
            if persistent.lake_count == 1:
                jump ow_find_lake
            else:
                jump ow_park_menu_2

        "我们回去吧":
            m "好, 咱们走!"
            jump ow_mc_house

        "我想回太空教室了":
            m "好的!"
            m "外面的景色真不错!"
            m "[player], 要常带我出来哦!"
            jump ow_go_back

label ow_park_menu_2:
    show monika 5a_gowm at t11
    with dissolve
    m "我们去哪?{nw}"
    menu:
        m "我们去哪?{fast}"
        "去湖边":
            jump ow_lake_02

        "回去吧":
            jump ow_mc_house

        "往前走走看?":
            jump ow_road

        "回太空教室":
            m "好的!"
            m "今天玩得很开心哦!"
            jump ow_go_back
label ow_find_lake:
    show monika 7b_gowm at t11
    with dissolve
    m "好啊!"
    show monika 10j_gowm at t11
    with dissolve
    m "欸[player], 你看那边!"
    show monika 5a_gowm at t11
    with dissolve
    m "是湖!"
    show monika 7t_gowm at t11
    with dissolve
    m "我们过去看看吧!"
    menu:
        "好":
            pass
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/music/park_lake.mp3"
    scene bg park_lake
    hide black
    show monika 5a_gowm at t11
    with dissolve
    m "[player]快看, 湖水真漂亮, 不是么?"
    show monika 7b_gowm at t11
    with dissolve
    m "经常出来看看风景有助于心情哦!"
    show monika 6j_gowm at t11
    with dissolve
    m "所以要带我常出来哦?"
    show monika 7t_gowm at t11
    with dissolve
    m "欸嘿嘿!"
    menu:
        "要不要来玩水?":
            jump ow_play_water

        "咱们回去吧":
            jump ow_mc_house

        "[m], 我想回太空教室了":
            jump ow_go_back
    
label ow_lake_menu:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg park_lake
    hide black
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/park_lake.mp3" fadein 1.0
    menu:
        "要不要来玩水?":
            jump ow_play_water

        "咱们回去吧":
            jump ow_mc_house

        "[m], 我想回太空教室了":
            jump ow_go_back

label ow_play_water:
    show monika 5a_gowm at t11
    with dissolve
    m "好啊!"
    menu:
        "把手伸进水中":
            pass
    show black zorder 100 with Dissolve(2.0, alpha=True)
    pause 1.0
    stop music fadeout 1.0
    play sound "Submods/To You Beyond the Stars/TYBS_Open World/sounds/hand_in_water.ogg"
    pause 1.5
    m "[player], 水里凉快吗?"
    menu:
        "... 我觉得挺凉的吧":
            pass
    m "啊哈哈, 果然有些东西还是得亲身体验一下呢!"
    pause 1.0
    play sound "Submods/To You Beyond the Stars/TYBS_Open World/sounds/hand_in_water_monika.ogg"
    pause 2.0
    m "果然很凉快呢!"
    m "欸嘿嘿, 我刚刚还以为湖水会是那种很温柔的温度."
    m "你觉得如果我把手一直放在这里, 会不会有小鱼过来看看?"
    m "说不定它们会觉得奇怪."
    pause 1.0
    m "..."
    m "[player], 你知道吗?"
    m "平时, 我感觉你总是在赶时间, 很少会停下来感受这些没有目的的小事."
    m "所以, 偶尔像这样也不错!"
    m "只是站在湖边, 和你一起玩水..."
    m "感觉今天会变成一个很美好的回忆呢!"
    menu:
        "如果你想的话, 我们可以经常来":
            pass
    m "真的吗? "
    m "这可是你自己说的哟?"
    m "那就这么说定了!"
    m "[m] 和 [player] 会一起创造出更多美好的回忆!"
    pause 2.0
    m "走吧[player], 路还长着呢!"
    hide black with Dissolve(2.0, alpha=True)
    scene bg park_lake
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/park_lake.mp3" fadein 1.0
    menu:
        "向前走走看吧":
            jump ow_road
        
        "原路返回":
            jump ow_mc_house

        "我想回太空教室":
            m "好吧!"
            m "我很期待下一次出行!"
            jump ow_go_back

label ow_road:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/street_school.mp3"
    scene bg road_02
    hide black
    $ persistent.count += 1
    if persistent.road_count == 1:
        jump ow_road_01
    else:
        jump ow_road_02

label ow_road_01:
    if persistent.count == 1:
        show monika 7t_gowm at t11
        with dissolve
        m "这里有一条新路!"
        show monika 8j_gowm at t11
        with dissolve
        m "看起来它通向两个地方!"
        show monika 9b_gowm at t11
        with dissolve
        m "[player], 你想往那边走呢?{nw}"
        menu:
            m "[player], 你想往那边走呢?{fast}"
            "去左边吧!":
                $ persistent.playground = True
                jump ow_playground

            "去右边吧!":
                $ persistent.playstore = True
                jump ow_playstore

    else:
        show monika 3k_gowm at t11
        with dissolve
        m "熟悉的分叉小路呢!"
        m "[player], 你想往哪边走呢?{nw}"
        menu:
            m "[player], 你想往哪边走呢?{fast}"
            "去左边吧!":
                $ persistent.playground = True
                jump ow_playground

            "去右边吧!":
                $ persistent.playstore = True
                jump ow_playstore
       

label ow_road_02:
    show monika 3k_gowm at t11
    with dissolve
    m "熟悉的分叉小路呢!"
    m "[player], 你想往哪边走呢?{nw}"
    menu:
        m "[player], 你想往那边走呢?{fast}"
        "去游乐场那边吧!":
            jump ow_playground

        "去电玩城那边!":
            jump ow_playstore

label ow_playground:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg play_ground
    hide black
    $ persistent.pg_count += 1
    if persistent.pg_count == 1:
        show monika 7k_gowm at t11
        with dissolve
        m "啊[player], 是游乐园!"
        show monika 7j_gowm at t11
        with dissolve
        m "哇...安静的游乐园是这样子的呢!"
        show monika 6q_gowm at t11
        with dissolve
        m "有些不可思议..."
        show monika 10k_gowm at t11
        with dissolve
        m "不过啊, 这里有点像属于我们二人的秘密基地呢!"
        show monika 5a_gowm at t11
        with dissolve
        m "虽然一个人都没有, 但是我并不感到寂寞哦?"
        show monika 10b_gowm at t11
        with dissolve
        m "因为有你在这里!"
        show monika 7a_gowm at t11
        with dissolve
        m "[player], 你想干点什么?{nw}"
        jump ow_pg_menu
    else:
        show monika 8k_gowm at t11
        with dissolve
        m "无人的游乐园!"
        show monika 7t_gowm at t11
        with dissolve
        m "[player], 你想干点什么?{nw}"
        jump ow_pg_menu

label ow_pg_menu:
    menu:
        m "[player], 你想干点什么?{fast}"
        "查看闸机口":
            jump ginkgo_bookmark

        "往前走":
            jump ow_road_03

        "回太空教室":
            m "好!"
            m "天, 我们玩得真开心!"
            jump ow_go_back

label ginkgo_bookmark:
    show monika 10j_gowm at t11
    with dissolve
    m "欸[player], 你看那边!"
    show monika 7t_gowm at t11
    with dissolve
    m "有一片银杏叶落在闸机口旁边了呢!"
    show monika 5a_gowm at t11
    with dissolve
    m "啊, 这个地方应该没有落叶这一说的才对吧?"
    show monika 3d_gowm at t11
    with dissolve
    m "嗯... 真奇怪呢?"
    show monika 10k_gowm at t11
    with dissolve
    m "可惜我不能把这里的东西带回太空教室!"
    show monika 3t_gowm at t11
    with dissolve
    m "如果它变成一枚书签的话, 肯定很好看!"
    show monika 10b_gowm at t11
    with dissolve
    m "走吧[player], 前面还有路呢!"
    jump ow_road_03

label ow_playstore:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg play_outside
    hide black
    show monika 7k_gowm at t11
    with dissolve
    m "电玩城!"
    show monika 5a_gowm at t11
    with dissolve
    m "看起来不错呢!"
    show monika 3b_gowm at t11
    with dissolve
    m "我们要不要进去瞧瞧呢?{nw}"
    menu:
        m "我们要不要进去瞧瞧呢?{fast}"
        "好啊":
            m "我们走!"
            jump ow_playstore_inside
            
        "往前走走吧!":
            m "嗯!"
            m "下次一定要来看看哦!"
            jump ow_road_03

label ow_playstore_inside:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/only u.mp3" fadein 1.0
    scene bg play_inside
    hide black 
    show monika 9k_gowm at t11
    with dissolve
    m "[player], 这里有好多游戏机呢?"
    show monika 5a_gowm at t11
    with dissolve
    m "你愿意和我一起玩玩吗?{nw}"
    menu:
        m "你愿意和我一起玩玩吗?{fast}"
        "好啊":
            jump ow_ps_ok

        "算了吧":
            m "啊, 好吧!"
            m "没关系, 我们下次再来!"
            jump ow_ps_menu

label ow_ps_menu:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/for u.mp3" fadein 1.0
    scene bg play_outisde
    hide black 
    show monika 7t_gowm at t11
    with dissolve
    m "又回来了呢?"
    show monika 5a_gowm at t11
    with dissolve
    m "往哪走走吧?{nw}"
    menu:
        m "往哪走走吧?{fast}"
        "回公园":
            jump park

        "往另一条路走走?":
            jump ow_road_03

        "我累了, 回去吧":
            jump ow_go_back

label ow_ps_ok:
    show monika 6t_gowm at t11
    with dissolve
    m "好的!"
    show monika 3p_gowm at t11
    with dissolve
    m "嗯... 让我准备一下..."
    call updateconsole("launching game.exe", "Error")
    show monika 3g_gowm at t11
    with dissolve
    m "怎么会!"
    show monika 4f_gowm at t11
    with dissolve
    m "我再试一下..."
    call updateconsole("Restarting...", "Error")
    call hideconsole
    show monika 7l_gowm at t11
    with dissolve
    m "啊, 看起来这里的游戏机坏了呢..."
    show monika 3m_gowm at t11
    with dissolve
    m "没关系, 也许下一次它就被修好了呢!"
    show monika 6t_gowm at t11
    with dissolve
    m "来吧[player], 我们走!"
    jump ow_road_03

    
