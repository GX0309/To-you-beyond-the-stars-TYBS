init -1 python:

    if not hasattr(persistent, "read_letters") or persistent.read_letters is None:
        persistent.read_letters = []


label ow_poem:
    show monika 3t_gowm at t11
    with dissolve
    m "好啊!"
    show monika 5a_gowm at t11
    with dissolve
    m "让我酝酿一下..."
    show monika 5a_gowm at t11
    with dissolve
    pause 2.0
    show monika 10t_gowm at t11
    with dissolve
    m "有了!"
    hide monika
    call random_poem
    $ persistent.ra_po += 1
    show monika 6j_gowm at t11
    with dissolve
    m "怎么样怎么样?"
    show monika 6k_gowm at t11
    with dissolve
    m "我写的还不错吧?"
    show monika 9b_gowm at t11
    with dissolve
    m "希望你能喜欢!"
    jump ow_club_menu


label random_poem:


    $ letters = [
        letter_one,
        letter_two,
        letter_three,
        letter_four,
        letter_five,
        letter_six,
        letter_seven,
        letter_eight,
        letter_nine,
        letter_ten
    ]

    $ available = [
        l for l in letters
        if l.poem_id not in persistent.read_letters
    ]

    if not available:
        return

    $ selected = renpy.random.choice(available)

    $ persistent.read_letters.append(selected.poem_id)

    call my_showpoem(poem=selected)

    return




