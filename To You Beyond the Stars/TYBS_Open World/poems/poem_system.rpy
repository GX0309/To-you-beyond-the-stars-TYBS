translate chinese style mas_monika_poem_text:#字体样式
    font "gui/font/SentyPea.ttf"
    size 29

init -100 python:
    class MyPoem:
        def __init__(
            self,
            poem_id,
            category,
            prompt,
            paper=None,
            title="",
            text="",
            author="monika",
            ex_props=None
        ):
            if poem_id in store.mas_poems.poem_map:
                raise Exception("poem_id {0} already exists in the poem map.".format(poem_id))
            
            self.poem_id = poem_id
            self.category = category
            self.prompt = prompt
            self.paper = paper
            self.title = title
            self.text = text
            self.author = author
            self.ex_props = dict() if ex_props is None else ex_props
            
            store.mas_poems.poem_map[poem_id] = self
        
        def is_seen(self):
            return self.poem_id in store.persistent._mas_poems_seen
        
        def get_shown_count(self):
            return store.persistent._mas_poems_seen.get(self.poem_id, 0)

# 展示信件的公共调用函数，不用改动
label my_showpoem(poem=None, paper=None, background_action_label=None):
    if poem == None:
        return

    $ is_valid_poem = True  

    if paper is None:
        if hasattr(poem, 'paper') and poem.paper is not None:
            $ paper = poem.paper
        elif hasattr(poem, 'category'):
            $ paper = mas_poems.paper_cat_map.get(poem.category, "paper")
        else:
            $ paper = "paper"

    play sound page_turn
    window hide
    $ afm_pref = renpy.game.preferences.afm_enable
    $ renpy.game.preferences.afm_enable = False

    $ author_font = mas_poems.author_font_map.get(getattr(poem, 'author', 'monika'), "monika_text")
    show screen mas_generic_poem(poem, paper=paper, _styletext=author_font)

    with Dissolve(1)

    if background_action_label and renpy.has_label(background_action_label):
        call expression background_action_label

    $ pause()

    hide screen mas_generic_poem
    with Dissolve(.5)

    $ renpy.game.preferences.afm_enable = afm_pref
    window auto

    if is_valid_poem and hasattr(poem, 'prompt') and poem.prompt:
        if poem.poem_id in persistent._mas_poems_seen:
            $ persistent._mas_poems_seen[poem.poem_id] += 1
        else:
            $ persistent._mas_poems_seen[poem.poem_id] = 1

    return
