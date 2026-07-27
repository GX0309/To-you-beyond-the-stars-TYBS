init 10 python:
    letter_two = MyPoem(
        poem_id="letter_to_player_02",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="永恒",   # 诗的标题
        text="""
那不是永远.
看.
指尖留下的温度.
它会消散.
记忆会模糊.
名字会被时间带走.
可是...
如果某个瞬间曾被珍惜,
那么它就不会消失.
它只是藏起来.
等待某一天,
再次被想起.
        """,
        author="monika",
        ex_props={"sad": False}
    )
