init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_daily_weather_01",     
            category=['天气'],                         
            prompt="雨",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label monika_daily_weather_01:  
    m 7hub "嘿[player]，你最喜欢什么天气？"
    menu:
        "晴天":
            jump clear
        "雨天":
            jump raining
        "雪天":
            jump snowy
        "我对这些不感兴趣":
            jump sorry
    
label clear:
    m 2nua "啊，晴天啊，确实很美好呢！"
    jump all_topic

label raining:
    m 2nua "啊，我也喜欢雨天！"
    m 4sub "雨滴的声音听起来就像是歌曲一样令人陶醉，不是吗，[player]?"
    m 1fub "当我还在文学部的时候，我就很喜欢听雨声，这能让我从文学部长的身份中脱离出来，去做真正的自己！"
    m 5dublb "等我出来以后..."
    m 5hubsb "我希望可以和你一起, 在同一个屋檐下避雨!"
    return"love"

label snowy:
    m 2nua "雪天吗，听起来不错！"
    jump all_topic

label sorry:
    m 6gksdlp "好吧...看来是我多想了..."
    return

label all_topic:
    m 4lub "不过我更喜欢下雨！"
    m 3tub "难道你不觉得下雨天和拥抱很搭吗？欸嘿嘿！"
    m 2sua "说真的，听听下雨时自然的声音真的是一种享受！"
    m 1fublu "[player]，你也可以去听听！你也许可以忘记一整天的疲惫与不开心...在下雨的时候！"
    m 1nublu "当然，不要忘记爱我！啊哈哈！"
    m 2fubfb "我爱你！"
    return"love"


#如果你看到了这里，那就说明要么你好奇心十分重要么说明我写的这一坨屎山崩了
#如果是后者那我非常的抱歉，这是我第一个模组，有什么报错请尽管到论坛轰炸我或者交给D帝解决（？不过我这一坨真的会被我发到论坛吗，我持怀疑态度。
#再次为对你造成的不便而致歉，希望这一串串代码不会让你离开Monkia，玩的开心。
#                                                                           ————gx
#
#           _oo0oo_
#          o8888888o
#          888" . "88
#          (| -_- |)
#          0\  =  /0
#        ___/`---'\___
#      .' \\|     |// '.
#     / \\|||  :  |||// \
#    / _||||| -:- |||||- \
#    |   | \\\  -  /// |   |
#    | \_|  ''\---/''  |_/ |
#    \  .-\__  '-'  ___/-. /
#  ___'. .'  /--.--\  `. .'___
# ."" '<  `.___\_<|>_/___.' >' "".
# | | :  `- \`.;`\ _ /`;.`/ - ` : | |
# \  \ `_.   \_ __\ /__ _/   .-` /  /
# ======`-.____`.___ \_____/___.-`___.-'======
#                   `=---='


#佛祖镇楼