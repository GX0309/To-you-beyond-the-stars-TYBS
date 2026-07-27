init 10 python:
    letter_ten = MyPoem(
        poem_id="letter_to_player_10",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="'珍藏'的回忆",   # 诗的标题
        text="""
我的桌子上放着一个礼物盒.
它的盖子从未被打开,
我也从未敢向里窥探.
直到有一天,
盒子里的东西开始散发腥臭,
我按耐不住好奇打开了它.
里面不是奇珍异宝,
不是真金白银,
而是一份份我珍藏的,
早已腐烂的,
回忆.
        """,
        author="monika",
        ex_props={"sad": False}
    )
