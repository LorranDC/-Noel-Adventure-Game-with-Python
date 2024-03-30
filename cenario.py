#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: PyGame
# Prof. Douglas Machado Tavares
# Ministrado em 2023


import pygame
import os
from pygame.constants import *


class Cenario:
    """ Define um Cenario """

    def __init__(self, tela, nome_arq_mapa):
        """ __init__() -> instancia de cenario """
        self.tela = tela
        self.xc = 0
        self.yc = 0
        self.__carregar_objetos()
        self.__carregar_mapa(nome_arq_mapa)
        num_px_x = (len(self.mapa[0]) - 1) * 100
        num_px_y = len(self.mapa) * 100
        self.area = pygame.surface.Surface((num_px_x, num_px_y))
        self.obstaculos = []
        self.obstaculos_simbolos = []


    def __carregar_objetos(self):
        """ Carrega os objetos """
        caminho = "dados/imagens/objetos/"
        lista_nomes = os.listdir(caminho)
        self.objetos = {}
        for nome in lista_nomes:
            if nome.endswith(".png"):
                simbolo = nome[-5]
                colisao = nome[-7]
                objeto = pygame.image.load(caminho + nome)
                self.objetos[simbolo] = (objeto, colisao)


    def __carregar_mapa(self, nome_arq_mapa):
        """ Carrega o mapa """
        arq_mapa = open(nome_arq_mapa, "r")
        self.mapa = arq_mapa.readlines()
        arq_mapa.close()


    def construir(self):
        """ Constroi o cenario """
        y = 0
        for linha in self.mapa:
            x = 0
            for simbolo in linha:
                if simbolo in self.objetos:
                    objeto, colidivel = self.objetos[simbolo]
                    self.area.blit(objeto, (x, y))
                    if colidivel == 'c':
                        rtg = objeto.get_bounding_rect()
                        rtg.x += x
                        rtg.y += y
                        self.obstaculos.append(rtg)
                        self.obstaculos_simbolos.append(simbolo)
                x = x + 100
            y = y + 100
        self.__area_original = self.area.copy()


    def limpar(self):
        """ Volta a superfice 'area' ao estado original """
        self.area = self.__area_original.copy()


    def update(self):
        """ Repinta o cenario """
        largura = self.area.get_rect().width
        altura = self.area.get_rect().height
        origem = (self.xc, self.yc, largura, altura)

        largura = self.tela.get_rect().width
        altura = self.tela.get_rect().height
        destino = (0, 0, largura, altura)

        self.tela.blit(self.area, destino, origem)


    def mover(self, dx, dy):
        """ Move o cenario """
        largura = self.tela.get_rect().width
        altura = self.tela.get_rect().height
        if 0 <= self.xc <= self.area.get_width() - largura:
            self.xc += dx
        if 0 <= self.yc <= self.area.get_height() - altura:
            self.yc += dy
