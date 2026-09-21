init python:

    if persistent.tybs_2048_best is None:
        persistent.tybs_2048_best = 0

    class Game2048(object):
        """一个 4x4 的 2048 棋盘."""

        SIZE = 4

        def __init__(self):
            self.reset()

        def reset(self):
            self.board = [[0] * self.SIZE for _ in range(self.SIZE)]
            self.score = 0
            self.won = False            
            self.keep_playing = False   
            self.game_over = False
            self.add_tile()
            self.add_tile()

        def add_tile(self):
            empty = []
            for r in range(self.SIZE):
                for c in range(self.SIZE):
                    if self.board[r][c] == 0:
                        empty.append((r, c))
            if not empty:
                return
            r, c = renpy.random.choice(empty)
            self.board[r][c] = 4 if renpy.random.random() < 0.1 else 2

        def _merge_line(self, values):
            merged = []
            gained = 0
            pending = 0
            for v in values:
                if v == 0:
                    continue
                if pending == 0:
                    pending = v
                elif pending == v:
                    nv = pending * 2
                    merged.append(nv)
                    gained += nv
                    if nv >= 2048:
                        self.won = True
                    pending = 0
                else:
                    merged.append(pending)
                    pending = v
            if pending:
                merged.append(pending)
            merged += [0] * (self.SIZE - len(merged))
            return merged, gained

        def _get_line(self, index, direction):
            if direction == "left":
                return list(self.board[index])
            if direction == "right":
                return list(reversed(self.board[index]))
            if direction == "up":
                return [self.board[r][index] for r in range(self.SIZE)]
            return [self.board[r][index] for r in range(self.SIZE - 1, -1, -1)]

        def _set_line(self, index, direction, line):
            if direction in ("right", "down"):
                line = list(reversed(line))
            if direction in ("left", "right"):
                self.board[index] = line
            else:
                for r in range(self.SIZE):
                    self.board[r][index] = line[r]

        def move(self, direction):
            """返回 True 表示棋盘发生了变化."""
            changed = False
            gained_total = 0
            for i in range(self.SIZE):
                line = self._get_line(i, direction)
                new_line, gained = self._merge_line(line)
                gained_total += gained
                if new_line != line:
                    changed = True
                self._set_line(i, direction, new_line)

            if changed:
                self.score += gained_total
                self.add_tile()
                self.game_over = not self.can_move()
            return changed

        def can_move(self):
            for r in range(self.SIZE):
                for c in range(self.SIZE):
                    v = self.board[r][c]
                    if v == 0:
                        return True
                    if c + 1 < self.SIZE and self.board[r][c + 1] == v:
                        return True
                    if r + 1 < self.SIZE and self.board[r + 1][c] == v:
                        return True
            return False

        def continue_after_win(self):
            self.keep_playing = True

    TYBS_2048_COLORS = {
        0:    "#cdc1b4",
        2:    "#eee4da",
        4:    "#ede0c8",
        8:    "#f2b179",
        16:   "#f59563",
        32:   "#f67c5f",
        64:   "#f65e3b",
        128:  "#edcf72",
        256:  "#edcc61",
        512:  "#edc850",
        1024: "#edc53f",
        2048: "#edc22e",
    }

    def tybs_2048_color(value):
        return TYBS_2048_COLORS.get(value, "#3c3a32")

    def tybs_2048_text_color(value):
        return "#776e65" if value in (0, 2, 4) else "#f9f6f2"

    def tybs_2048_font_size(value):
        if value >= 1024:
            return 28
        if value >= 128:
            return 34
        return 42

    def tybs_2048_move(direction):
        if g2048.game_over:
            return
        if g2048.move(direction):
            if g2048.score > persistent.tybs_2048_best:
                persistent.tybs_2048_best = g2048.score
        renpy.restart_interaction()

    def tybs_2048_restart():
        g2048.reset()
        renpy.restart_interaction()

    def tybs_2048_continue():
        g2048.continue_after_win()
        renpy.restart_interaction()


