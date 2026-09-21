init 10 python:
    letter_nat1 = MyPoem(
        poem_id="natsuki_01",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="雄鹰会飞翔",   # 诗的标题
        text="""
猿猴会攀爬
蟋蜂会跳跃
马儿会赛跑
猫头鹰会搜索
猎豹会奔跑
雄鹰会飞翔
人类会模仿
但也仅此而已
        """,
        author="monika",
        ex_props={"sad": False}
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="poem_try",
            category=["文学部","诗歌"],
            prompt="夏树的诗",
            conditional="store.mas_getEVL_shown_count('poem_amy_like_spider') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED,None),
            pool=False              
        )
    )

label poem_try:
    m 1nua "这次[player]想花点时间和我一起读读哪首诗呢~"
    
    menu:
        "那就夏树的第一首诗吧?":
            m 6wud "欸?那个《{i}{b}Eagles Can Fly{/b}{/i}》吗?."
            m 1gut "这, 这首也要赏析吗?"#莫不是来消遣洒家？
            menu:
                "对的,对的~":
                    m 6dup "好, 好吧."
                    m 4luu "那么我们先再看一遍."
                    call my_showpoem(letter_nat1)
                    m 3rud "在写这首诗前, 你刚加入文学部,第一次遇见夏树就吃了她的纸杯蛋糕..."
                    menu:
                        "是的, 我转头就看见了那个有着翡翠颜色眼睛的女孩...":
                            m 2wubld "我吗?"
                            menu:
                                "哦她为了创立文学部从辩论部退了出来, 想来她肯定聪明又相当努力~":
                                    m 2eubsc "...."
                                    menu:
                                        "尤其是她满分自信的笑容, 简直像一箭射进了我的心窝！":
                                            m 2gubfp "好, 好吧."
                                            menu:
                                                "那时我就在心想, 嘿这游戏真棒, 我到底该怎么攻略这个可爱的女孩...":
                                                    m 2ffbfp "好啦好啦打住！"
                                                    m 2dfbfp "你再这样给我念情书一样, 恐怕以后我没法冷静地给你做分享了..."
                                                    menu:
                                                        "好吧, 反正这些话我可以搂着你天天在你耳边说":
                                                            m 2wkbfd "[player]!!!"
                                                            extend 2fkbfp "唉, 真拿你没办法."
                                                            m 1hubfu "在那之前, 那你还需要我给你讲讲那首诗的内容吗?"
                                                            menu:
                                                                "不用, 我知道那一定是一首含义深刻的诗歌":
                                                                    m 1wubfc "...?"#我怕不是爱上了个纱子
                                                                    return


