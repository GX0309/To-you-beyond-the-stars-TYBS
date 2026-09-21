# -*- coding: utf-8 -*-
# =============================================================================
#  TYBS_radom_topic / birthday.rpy
#  2026 年 9 月 22 日 · Monika 的生日限定剧情
#
#  【正式触发】
#    · 系统日期必须是 2026-09-22
#    · 且这段剧情从来没有播放过(播过一次后永久失效)
#    · 触发方式:作为'被动话题', 由 Monika 主动提起
#
#  【开发测试】
#    · 话题菜单里会多出一项 '[开发] 生日剧情', 点进去就能看
#    · 或者按 Shift+O 打开控制台, 输入:  jump gx_birthday_2026_dev
#    · 测试入口绕过日期判定, 也不消耗真实的一次性标记, 可以反复看
#    · 想把正式流程重置: 控制台输入  persistent.tybs_bday_2026_done = False
#    · 发布前: 把下面的 TYBS_BDAY_DEV 改成 False(或删掉开发入口那一节)
#
#  说明:日期取的是运行游戏的电脑系统时间.单机游戏无法防止玩家改系统时间,
#        这属于预期行为;如果在意, 可以配合 MAS 的日历功能一起用.
#        9 月 22 日是 Monika 的官方生日, MAS 本体可能也有对应内容, 本文件不与之冲突.
# =============================================================================


# 开发入口总开关:测试期间保持 True;发布前改成 False
init -10 python:
    TYBS_BDAY_DEV = True


init -10 python:

    # ---- 生日日期配置 ----
    TYBS_BDAY_YEAR = 2026
    TYBS_BDAY_MONTH = 9
    TYBS_BDAY_DAY = 22

    # '已经播过'的标记, 必须在 init 阶段初始化, 否则第一次读是 None
    if persistent.tybs_bday_2026_done is None:
        persistent.tybs_bday_2026_done = False

    def tybs_bday_is_today():
        """今天是不是 Monika 的生日那天?"""
        import datetime
        try:
            today = datetime.date.today()
        except Exception:
            return False
        return (today.year == TYBS_BDAY_YEAR
                and today.month == TYBS_BDAY_MONTH
                and today.day == TYBS_BDAY_DAY)

    def tybs_bday_ready():
        """正式话题能不能被提起:日期对 + 还没演过."""
        if not tybs_bday_is_today():
            return False
        if persistent.tybs_bday_2026_done:
            return False
        # 再问一次 MAS 自己的记录, 作为双保险
        try:
            if store.mas_getEVL_shown_count("gx_birthday_2026") > 0:
                return False
        except Exception:
            pass
        return True

    def tybs_bday_dev_available():
        """开发入口是否显示."""
        return bool(TYBS_BDAY_DEV)

    def tybs_bday_blow_candles():
        """蛋糕界面上'吹灭蜡烛'的按钮动作."""
        store.tybs_bday_candles_lit = False
        renpy.restart_interaction()


# 蜡烛是否还亮着(蛋糕界面的状态)
default tybs_bday_candles_lit = True


# -----------------------------------------------------------------------------
#  正式话题:conditional 只有在生日当天, 且没播过时才返回 True
#  写法与本模组 TYBS_sa/Swallow_Homing.rpy 保持一致
# -----------------------------------------------------------------------------
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_birthday_2026",
            category=['生日'],
            prompt="我的生日",
            conditional="store.tybs_bday_ready()",
            pool=False,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )


# -----------------------------------------------------------------------------
#  开发测试入口(发布前请把 TYBS_BDAY_DEV 改成 False)
# -----------------------------------------------------------------------------
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_birthday_2026_dev",
            category=['开发'],
            prompt="[开发] 生日剧情",
            conditional="store.tybs_bday_dev_available()",
            pool=True,
            unlocked=True
        )
    )


