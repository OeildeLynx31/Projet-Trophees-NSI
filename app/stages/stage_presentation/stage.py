import pygame
import os

from ...utils.Button import Button
from ...utils.Storage import *

from ...utils.Font import *

PAGES = [
    {
        "title": "Le Projet",
        "lines": [
            "Trophees NSI 2025-2026",
            "",
            "Ce jeu est un platformer 2D développé en Python",
            "avec la bibliothèque Pygame dans le cadre",
            "des Trophées NSI.",
            "",
            "Le joueur explore des niveaux, combat des ennemis",
            "et accumule des points en cassant des caisses.",
        ]
    },
    {
        "title": "Les Mecaniques",
        "lines": [
            "Déplacement : Z pour avancer, souris pour la direction",
            "Saut        : ESPACE ou flèche haut",
            "Attaque     : Clic gauche",
            "Inventaire  : E",
            "",
            "Les ennemis patrouillent et attaquent au corps à corps.",
            "Les caisses sont destructibles et donnent des points.",
            "Des trampolines permettent de sauter plus haut.",
        ]
    },
    {
        "title": "Les Ennemis",
        "lines": [
            "Zombush  — ennemi de base, saute, 20 PV",
            "MiniRock — rapide, courte portée, 20 PV",
            "Grolem   — lent mais puissant, 40 PV",
            "Spike    — piège au sol, immortel",
            "",
            "Chaque ennemi tue rapporte des points.",
            "Plus l'ennemi est fort, plus le gain est eleve.",
        ]
    },
    {
        "title": "L'Equipe",
        "lines": [
            "Développé par :",
            "",
            "  • HENRY-VIEL Vincent — architecture du jeu, mécaniques, systèmes, audio",
            "  • DALOUX Ewenn — système de stockage, utilitaires, base des entités",
            "  • CHOQUAR Jules — conception des niveaux, environnements, interfaces",
            "  • ROUX Valentin — graphismes, animations du joueur, design visuel",
            "",
            "Projet réalisé en classe de Première NSI",
            "Lycée Emilie de Rodat, Toulouse",
            "Année scolaire 2025-2026",
        ]
    },
]

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.id = "presentation"

        self.backdrop = pygame.transform.scale(
            pygame.image.load(os.path.join('./assets/backgrounds/', 'bg_interface__main.png')),
            (1280, 720)
        ).convert()

        self.container_w = 1080
        self.container_h = 520
        self.container_x = (1280 - self.container_w) // 2
        self.container_y = 160

        self.text_overlay = pygame.Surface((self.container_w - 120, self.container_h - 120), pygame.SRCALPHA)
        self.text_overlay.fill((0, 0, 0, 80))

        self.title = pygame.transform.scale_by(pygame.image.load(os.path.join('./assets/interface/', "title.png")), 2).convert_alpha()
        btn_y = self.container_y + self.container_h - 80
        self.btn_prev = Button(game, self.container_x + 40,        btn_y, 180, 100, "< PRÉC")
        self.btn_next = Button(game, self.container_x + self.container_w - 220, btn_y, 180, 100, "SUIV >")
        self.btn_back = Button(game, (1280 - 220) // 2,            btn_y + 28, 220, 100, "RETOUR")

        self.currentPage = 0
        self.navCooldown = 250
        self.lastNav = pygame.time.get_ticks()

        self.game.musicManager.play_music('powerful_adventure', game.settings, interrupt=True)

    def tick(self, game):
        self.game = game

        self.screen.blit(self.backdrop, (0, 0))

        self.screen.blit(self.text_overlay, (self.container_x + 60, self.container_y + 50))

        self.screen.blit(self.title, (640 - self.title.get_width() // 2, self.container_y - 140))

        self.drawPage()

        self.btn_prev.draw(self.screen)
        self.btn_next.draw(self.screen)
        self.btn_back.draw(self.screen)

        self.drawPageIndicator()

        now = pygame.time.get_ticks()
        if now - self.lastNav > self.navCooldown:
            if self.btn_prev.isClicked() and self.currentPage > 0:
                self.currentPage -= 1
                self.lastNav = now
            if self.btn_next.isClicked() and self.currentPage < len(PAGES) - 1:
                self.currentPage += 1
                self.lastNav = now
            if self.btn_back.isClicked():
                self.game.changeStage("main")
                self.lastNav = now

        pygame.display.flip()

    def drawPage(self):
        page = PAGES[self.currentPage]

        title_label = Label(
            page["title"],
            (640, self.container_y + 65),
            getFont(self.game, "alagard"),
            "#f5e6c8",
            38,
            ["center"]
        )
        title_label.draw(self.screen)

        sep_y = self.container_y + 80
        pygame.draw.line(self.screen, (180, 130, 80),
                         (self.container_x + 60, sep_y),
                         (self.container_x + self.container_w - 60, sep_y), 2)

        line_y = self.container_y + 100
        for line in page["lines"]:
            if line == "":
                line_y += 14
                continue
            label = Label(
                line,
                (self.container_x + 80, line_y),
                getFont(self.game, "yoster"),
                "#e8d5b0",
                22
            )
            label.draw(self.screen)
            line_y += 34

    def drawPageIndicator(self):
        total = len(PAGES)
        dot_y = self.container_y + self.container_h - 52
        spacing = 18
        start_x = 640 - (total * spacing) // 2

        for i in range(total):
            color = (245, 200, 100) if i == self.currentPage else (100, 80, 50)
            pygame.draw.circle(self.screen, color, (start_x + i * spacing, dot_y), 5)