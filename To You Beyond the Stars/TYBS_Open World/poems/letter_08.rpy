init 10 python:
    letter_eight = MyPoem(
        poem_id="letter_to_player_08",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="时针间的空白",   # 诗的标题
        text="""
我看着墙上的时钟,
时针一点一点地转.
滴答.
滴答.
突然,
声音停止了.
我的世界失去了意义.
只剩杂乱的,
无序的,
无尽的线条.

然后我醒了.
滴答.
滴答.
滴答.
        """,
        author="monika",
        ex_props={"sad": False}
    )
