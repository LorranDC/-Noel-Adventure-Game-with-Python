#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: PyGame
# Prof. Douglas Machado Tavares
# Ministrado em 2023


import pygame
import time


class Barra:
    """ Define uma Barra de Stauts """

    def __init__(self, tela):
        """ __init__() -> instancia de cenario """
        self.tela = tela
        self.__fonte_A = pygame.font.Font("dados/fontes/VeraMoBd.ttf", 22)
        self.__fonte_B = pygame.font.Font("dados/fontes/VeraMoBd.ttf", 16)
        self.__fundo = pygame.image.load("dados/imagens/barra/fundo_01.png")
        # experimente: fundo_01, fundo_02, ... fundo_06
        self.__ligada = False
        self.__msg_render = None


    def ligar(self):
        """ Liga a atualizacao da barra """
        self.__ligada = True
        self.tempo_inicial = time.time()


    def desligar(self):
        """ Desliga a atualizaçao da barra """
        self.__ligada = False


    def update(self, x, num_colisoes):
        """ Repinta a Barra """
        cor = (255, 255, 0)
        modelo = "Posição: {:3d}m   Colisões: {:02d}   Tempo: {:02d}:{:05.2f}"
        if self.__ligada:
            tac = time.time()
            self.tempo = tac - self.tempo_inicial
            minutos = int(self.tempo // 60)
            seg = self.tempo % 60
            posicao = int(x / 100)
            msg_str = modelo.format(posicao, num_colisoes, minutos, seg)
            self.__msg_render = self.__fonte_A.render(msg_str, True, cor)
            self.tela.blit(self.__fundo, (150, 10))
            self.tela.blit(self.__msg_render, (195, 28))
        elif self.__msg_render is not None:
            self.tela.blit(self.__fundo, (150, 10))
            self.tela.blit(self.__msg_render, (195, 28))
        cor = (200, 200, 255)
        msg_str = "Copyleft © 2020 - Douglas Machado Tavares".center(50)
        msg_render = self.__fonte_B.render(msg_str, True, cor)
        self.tela.blit(msg_render, (500, 555))
        msg_str = "CEFET-MG".center(50)
        msg_render = self.__fonte_B.render(msg_str, True, cor)
        self.tela.blit(msg_render, (500, 575))
