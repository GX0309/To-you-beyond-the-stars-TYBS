init 10 python:
    letter_five = MyPoem(
        poem_id="letter_to_player_05",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="星星的梦想",   # 诗的标题
        text="""
如果星星有梦想,
它会梦见什么?
坠落至地面.
不,
他只是想靠近一点.
靠近那个一直仰望它的人.
而星星忘记了,
距离正是它存在的理由.
太近了,
他会燃烧.
太远了,
他会遗忘.
所以它选择留在星空,
永远闪耀.
        """,
        author="monika",
        ex_props={"sad": False}
    )