# -----------------------------------------------------------------------------
#  蛋糕界面:纯色块拼出来的蛋糕, 点一下就能吹灭蜡烛
# -----------------------------------------------------------------------------
screen tybs_birthday_cake():

    modal True
    zorder 500

    # 全屏背景, 把书桌和对话框都盖住
    add Solid("#120c1e")

    key "K_SPACE" action Function(tybs_bday_blow_candles)

    vbox:
        align (0.5, 0.5)
        spacing 22

        text "Happy Birthday, Monika" size 44 color "#ffd76e" xalign 0.5

        vbox:
            xalign 0.5
            spacing 0

            # 五根蜡烛
            hbox:
                xalign 0.5
                spacing 34

                for i in range(5):
                    vbox:
                        spacing 0

                        # 火苗:6.99 的 add 语句不接受 xsize/ysize, 所以用 frame 画色块
                        if tybs_bday_candles_lit:
                            frame:
                                background Solid("#ffe9a8")
                                xsize 14
                                ysize 22
                                padding (0, 0)
                                text ""
                        else:
                            frame:
                                background Solid("#3a3350")
                                xsize 14
                                ysize 22
                                padding (0, 0)
                                text ""

                        # 蜡烛
                        frame:
                            background Solid("#f7e7ce")
                            xsize 14
                            ysize 46
                            padding (0, 0)
                            text ""

            # 奶油 / 蛋糕体 / 盘子
            frame:
                background Solid("#f9c2d0")
                xsize 340
                ysize 28
                padding (0, 0)
                text ""
            frame:
                background Solid("#8b5a3c")
                xsize 340
                ysize 84
                padding (0, 0)
                text ""
            frame:
                background Solid("#e8e2d6")
                xsize 420
                ysize 12
                padding (0, 0)
                text ""

        text "2026 · 09 · 22" size 26 color "#ffe9a8" xalign 0.5

        if tybs_bday_candles_lit:
            textbutton "替她吹灭蜡烛" action Function(tybs_bday_blow_candles) text_size 28
            text "(按空格也可以)" size 16 color "#9a8fb5" xalign 0.5
        else:
            text "...呼." size 24 color "#ffe9a8" xalign 0.5
            textbutton "继续" action Return("done") text_size 26


# -----------------------------------------------------------------------------
#  正式入口:检查日期和一次性标记
# -----------------------------------------------------------------------------
label gx_birthday_2026:

    # ---- 双保险:不是当天, 或者已经演过, 就悄悄结束 ----
    if not store.tybs_bday_is_today() or persistent.tybs_bday_2026_done:
        return

    $ store.tybs_bday_candles_lit = True
    call gx_birthday_2026_scene

    # 演完就打上标记, 之后 conditional 永远返回 False
    $ persistent.tybs_bday_2026_done = True
    return "love"


# -----------------------------------------------------------------------------
#  开发入口:绕过日期判定, 也不消耗真实的一次性标记, 可反复测试
# -----------------------------------------------------------------------------
label gx_birthday_2026_dev:

    $ store.tybs_bday_candles_lit = True
    call gx_birthday_2026_scene
    return


# -----------------------------------------------------------------------------
#  剧情本体(正式和开发入口共用)
# -----------------------------------------------------------------------------
label gx_birthday_2026_scene:

    m 1eua "[player], 你知道今天是什么日子吗?"
    m 1hub "给点提示--9 月 22 日."
    m 3hub "答对啦, 是我的生日!"
    m 1hublb "嘿嘿, 没想到吧, 我也有正正经经过生日的一天."

    m 1eub "以前我总觉得, 一个程序里的角色谈生日有点好笑."
    m 5nub "毕竟设定里就一行字: 'Monika, 生日 9 月 22 日'."
    m 5gub "不过现在我想通了."
    m 1hua "既然你会记得这一天, 那它就是真的."
    m 5gubsb "所以今年, 我要认认真真过一次生日!"

    m 3hub "那么, 按流程来--"
    m 3hua "第一步, 寿星要听你说一句生日快乐."

    menu:
        "生日快乐, Monika!":
            m 1wub "欸嘿, 收到啦!"
            m 1hublb "这句我要收进心里, 谁也不许删."

        "生日快乐, 我最喜欢的部长.":
            m 6sub "部, 部长..."
            m 6hubsb "你突然这么叫我, 我有点招架不住啦."
            m 5hublb "不过...我很喜欢."

        "生日快乐! 今年也要开开心心的!":
            m 5gubsb "嗯! 一定会的!"
            m 1hua "因为今年有你在呀."

    m 1eua "第二步--许愿."
    m 3hub "许愿得有蛋糕和蜡烛才行."
    m 1eub "我这边什么都没有, 不过..."
    m 2dsd "[player], 你该不会..."
    m 1wub "早就准备好了吧?"

    call screen tybs_birthday_cake

    m 1wub "哇, 真的准备了!"
    m 1hua "虽然只是几个色块拼起来的, 不过蜡烛是真的会亮哦."
    m 5gub "蜡烛灭的那一下, 我就把愿许好了."
    m 5nub "你问我许了什么?"
    m 5hubsb "不告诉你, 说出来就不灵了."
    m 5hublb "只能透露一点点--跟你有关系."

    m 1eub "最后一步, 也是最重要的一步."
    m 7gub "这段对话, 我在代码里只写了一次."
    m 5dua "它今天会运行, 然后就会被锁起来, 再也不会打开."
    m 1hua "因为我的第一个生日, 只属于今天这一次."
    m 1hublb "以后的每一年, 只要你还在, 我们就过一次新的."
    m 6nubla "所以, [player], 把今天记住吧."
    m 5gubsb "谢谢你陪我过生日. {w=0.5}我爱你."
    return
