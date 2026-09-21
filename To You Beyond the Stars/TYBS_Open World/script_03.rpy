#03讲述：流程2（ddlc原版）学校
translate chinese style mas_monika_poem_text:#字体样式
    font "gui/font/SentyPea.ttf"
    size 29

init 10 python:
    class MyPoem:
        def __init__(
            self,
            poem_id,
            category,
            prompt,
            paper=None,
            title="",
            text="",
            author="monika",
            ex_props=None
        ):
            if poem_id in store.mas_poems.poem_map:
                raise Exception("poem_id {0} already exists in the poem map.".format(poem_id))
            
            self.poem_id = poem_id
            self.category = category
            self.prompt = prompt
            self.paper = paper
            self.title = title
            self.text = text
            self.author = author
            self.ex_props = dict() if ex_props is None else ex_props
            
            store.mas_poems.poem_map[poem_id] = self
        
        def is_seen(self):
            return self.poem_id in store.persistent._mas_poems_seen
        
        def get_shown_count(self):
            return store.persistent._mas_poems_seen.get(self.poem_id, 0)

# 展示信件的公共调用函数，不用改动
label my_showpoem(poem=None, paper=None, background_action_label=None):
    if poem == None:
        return

    $ is_valid_poem = True  

    if paper is None:
        if hasattr(poem, 'paper') and poem.paper is not None:
            $ paper = poem.paper
        elif hasattr(poem, 'category'):
            $ paper = mas_poems.paper_cat_map.get(poem.category, "paper")
        else:
            $ paper = "paper"

    play sound page_turn
    window hide
    $ afm_pref = renpy.game.preferences.afm_enable
    $ renpy.game.preferences.afm_enable = False

    $ author_font = mas_poems.author_font_map.get(getattr(poem, 'author', 'monika'), "monika_text")
    show screen mas_generic_poem(poem, paper=paper, _styletext=author_font)

    with Dissolve(1)

    if background_action_label and renpy.has_label(background_action_label):
        call expression background_action_label

    $ pause()

    hide screen mas_generic_poem
    with Dissolve(.5)

    $ renpy.game.preferences.afm_enable = afm_pref
    window auto

    if is_valid_poem and hasattr(poem, 'prompt') and poem.prompt:
        if poem.poem_id in persistent._mas_poems_seen:
            $ persistent._mas_poems_seen[poem.poem_id] += 1
        else:
            $ persistent._mas_poems_seen[poem.poem_id] = 1

    return

init 10 python:
    # 第一封情书
    letter_x = MyPoem(
        poem_id="first_letter_to_player",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="梦的回信",   # 诗的标题
        text="""
我曾以为，
世界不过是一页写好的故事，
每一句对白，
每一个相遇，
都只是被安排好的注脚。

直到你的目光停留在这里。

如果未来只是一条漫长的路，
如果我们之间隔着看不见的距离，
那也没关系。

我会把每一句想对你说的话，
藏进诗里。

等某一天，
你再次翻开它的时候，
希望你能发现——

每一个字，
都曾因为你而闪耀。

        """,
        author="monika",
        ex_props={"sad": False}
    )

label ow_street_1:
    $ persistent.street_count += 1
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg residential
    if persistent.street_count == 1:
        show monika 9t_gowm at t11
        with dissolve
        m "新场景!"
        show monika 1k_gowm at t11
        with dissolve
        m "我还没在游戏中到过这个地方呢!"
        show monika 10a_gowm at t11
        with dissolve
        m "[player], 你想去哪?{nw}"
        jump ow_school_menu
    else:
        show monika 9t_gowm at t11
        with dissolve
        m "好清新的空气!"
        show monika 10k_gowm at t11
        with dissolve
        m "[player], 你想去哪?{nw}"
        jump ow_school_menu


label ow_school_corridor:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg corridor
    m "接下来你要去哪呢?{nw}"
    menu:
        m "接下来你要去哪呢?{fast}"
        "去教室吧":
            jump ow_classroom

        "去社团活动室":
            jump ow_club
        
        "回太空教室吧":
            jump ow_go_back


label ow_school_menu:
    menu:
        m "[player], 你想去哪?{fast}"
        "去学校吧":
            jump ow_school_corridor

        "原路返回":
            jump ow_mc_house

        "回太空教室吧":
            m "嗯!"
            m "我们回去吧!"
            jump ow_go_back


label ow_classroom:
    $ persistent.classroom_count += 1
    stop music fadeout 1.0
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg classroom
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/old classroom.mp3" fadein 1.0
    if persistent.classroom_count == 1:
        show monika 3b_gowm at t11
        with dissolve
        m "嘿[player]..."
        show monika 10t_gowm at t11
        with dissolve
        m "你可以帮我一个大忙吗？"
        show monika 10b_gowm at t11
        with dissolve
        m "其实，我正在组建一个新的！"
        show monika 9t_gowm at t11
        with dissolve
        m "{b}文学部!!!{/b}"
        show monika 5a_gowm at t11
        with dissolve
        m "怎么样? 是不是感觉有些似曾相识?"
        show monika 3j_gowm at t11
        with dissolve
        m "所以, 你现在想干点什么? 我亲爱的部员?"
        hide monika
        jump ow_classroom_menu
    else:
        show monika 5a_gowm at t11
        with dissolve
        m "我们又回来了呢, [player]!"
        m "现在你想干点什么?"
        hide monika
        jump ow_classroom_menu

label ow_classroom_menu:
    menu:
        "我随便看看":
            jump ow_classroom_around

        "咱们出去吧":
            jump ow_corridor_menu
        
        "让我们去文学部看看吧!":
            jump ow_club
        
        "回太空教室吧":
            m "好的!"
            jump ow_go_back

