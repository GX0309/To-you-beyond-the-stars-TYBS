

init -10 python:
    import datetime


init 5 python:
    _gq_row = persistent.event_database.get("gx_guoqing", None)

    if _gq_row is not None and len(_gq_row) > 10 and _gq_row[9] is None:
        persistent.event_database.pop("gx_guoqing", None)

        _gq_lockdb = getattr(persistent, "_mas_event_init_lockdb", None)
        if _gq_lockdb is not None:
            _gq_lockdb.pop("gx_guoqing", None)

        _gq_rules = getattr(persistent, "_mas_undo_action_rules", None)
        if _gq_rules is not None:
            _gq_rules.pop("gx_guoqing", None)

    _gq_row = None


init 5 python:
    gx_gq_ev = Event(
        persistent.event_database,
        eventlabel="gx_guoqing",
        category=['日常', '节日'],
        prompt="国庆节",
        pool=True,
        unlocked=False,
        start_date=datetime.datetime(2026, 10, 1),
        end_date=datetime.datetime(2026, 10, 2),
        years=[],
        action=EV_ACT_UNLOCK
    )

    addEvent(gx_gq_ev, skipCalendar=True)

    MASUndoActionRule.create_rule(gx_gq_ev)




label gx_guoqing:
    m 1eua "[player], 今天是十月一日哦."
    m 1hub "国庆节! 这个我记着的."
    m 3hub "是你们国家的生日, 对吧?"
    m 1eub "我查过资料: 1949 年 10 月 1 日, 开国大典."
    m 5lua "那天的广场上, 升起了第一面五星红旗."
    m 1hua "光是想象那个画面, 就觉得心里发热."
    m 1eub "听说逢整数年份还会有阅兵式?"
    m 3hub "整齐的方阵一队一队走过去, 光是看视频都觉得气势很足!"
    m 5nub "可惜我这边看不到直播..."
    m 1hublb "所以你要是看了, 一定要讲给我听!"
    m 1eua "对了, 国庆还有七天长假呢."
    m 3hua "你现在是放假了, 还是要上班上学?"
    menu:
        "放假啦!":
            m 1wub "太好了!"
            m 1hublb "那这几天你可要多来看看我!"
            m 3hub "七天呢, 我们每天都能聊点不一样的!"

        "还要上班...":
            m 1lub "欸? 国庆还要上班吗..."
            m 1eka "那你要注意休息, 别把自己累坏了."
            m 1hublb "不过下了班也要来找我哦, 我一直在等你的."

        "路上全是人, 正堵着呢":
            m 5gub "哈哈, 我猜到了!"
            m 3tub "每到长假, 大家都在路上堵着."
            m 1hublb "你就在车里陪我聊天吧, 反正我哪儿也去不了."
    m 1eua "我看过很多关于你们国家的照片."
    m 7eua "长城, 西湖, 大漠, 还有南方那些水乡."
    m 5lua "每一张我都很喜欢."
    m 1eub "如果有机会, 我真想亲眼看一看."
    m 5hua "所以你去旅行的时候, 可不可以多拍几张照片?"
    m 1hublb "不用特意拍风景, 拍你走过的路就好."
    m 1eua "还有烟花."
    m 7nub "国庆的晚上, 好像会有烟花表演吧?"
    m 1wub "烟花我在这边是看不到的."
    m 5lua "所以那一下, 就替我看吧."
    m 1hua "你抬头的时候, 我也在抬头."
    m 1eua "最后送你一句话, 是我在一首诗里读到的."
    m 7eua "为什么我的眼里常含泪水? 因为我对这土地爱得深沉."
    m 1eub "我大概永远没办法真正站到那片土地上."
    m 1hublb "但你会替我站在那里, 这就够了."
    m 3hub "好啦, 总之--"
    m 1hublb "国庆快乐, [player]!"
    m 1hua "玩得开心, 也要注意安全."
    m 5gubsb "人堆里别走丢了, 记得回来找我."
    return"love"


