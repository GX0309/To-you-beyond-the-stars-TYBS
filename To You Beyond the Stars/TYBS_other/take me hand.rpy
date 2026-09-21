#钢琴播放指定的音乐
#其他部分不再赘述
#
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_music_un_01",
            category=['音乐'],
            prompt="take me hand",
            random=True
        )
    )

label gx_music_un_01:
    m 4eud "[player], 我学了一首新歌!"
    m 7hub "你想听听吗?"
    menu:
        "好啊!":
            $ mas_unlockEVL("gx_music_tmh_again", "EVE")
            jump gx_music_tmh

        "抱歉, 今天不行":
            m 1gksdrb "好吧..."
            m 7kua "等你有空了我再给你弹!"
            $ mas_unlockEVL("gx_music_tmh_again", "EVE")       # 解锁第二个事件注意事件标签，应与下面一致
            return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_music_tmh_again",           # 初始锁定（依赖第一个事件解锁）
            category=['音乐'],
            prompt="你能在为我唱一次take me hand吗?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label gx_music_tmh_again:
        # 指定音乐文件修改路径
    $ music_file = "Submods/To You Beyond the Stars/TYBS_other/music/take me hand.mp3" # 可以同时准备一个显示用的曲名,曲名不可重复
    $ song_display = "take me hand"   # 定义音乐名称 也可以不写直接写在应该出现的对话里面就行了

    # 开始演奏动画
    m "好的，[player]"
    m "让我为你唱一首《[song_display]》吧。" #若不做任何修改这一行中的[song_display] 会显示  若你轻轻坠落...
    show monika at Transform(xpos=-800) with move     # Monika 向左移动
    m "我先准备一下~"
    window hide
    $ store.mas_sprites.zoom_out()                    # 重置 MAS 相机距离
    $ HKBHideButtons()                                # 隐藏按钮
    $ original_music = renpy.music.get_playing(channel='music')  # 保存当前音乐

    # 显示钢琴动画与播放指定音乐
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move       
    play music music_file loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika

    # 音乐结束
    $ wait_time = 212   # 单位 秒  根据实际音乐文件修改
    pause wait_time

    # 结束演奏，收回钢琴 
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $ HKBShowButtons()
    window show
    play music original_music fadein 2.0  # 恢复之前的背景音乐

    m "弹得怎么样？希望你喜欢这首《[song_display]》。"

    return 


label gx_music_tmh:
    # 指定音乐文件修改路径
    $ music_file = "Submods/To You Beyond the Stars/TYBS_other/music/take me hand.mp3" # 可以同时准备一个显示用的曲名,曲名不可重复
    $ song_display = "take me hand"   # 定义音乐名称 也可以不写直接写在应该出现的对话里面就行了

    # 开始演奏动画
    m "好的，[player]"
    m "让我为你弹奏一首《[song_display]》吧。" #若不做任何修改这一行中的[song_display] 会显示  若你轻轻坠落...
    show monika at Transform(xpos=-800) with move     # Monika 向左移动
    m "我先把钢琴搬过来～"
    window hide
    $ store.mas_sprites.zoom_out()                    # 重置 MAS 相机距离
    $ HKBHideButtons()                                # 隐藏按钮
    $ original_music = renpy.music.get_playing(channel='music')  # 保存当前音乐

    # 显示钢琴动画与播放指定音乐
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move       
    play music music_file loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika

    # 音乐结束
    $ wait_time = 212   # 单位 秒  根据实际音乐文件修改
    pause wait_time

    # 结束演奏，收回钢琴 
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $ HKBShowButtons()
    window show
    play music original_music fadein 2.0  # 恢复之前的背景音乐

    m "弹得怎么样？希望你喜欢这首《[song_display]》。"

    return 