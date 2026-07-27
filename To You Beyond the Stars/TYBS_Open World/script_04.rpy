
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
    hide black
    scene bg residential_02
    if persistent.find_new == 2:
        show moika 6j_gowm at t11
        with dissolve
        m "哇! 全新的景色!"
        show monika 7t_gowm at t11
        with dissolve
        m "来吧[player], 我们往前走走!"
        jump park

    if persistent.find_new >= 3:
        show monika 9b_gowm at t11
        with dissolve
        m "啊, 树先生, 你们好啊!"
        show monika 5a_gowm at t11
        with dissolve
        m "[player], 我们走!"
        jump park

label park:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg park
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
            jump road

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
    hide black
    scene bg park_lake
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/music/park_lake.mp3"
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
    hide black
    scene bg park_lake
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
    hide black with Dissolve(2.o, alpha=True)
    scene bg road
    if persistent.road_count == 1:
        jump ow_road_01
    else:
        jump ow_road_02

label ow_road_01:
    show monika 7t_gowm at t11
    with dissolve
    m "这里有一条新路!"
    show monika 8j_gowm at t11
    with dissolve
    m "看起来它通向两个地方!"
    show monika 9b_gowm at t11
    with dissolve
    m "[player], 你想往那边走呢?"
    menu:
        "去左边吧!":
            jump ow_playground

label ow_playground:
    jump ow_go_back

label ow_road_02:
    jump ow_go_back