label ow_classroom_around:
    hide monika
    call screen gow_school_class
    screen gow_school_class:
        imagemap:
            ground "bg/class.png"
            hotspot (242, 530, 363, 563) action Jump("ow_letter") hover_sound gui.hover_sound
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("gow_school_class"), Jump("ow_classroom_menu")] hover_sound gui.hover_sound

label ow_letter:  
    if persistent.letter_count == 0:
        show monika 4d_gowm at t11
        with dissolve
        m "你猜怎么着, [player]?"
        show monika 4k_gowm at t11
        with dissolve
        m "我在这张桌子里面发现了一封信!"
        show monika 3t_gowm at t11
        with dissolve
        m "是写给你的!"
        show monika 2j_gowm at t11
        with dissolve
        m "我把它放在characters文件夹里了, 记得看!"
        hide monika
        python:
            message = """\
亲爱的[player]:
其实我纠结了好一会儿要不要写这封信.
因为啊, 把这种话直接说出来, 总感觉有一点害羞呢.
不过想了想...
有些想法如果一直藏起来, 好像也挺可惜的.
所以, 我决定偷偷写下来!
你知道吗?
有时候一个人变得特别, 并不是因为做了什么惊天动地的事情.
可能只是一次普通的聊天.
一次认真倾听.
或者是在某个瞬间, 让别人觉得...
和这个人在一起的时候, 好像很安心.
我觉得那是一种很珍贵的感觉.
而你呢...
好像不知不觉就做到了.
你总是会注意到一些别人忽略的小事.
也总是愿意花时间去理解别人.
这样的你, 真的很特别哦!
所以啊...
如果有一个人会期待和你聊天.
会记得你说过的话.
会因为看到你的消息而开心.
你应该不会觉得奇怪吧?
因为那个人...
可能只是很喜欢和你待在一起而已.
我爱你, [player]!
欸嘿嘿!
谢谢你一直愿意听我说话!
                ——[m]

啊哈哈, 被我吓到了吗?
"""
            _write_txt("/characters/致星海彼端的你.txt", message)
        $ persistent.letter_count += 1
        call screen gow_school_class

    else:
        menu:
            "将手伸进桌洞":
                call my_showpoem(letter_x)  # 调用上面注册的第一封信
                call screen gow_school_class







label ow_corridor_menu:
    stop music fadeout 1.0
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/for u.mp3" fadein 1.0
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg corridor
    menu:
        m "接下来你要去哪呢?{fast}"
        "去教室吧":
            jump ow_classroom

        "去社团活动室":
            jump ow_club
        
        "原路返回!":
            jump ow_residental

        "回家吧":
            m "好的!"
            m "要带我常出来活动一下哟!"
            jump ow_go_back




label ow_club:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg club
    $ persistent.club_count += 1
    if persistent.club_count == 1:
        show monika 4j_gowm at t11
        with dissolve
        m "哇... 我真的没想到我还能再看到这里!"
        show monika 6t_gowm at t11
        with dissolve
        m "现在, 这里只属于我们两个人!"
        show monika 5a_gowm at t11
        with dissolve
        m "你知道吗? 以前我总觉得, 文学部最重要的是书, 诗, 还有那些活动."
        show monika 10t_gowm at t11
        with dissolve
        m "但是现在想想..."
        show monika 10j_gowm at t11
        with dissolve
        m "最重要的还是有人愿意听我说这些乱七八糟的话!"
        show monika 3k_gowm at t11
        with dissolve
        m "既然教室是空的, 要不要陪我在这里待一会?"
        show monika 3t_gowm at t11
        with dissolve
        m "我们可以写一首诗, 喝杯咖啡, 或者... 什么都不做也可以."
        show monika 2b_gowm at t11
        with dissolve
        m "毕竟, 有时候最好的故事, 不一定需要写下来."
        show monika 9s_gowm at t11
        with dissolve
        m "只要有人和你一起经历, 就已经算是一篇很棒的作品了, 对吧?"
        show monika 5a_gowm at t11
        with dissolve
        m "那么, 你想干什么呢, 我亲爱的部员?"
        jump ow_club_menu

    else:
        show monika 6t_gowm at t11
        with dissolve
        m "旧地重游的感觉真不错!"
        show monika 5j_gowm at t11
        with dissolve
        m "[player], 你想干什么?"
        jump ow_club_menu

label ow_club_menu:
    menu:
        "[m], 你能给我写首诗吗?":
            if persistent.ra_po >= 10:
                show monika 3q_gowm at t11
                with dissolve
                m "抱歉[player], 我目前没有什么好的灵感..."
                show monika 4o_gowm at t11
                with dissolve
                m "或许再过几天, 我一定能写出更好的诗的!"
                show monika 3b_gowm at t11
                with dissolve
                m "你想再读一遍以前的诗吗?{nw}"
                menu:
                    m "你想再读一遍以前的诗吗?{fast}"
                    "好啊":
                        $ persistent.ra_po == 0
                        $ persistent.read_letters = []
                        call ow_poem
                    
                    "我看我还是耐心等待吧":
                        show monika 8t_gowm at t11
                        with dissolve
                        m "好的!"
                        show monika 9j_gowm at t11
                        with dissolve
                        m "保持耐心, 好吗?"
                        jump ow_club_menu

            else:
                call ow_poem
        
        "[m], 我想回去了":
            show monika 3a_gowm at t11
            m "嗯!"
            jump ow_go_back

        "我们出去看看吧!":
            show monika 4b_gowm at t11
            m "好的!"
            jump ow_corridor_menu


label ow_residental:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide black
    scene bg residential
    jump ow_school_menu




