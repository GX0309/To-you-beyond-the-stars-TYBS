init 10 python:
    letter_three = MyPoem(
        poem_id="letter_to_player_03",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="奇迹",   # 诗的标题
        text="""
一颗落下的雨滴.
一束微弱的光.
一个被遗忘的瞬间.
它们都普通得不像答案.
可是...
当有人愿意停下脚步,
去看见它.
去珍惜它.
它便成为了,
只属于某个人的奇迹.
        """,
        author="monika",
        ex_props={"sad": False}
    )
