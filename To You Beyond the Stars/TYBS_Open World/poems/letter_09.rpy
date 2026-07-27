init 10 python:
    letter_nine = MyPoem(
        poem_id="letter_to_player_09",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="房子里的大象",   # 诗的标题
        text="""
空荡的房间内,
惟留一头大象.
扭曲的,
不安的,
焦躁的线条,
构成了虚掩着的眼眸,
和垂落的鼻子.
它的身躯非常庞大,
整个房间仿佛是为他而打造的.
它的身躯十分渺小,
没有一个人注视着它.
而它,
即使不被注视,
也不会消失.
永远的,
守护着,
死去的,
永恒.
        """,
        author="monika",
        ex_props={"sad": False}
    )
