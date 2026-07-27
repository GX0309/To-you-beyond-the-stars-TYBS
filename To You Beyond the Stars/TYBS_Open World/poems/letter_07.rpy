init 10 python:
    letter_seven = MyPoem(
        poem_id="letter_to_player_07",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="露珠与流星",   # 诗的标题
        text="""
在蓝黑色的天幕下,
我看着一枚露珠.
它是如此晶莹,
如此完美.
然后,
它像一颗流星,
从叶片落下.
滴落到地面上,
溅起一片尘土.
我缓缓抬头,
泛白的天空中,
一枚流星像露珠一样落下,
溅起一片云彩.
        """,
        author="monika",
        ex_props={"sad": False}
    )
