import pygame
import os
from ...utils.Button import Button
from ...utils.Font import getFont, Label
from ...utils.Storage import getData, initFile, upsertData

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.id = "gameover"

        initFile("save", ["name", "stage", "player_x", "player_y", "player_health", "player_boosts", "score", "best_score"])
        existing = getData("save", ["name", "player_data"])
        old_best = int(existing["best_score"]) if existing and existing.get("best_score") else 0
        self.best_score = max(old_best, self.game.score)

        save_data = {
            "name": "player_data",
            "stage": "1",
            "player_x": "100",
            "player_y": "300",
            "player_health": "20",
            "player_boosts": "",
            "score": str(self.game.score),
            "best_score": str(self.best_score),
        }
        upsertData("save", ["name", "player_data"], save_data)

        self.backdrop = pygame.transform.scale(
            pygame.image.load(os.path.join('./assets/backgrounds/', 'bg_interface__main.png')),
            (1280, 720)
        ).convert()

        if self.game.deathScreen is not None:
            self.backdrop = self.game.deathScreen.copy()

        self.overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.overlay_alpha = 0
        self.overlay_target = 185
        self.overlay_speed = 3

        self.red_overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.red_overlay.fill((120, 0, 0, 0))

        self.panel_w = 720
        self.panel_h = 400
        self.panel_x = (1280 - self.panel_w) // 2
        self.panel_y = (720 - self.panel_h) // 2 - 22

        self.panel_bg = pygame.Surface((self.panel_w, self.panel_h), pygame.SRCALPHA)
        self.panel_bg.fill((15, 5, 5, 200))

        self.panel_border = pygame.Surface((self.panel_w, self.panel_h), pygame.SRCALPHA)
        pygame.draw.rect(self.panel_border, (180, 30, 30, 220), (0, 0, self.panel_w, self.panel_h), 3)

        self.sep_y = self.panel_y + 90

        raw_reason = self.game.deathReason if self.game.deathReason else "cause inconnue"
        reason_display = raw_reason[0].upper() + raw_reason[1:] if raw_reason else "Cause inconnue"
        self.reason_text = f"Tué par : {reason_display}"

        btn_y = self.panel_y + self.panel_h - 80
        self.btn_retry = Button(game, self.panel_x + 60,                    btn_y, 280, 92, "RÉESSAYER")
        self.btn_menu  = Button(game, self.panel_x + self.panel_w - 300,    btn_y, 280, 92, "MENU")

        self.animDone = False
        self.tickCount = 0

    def tick(self, game):
        self.game = game
        self.tickCount += 1

        self.screen.blit(self.backdrop, (0, 0))

        if self.overlay_alpha < self.overlay_target:
            self.overlay_alpha = min(self.overlay_alpha + self.overlay_speed, self.overlay_target)
        self.red_overlay.fill((120, 0, 0, self.overlay_alpha))
        self.screen.blit(self.red_overlay, (0, 0))

        if self.tickCount > 20:
            self.screen.blit(self.panel_bg, (self.panel_x, self.panel_y))
            self.screen.blit(self.panel_border, (self.panel_x, self.panel_y))
            self.drawContent()
            self.btn_retry.draw(self.screen)
            self.btn_menu.draw(self.screen)

        if self.tickCount > 40:
            if self.btn_retry.isClicked():
                self.game.score = 0
                self.game.deathReason = ""
                self.game.deathScreen = None
                self.game.changeStage("1")
                return
            if self.btn_menu.isClicked():
                self.game.score = 0
                self.game.deathReason = ""
                self.game.deathScreen = None
                self.game.changeStage("main")
                return

        pygame.display.flip()

    def drawContent(self):
        cx = self.panel_x
        cy = self.panel_y

        title = Label(
            "VOUS ETES MORT",
            (640, cy + 44),
            getFont(self.game, "alagard"),
            (220, 40, 40),
            52,
            ["center"]
        )
        title.draw(self.screen)

        pygame.draw.line(self.screen, (180, 30, 30),
                         (cx + 40, self.sep_y), (cx + self.panel_w - 40, self.sep_y), 2)

        reason_label = Label(
            self.reason_text,
            (640, self.sep_y + 30),
            getFont(self.game, "yoster"),
            (210, 160, 160),
            24,
            ["center"]
        )
        reason_label.draw(self.screen)

        score_label = Label(
            f"Score  :  {self.game.score}",
            (640, self.sep_y + 80),
            getFont(self.game, "alagard"),
            (230, 200, 100),
            30,
            ["center"]
        )
        score_label.draw(self.screen)

        best_label = Label(
            f"Meilleur score  :  {self.best_score}",
            (640, self.sep_y + 122),
            getFont(self.game, "yoster"),
            (170, 150, 100),
            24,
            ["center"]
        )
        best_label.draw(self.screen)
