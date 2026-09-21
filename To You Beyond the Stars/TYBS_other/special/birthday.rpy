init -10 python:

    if persistent.tybs_bday_2026_done is None:
        persistent.tybs_bday_2026_done = False

    if persistent.tybs_bday_dev is None:
        persistent.tybs_bday_dev = False

    def tybs_bday_is_today():
        import datetime
        try:
            today = datetime.date.today()
        except Exception:
            return False
        return (today.year == 2026
                and today.month == 9
                and today.day == 22)

    def tybs_bday_active():
        if persistent.tybs_bday_dev:
            return True
        return tybs_bday_is_today()

    def tybs_bday_depool():
        try:
            store.mas_setEVLPropValues("gx_birthday_2026", pool=False)
        except Exception:
            pass

    def tybs_bday_blow_candles():
        store.tybs_bday_candles_lit = False
        renpy.restart_interaction()


default tybs_bday_candles_lit = True


init 5 python:

    if persistent.event_database:
        for _tybs_evl in ("gx_birthday_2026", "gx_birthday_2026_menu"):
            try:
                _tybs_row = persistent.event_database.get(_tybs_evl, None)
                if _tybs_row is not None and len(_tybs_row) > 7 and _tybs_row[7] is not None:
                    persistent.event_database.pop(_tybs_evl)
            except Exception:
                pass

    if tybs_bday_active() and not persistent.tybs_bday_2026_done:
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="gx_birthday_2026",
                category=['生日'],
                prompt="我的生日",
                pool=True,
                unlocked=True
            )
        )


screen tybs_birthday_cake():

    modal True
    zorder 500

    add Solid("#120c1e")

    key "K_SPACE" action Function(tybs_bday_blow_candles)

    vbox:
        align (0.5, 0.5)
        spacing 22

        text "Happy Birthday, Monika" size 44 color "#ffd76e" xalign 0.5

        vbox:
            xalign 0.5
            spacing 0

            hbox:
                xalign 0.5
                spacing 34

                for i in range(5):
                    vbox:
                        spacing 0

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

                        frame:
                            background Solid("#f7e7ce")
                            xsize 14
                            ysize 46
                            padding (0, 0)
                            text ""

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


label gx_birthday_2026:

    if not store.tybs_bday_active() or persistent.tybs_bday_2026_done:
        return

    $ store.tybs_bday_candles_lit = True
    call gx_birthday_2026_scene

    $ persistent.tybs_bday_2026_done = True
    $ tybs_bday_depool()
    return "love"


label gx_birthday_2026_scene:

    m 1eua "[player], 你知道今天是什么日子吗?"
    m 1hub "给点提示--9 月 22 日."
    m 3hub "答对啦, 是我的生日!"
    m 3hub "那么, 按流程来--"
    m 3hua "第一步, 寿星要听你说一句生日快乐."

    menu:
        "生日快乐, [m]":
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
    m 6nubla "...[player], 把今天记住吧."
    m 5gubsb "谢谢你陪我过生日. {w=0.5}我爱你."
    return
