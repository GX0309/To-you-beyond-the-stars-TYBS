default persistent.letter_count = 0
default persistent.ra_po = 0
default persistent.club_count = 0
default persistent.street_count = 0
default persistent.classroom_count = 0
default persistent.monika_topic_count = 0
default persistent.mc_house_count = 0
default persistent.sa_house_count = 0
default persistent.mc_room_count = 0
default persistent.find_new = 0
default persistent.park_count = 0
default persistent.lake_count = 0
default persistent.read_letters = []
default persistent.playground = False
default persistent.playstore = False
default persistent.road_count = 0
default persistent.pg_count = 0
default persistent.count = 0
default persistent.playstore_count = 0
default persistent.road_03_count = 0
default persistent.coffe_count = 0

init python:
    if not hasattr(store, "glitchtext"):
        def glitchtext(num):
            return "?" * num

default OW_mc = glitchtext(4)


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_test_01",     
            category=['测试话题(open world)'],                         
            prompt="重置变量",                             
            unlocked=True,                             
            pool=True                                  
        )
    )

label ow_test_01:
    "确定要重置开放世界的所有游览记录吗?{nw}"
    menu:
        "确定要重置开放世界的所有游览记录吗?{fast}"
        "是":
            jump return_default

        "否":
            return

label return_default:
    $ persistent.monika_topic_count = 0
    $ persistent.mc_room_count = 0
    $ persistent.sa_house_count = 0
    $ persistent.mc_house_count = 0
    $ persistent.classroom_count = 0
    $ persistent.letter_count = 0
    $ persistent.street_count = 0
    $ persistent.ra_po = 0
    $ persistent.club_count = 0
    $ persistent.find_new = 0
    $ persistent.park_count = 0
    $ persistent.lake_count = 0
    $ persistent.read_letters = []
    $ persistent.playground = False
    $ persistent.playstore = False
    $ persistent.road_count = 0
    $ persistent.pg_count = 0
    $ persistent.count = 0
    $ persistent.playstore_count = 0
    $ persistent.road_03_count = 0
    $ persistent.coffe_count = 0

    "变量已重置"
    return
init 5 python:
    if persistent.playground and persistent.playstore:
        persistent.road_count = 1
