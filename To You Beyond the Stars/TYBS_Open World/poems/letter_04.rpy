init 10 python:
    letter_four = MyPoem(
        poem_id="letter_to_player_04",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="冬日阳光",   # 诗的标题
        text="""
我拥抱着这一束,
属于冬日的暖阳.
抱着昨日的大雪,
明日的向往.
在光明的景色中,
阳光还是早早谢幕.
可悲啊,
冬天到来,
我到哪里去采花?
哪里去寻日光,
和地上的荫处？
四面环雪,
唯有残存的阳光,
在风中缓缓照耀.
        """,
        author="monika",
        ex_props={"sad": False}
    )
