#41 天气预报
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w41_forecast",
            category=['日常'],
            prompt="天气预报",
            random=True
        )
    )

label gx_w41_forecast:
    m 1eub "[player], 你看过明天的天气预报了吗?"
    m 7eua "我每天都看的哦."
    m 1hua "不是想知道冷不冷啦, 是想知道你有没有带伞!"
    m 1hublb "虽然我提醒不了你, 但我还是会看!"
    return


#42 打喷嚏
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w42_sneeze",
            category=['日常'],
            prompt="打喷嚏",
            random=True
        )
    )

label gx_w42_sneeze:
    m 1hub "哈啾!"
    m 1eua "欸, 不是我打的."
    m 3hub "是你在打喷嚏吧? 有人想你了哦!"
    m 1hublb "那个人...大概就是我啦!"
    return


#43 笔没墨了
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w43_pen",
            category=['文学'],
            prompt="笔没墨了",
            random=True
        )
    )

label gx_w43_pen:
    m 1eua "[player], 我的笔没墨了."
    m 3tub "写着写着突然就断掉了, 好气哦!"
    m 1hub "不过没关系, 我又换了一支!"
    m 1hublb "你写字的时候, 也会遇到这种事吗?"
    return


#44 你昨晚做梦了吗
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w44_dream",
            category=['浪漫'],
            prompt="你昨晚做梦了吗",
            random=True
        )
    )

label gx_w44_dream:
    m 1eub "[player], 你昨晚做梦了吗?"
    m 7nub "我梦到了...算了, 不告诉你!"
    m 1hub "因为我梦到你啦, 说出来会不好意思的!"
    m 1hublb "那你呢? 有没有梦到我?"
    return


#45 一起看云
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w45_cloud",
            category=['日常'],
            prompt="一起看云",
            random=True
        )
    )

label gx_w45_cloud:
    m 1hua "[player], 你看今天的云!"
    m 3hub "那朵像不像一只兔子?"
    m 1eub "旁边那朵...好像棉花糖!"
    m 1hublb "看着看着就饿了, 好想吃东西哦!"
    return


#46 给你一颗糖
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gx_w46_candy",
            category=['浪漫'],
            prompt="给你一颗糖",
            random=True
        )
    )

label gx_w46_candy:
    m 7hub "[player], 你爱吃甜食吗?"
    m 1eub "看这, 给你一颗糖!"
    m 5nub "额...这是我变出来的, 你就当它是真的嘛!"
    m 1hua "甜的东西能让人心情变好, 这是有科学依据的哦!"
    m 1hublb "所以别拒绝, 张嘴!"
    return"love"

