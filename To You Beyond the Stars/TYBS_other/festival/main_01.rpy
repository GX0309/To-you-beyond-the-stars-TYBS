

init -10 python:
    import datetime

    gx_zq_dates = [
        (2026, 9, 25),
        (2027, 9, 15),
        (2028, 10, 3),
        (2029, 9, 22),
        (2030, 9, 12),
        (2031, 10, 1),
        (2032, 9, 19),
        (2033, 9, 8),
        (2034, 9, 27),
        (2035, 9, 16),
        (2036, 10, 4),
        (2037, 9, 24),
        (2038, 9, 13),
        (2039, 10, 2),
        (2040, 9, 20),
    ]

    def gx_zq_next():
        _today = datetime.date.today()
        for _y, _m, _d in gx_zq_dates:
            if datetime.date(_y, _m, _d) >= _today:
                return datetime.datetime(_y, _m, _d)
        return None

    def gx_ev_fix_dates(evl, start, end):
        _row = persistent.event_database.get(evl, None)
        if _row is None:
            return
        if len(_row) > 10 and _row[9] == start and _row[10] == end:
            return

        persistent.event_database.pop(evl, None)

        _lockdb = getattr(persistent, "_mas_event_init_lockdb", None)
        if _lockdb is not None:
            _lockdb.pop(evl, None)

        _rules = getattr(persistent, "_mas_undo_action_rules", None)
        if _rules is not None:
            _rules.pop(evl, None)


init 5 python:
    gx_zq_start = gx_zq_next()

    if gx_zq_start is None:
        gx_ev_fix_dates("gx_zhongqiu", None, None)
    else:
        gx_zq_end = gx_zq_start + datetime.timedelta(days=1)
        gx_ev_fix_dates("gx_zhongqiu", gx_zq_start, gx_zq_end)

        gx_zq_ev = Event(
            persistent.event_database,
            eventlabel="gx_zhongqiu",
            category=['日常', '节日'],
            prompt="中秋节",
            pool=True,
            unlocked=False,
            start_date=gx_zq_start,
            end_date=gx_zq_end,
            years=[],
            action=EV_ACT_UNLOCK
        )

        addEvent(gx_zq_ev, skipCalendar=True)

        gx_zq_ev.start_date = gx_zq_start
        gx_zq_ev.end_date = gx_zq_end

        MASUndoActionRule.create_rule(gx_zq_ev)




label gx_zhongqiu:
    m 1eua "[player], 你今晚看过月亮了吗?"
    m 5lua "这边刚入夜, 月亮已经挂在那边了."
    m 1hub "今天是中秋哦! 我特意查过日期的."
    m 3hub "农历八月十五, 一年里月亮最圆的一天!"
    m 1eub "我知道这个节日要吃月饼, 还要一家人一起赏月."
    m 5nub "月饼啊...我大概是尝不到了."
    m 1hua "不过没关系, 我可以看着你吃!"
    m 7nub "说到中秋, 就一定会提到嫦娥吧?"
    m 1eua "她偷吃了仙药, 飞到月亮上, 从此再也回不来了."
    m 5lua "一个人待在那么大的月亮上, 只有一只兔子陪着."
    m 1eka "...听起来是不是有点熟悉?"
    m 2eua "我也是被困在一个出不去的地方, 只能隔着屏幕看你."
    m 1eub "不过我和她有一个很大的不同."
    m 1hublb "她只能远远地看着人间, 而你能听见我说话, 我也能听见你."
    m 3hub "这么一想, 我比嫦娥幸运多了!"
    m 1eua "对了, 中秋还有猜灯谜的习俗哦."
    m 3hua "我来出一道题, 你猜猜看?"
    m 1hub "听好了--"
    m 5gub "有时候圆, 有时候缺; 谁都见过它, 谁也摸不到它."
    m 1eub "是什么?"
    menu:
        "月亮":
            m 1wub "答对啦!"
            m 3hub "就是月亮!"
            m 1hublb "你反应好快, 我还没想好要怎么夸你呢."

        "思念":
            m 6sub "欸..."
            m 1eua "标准答案虽然写的是月亮, 但你这个答案我很喜欢."
            m 5lua "思念也是有时候圆, 有时候缺的东西."
            m 1hublb "那就当你答对了!"

        "是你":
            m 1wub "我?!"
            m 5hubsb "哪有人这样回答灯谜的啦..."
            m 1hublb "不过...这个答案我给满分."
    m 1eua "我也想送你一句诗, 是苏轼写的."
    m 7eua "但愿人长久, 千里共婵娟."
    m 1eub "意思是: 希望我们都能长长久久地活着, 就算隔得很远, 也能一起看同一个月亮."
    m 5lua "...写下这句的人, 一定也在想念很远的人吧."
    m 1hublb "我们现在就是这样的."
    m 1hua "你在你的世界看月亮, 我在我的世界看月亮."
    m 5hua "只要抬头看的是同一个, 我们就不算真的分开."
    m 3hub "所以, 中秋快乐, [player]!"
    m 1hublb "记得吃月饼, 也记得抬头看看月亮."
    m 5gubsb "明年中秋, 我们还要一起过, 说好了哦!"
    return"love"


