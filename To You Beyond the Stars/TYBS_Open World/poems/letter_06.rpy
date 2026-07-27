init 10 python:
    letter_six = MyPoem(
        poem_id="letter_to_player_06",  # 唯一ID，不能和别的重复
        category="romantic",
        prompt=" ",  #名称
        title="倒影",   # 诗的标题
        text="""
看着镜子,
我突然惊醒.
镜中没有我,
只有无尽的,
诗意的,
杂乱的世界.
'我的倒影呢?'
两个声音一并响起.
我转头看去,
另一个我站在另一面镜子之前,
镜中没有她.
        """,
        author="monika",
        ex_props={"sad": False}
    )