default g2048 = Game2048()




screen game_2048():

    tag game
    modal True
    zorder 200

    key "K_LEFT"     action Function(tybs_2048_move, "left")
    key "K_RIGHT"    action Function(tybs_2048_move, "right")
    key "K_UP"       action Function(tybs_2048_move, "up")
    key "K_DOWN"     action Function(tybs_2048_move, "down")
    key "K_r"        action Function(tybs_2048_restart)
    key "K_x"        action Return("quit")

    add Solid("#faf8ef")

    vbox:
        align (0.5, 0.5)
        spacing 14

        text "2048" size 54 color "#776e65" xalign 0.5
        text "得分 [g2048.score]     最高 [persistent.tybs_2048_best]" size 22 color "#776e65" xalign 0.5

        frame:
            background Solid("#bbada0")
            padding (12, 12)
            xalign 0.5

            vbox:
                spacing 10

                for row in range(4):
                    hbox:
                        spacing 10

                        for col in range(4):
                            $ tile_value = g2048.board[row][col]
                            $ tile_text = ("%d" % tile_value) if tile_value else ""
                            $ tile_bg = tybs_2048_color(tile_value)
                            $ tile_fg = tybs_2048_text_color(tile_value)
                            $ tile_size = tybs_2048_font_size(tile_value)

                            frame:
                                xsize 96
                                ysize 96
                                padding (0, 0)
                                background Solid(tile_bg)

                                text tile_text:
                                    align (0.5, 0.5)
                                    size tile_size
                                    color tile_fg

        if g2048.game_over or (g2048.won and not g2048.keep_playing):
            frame:
                background Solid("#eee4daf0")
                padding (28, 18)
                xalign 0.5

                vbox:
                    spacing 12

                    if g2048.won and not g2048.keep_playing:
                        text "恭喜!你合出了 2048!" size 28 color "#776e65" xalign 0.5
                    else:
                        text "无路可走了... 最终得分 [g2048.score]" size 28 color "#776e65" xalign 0.5

                    hbox:
                        spacing 16
                        xalign 0.5

                        if g2048.won and not g2048.keep_playing:
                            textbutton "继续挑战" action Function(tybs_2048_continue)
                        textbutton "再来一局" action Function(tybs_2048_restart)
                        textbutton "退出游戏 (X)" action Return("quit")

        hbox:
            xalign 0.5
            spacing 14
            textbutton "←" action Function(tybs_2048_move, "left")  text_size 26
            textbutton "↑" action Function(tybs_2048_move, "up")    text_size 26
            textbutton "↓" action Function(tybs_2048_move, "down")  text_size 26
            textbutton "→" action Function(tybs_2048_move, "right") text_size 26

        hbox:
            xalign 0.5
            spacing 20
            textbutton "重新开始 (R)" action Function(tybs_2048_restart)
            textbutton "退出 (X)" action Return("quit")

        text "方向键移动 · R 重开 · X 退出" size 18 color "#a09a90" xalign 0.5




init 5 python:
    try:
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="tybs_game_2048",
                category=['游戏'],
                prompt="2048 小游戏",
                unlocked=True,
                pool=True
            )
        )
    except Exception:
        pass


label tybs_game_2048:

    m 1eua "要不要陪我玩一局 2048 呀[player]?"
    m 1hub "用方向键推动方块, 数字相同就会合并, 目标是合出 2048!"
    m 1eub "用鼠标的话, 点屏幕上的方向按钮也可以, 按 R 随时重新开始."
    m 1hua "放松一点, 输赢都不重要, 我就在旁边看着你."

    $ g2048.reset()
    call screen game_2048

    if g2048.score >= persistent.tybs_2048_best and g2048.score > 0:
        m 1wub "哇, [g2048.score] 分, 这是你的新纪录!"
    else:
        m 1eua "这一局拿到了 [g2048.score] 分, 最高纪录还停在 [persistent.tybs_2048_best] 分."

    m 1hua "辛苦啦, 下次想玩随时来找我."
    return
