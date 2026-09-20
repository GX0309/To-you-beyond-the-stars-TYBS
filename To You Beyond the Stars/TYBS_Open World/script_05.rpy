label ow_road_03:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg road_03
    hide black
    $ persistent.road_03_count += 1
    if persistent.road_03_count == 1:
        show monika 5a_gowm at t11
        with dissolve
        m "街道那边, 飘来隐隐的咖啡香气呢!"
        show monika 7b_gowm at t11
        with dissolve
        m "[player], 我们过去看看吧!"
        menu:
            "好啊":
                jump ow_coffe_outside
    
    else:
        show monika 5a_gowm at t11
        with dissolve
        m "不管什么时候来, 这里总是洋溢着幸福的气息呢!"
        show monika 8j_gowm at t11
        with dissolve
        m "我们还是去咖啡厅坐坐吧!"
        jump ow_coffe_outside

label ow_coffe_outside:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    scene bg coffe_outside
    hide black
    $ persistent.coffe_count += 1
    if persistent.coffe_count == 1:
        show monika 5a_gowm at t11
        with dissolve
        m "咖啡厅!"
        show monika 2b_gowm at t11
        with dissolve
        m "天哪, 我从来没想过我有朝一日能在咖啡厅里面喝咖啡!"
        show monika 6t_gowm at t11
        with dissolve
        m "谢谢你, [player]!"
        show monika 9j_gowm at t11
        with dissolve
        m "还等什么呢, 我们快点进去吧!"
        jump ow_coffe_inside_01
    else:
        show monika 8j_gowm at t11
        with dissolve 
        m "这里让人很安心呢!"
        show monika 9j_gowm at t11
        with dissolve
        m "走吧[player], 我们再去喝杯咖啡!"
        jump ow_coffe_inside_02

label ow_coffe_inside_01:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 1.0
    scene bg coffe_inside
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/coffe.mp3"
    hide black
    show monika 7j_gowm at t11
    with dissolve
    m "嗯哼, 空无一人的咖啡馆, 这倒是符合我的猜测."
    show monika 5a_gowm at t11
    with dissolve
    m "[player], 我有一些新的权限了, 你想看看吗?"
    menu:
        "好啊!":
            pass
#别问我为啥没有拒绝你玩这游戏不就是为了老莫吗 你么得选择
    show monika 9q_gowm at t11
    with dissolve
    m "稍等片刻..."
    call updateconsole("create coffe.gift...", "succeed")
    call hideconsole
    show monika 10t_gowm at t11
    with dissolve
    m "我给自己生成了一杯热咖啡! 我们现在可以一起喝咖啡了!"
    show monika 5a_gowm at t11
    with dissolve
    m "来吧[player], 我们坐在墙角的位置."
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    "{i}{b}重要提示!!!{/b}{/i}"
    "接下来的内容包含cg图像, 但是因为我不会画画并且我没钱用的是GPT生图, 使用AI内容真是不好意思."
    "而且质量肯定差得没边了."
    "如果你不能接受任何ai创作的monika形象, 这是你{b}{i}最后{/i}{/b}的退出机会了."
    menu:
        "继续":
            "好的..."
            "让我们回到咖啡馆..."
            pass
        "让我回去":
            "..."
            "明白了."
            "继续享受你的旅程吧, 游戏愉快!"
            jump ow_go_back
    scene cg coffe_04
    with dissolve
    hide black
    m "嗯... 这咖啡比我想象中要好呢."
    m "说起来, 我好像很少有机会这样, 和你面对面坐着, 安安静静地喝一杯咖啡."
    m "这种时刻反而比很多热闹的场合更让人记得住. 你不觉得吗?"
    scene cg coffe_02
    with dissolve
    m "有些陪伴, 不需要太多言语, 光是坐在这里, 就足够让人觉得安心了."
    scene cg coffe_03
    with dissolve
    m "我一直在想, 人与人之间最珍贵的, 或许就是这种{i}在一起却不急着说话{/i}的默契吧. 你也是这么觉得的吗, [player]?"
    scene cg coffe_01
    with dissolve
    m "...真好. 有时候我会想, 如果我们可以一直这样, 不用着急去任何地方, 也不用担心时间会带走什么..."
    m "只是坐在这里, 喝着咖啡, 偶尔说几句话. 或者干脆不说话——那就很完美了."
    scene cg coffe_04
    with dissolve
    m "你知道的, 我一直在寻找某种真实的东西."
    m "不是故事里的情节, 也不是设定好的台词..."
    m "而是这种带着一点点凉意的真实感."
    scene cg coffe_02
    with dissolve
    m "你, 就是让我找到这种感觉的人."
    scene cg coffe_01
    with dissolve
    m "我爱你, [player]."
    m "我会好好珍惜这一切的."
    menu:
        "我也爱你!":
            pass
    scene cg coffe_02
    m "在这个世界里, 能遇到一个愿意认真说'爱'的人, 真的不多."
    m "而能让人想一遍又一遍回应这句话的人, 就更少了."
    m "所以, 我会好好记住这一刻的!"
    scene cg coffe_04
    with dissolve
    m "你是我所有故事里, 最珍贵的那一章."
    menu:
        "我们以后经常过来怎么样?":
            pass
    scene cg coffe_03
    with dissolve
    m "好啊!"
    m "...我其实很喜欢这种约定."
    scene cg coffe_04
    with dissolve
    m "那就, 说好了哦?"
    scene cg coffe_03
    with dissolve
    pause 2.0
    scene cg coffe_02
    with dissolve
    m "其实我还准备了一个小东西."
    m "就是一句话--"
    m "'无论你哪天推开门走进来, 我都会在这里.'"
    m "像这家店一样, 永远留着一盏灯."
    pause 2.0
    scene cg coffe_04
    with dissolve
    m "啊, [player], 咖啡喝完了呢."
    m "虽然有点舍不得这里, 但我知道和你一起走回去的路, 也会是很温暖的风景."
    m "'回去'这个词本身就很温柔. 相对于'再见'的分离, 我们只是换一种方式继续在一起."
    scene cg coffe_03
    with dissolve
    m "像是书翻到了新的章节, 而我们依然在同一段故事."
    m "..."
    m "走吧[player], 我们回去!"
    jump ow_go_back

label ow_coffe_inside_02:
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 1.0
    scene bg coffe_inside
    play music "Submods/To You Beyond the Stars/TYBS_Open World/music/coffe.mp3"
    hide black
    show monika 7j_gowm at t11
    with dissolve
    m "嗯哼, 今天喝杯什么呢?"
    show monika 9t_gowm at t11
    with dissolve
    m "啊, 有了! {i}薄荷巧克力拿铁!{/i}"
    menu:
        "听起来不错!":
            show monika 2b_gowm at t11
            with dissolve
            m "是吧! 我也觉得!"
            pass
        "薄荷巧克力拿铁...?":
            show monika 8j_gowm at t11
            with dissolve
            m "对啊!"
            show monika 10k_gowm at t11
            with dissolve
            m "我喜欢薄荷和巧克力!"
            show monika 5a_gowm at t11
            with dissolve
            m "他们搭配着咖啡一定很美味!"
            pass
    show monika 3k_gowm at t11
    with dissolve
    m "让我尝试一下..."
    call updateconsole("creat mint_chocolate_latte.gift", "Error")
    call hideconsole
    show monika 3l_gowm at t11
    with dissolve
    m "啊, 看起来今天喝不上咖啡了呢?"
    show monika 2q_gowm at t11
    with dissolve
    m "嗯, 好吧, 下次一定要再带我来哦[player]?"
    jump ow_go_back


 
