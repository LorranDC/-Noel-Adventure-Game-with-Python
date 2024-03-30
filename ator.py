#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: PyGame
# Prof. Douglas Machado Tavares
# Ministrado em 2023


import pygame


class Ator(pygame.sprite.Sprite):
    """ Define um Ator """

    def __init__(self, pos_x=0, pos_y=0):
        """ __init__() -> instancia de ator """
        pygame.sprite.Sprite.__init__(self)
        self.poses = {}
        self.__p = 0 # um ponteiro para pose atual
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__congelado = False
        self.__estado_atual = ""
        self.mochila = {}


    def inserir_estado(self, estado):
        """ Insere um novo estado """
        self.poses[estado] = []
        self.alterar_estado(estado)


    def alterar_estado(self, novo_estado):
        """ Altera um novo estado """
        self.__estado_atual = novo_estado
        self.__p = 0


    def retornar_estado(self):
        """ Retorna o estado """
        return self.__estado_atual


    def esta(self, estado):
        """ Verifica se o ator esta realizando determinada ação """
        return self.__estado_atual == estado


    def inserir_pose(self, estado, nome_arq_img):
        """ Armazena uma 'surface' dentro da lista poses """
        self.image = pygame.image.load(nome_arq_img)
        self.rect = self.image.get_rect()
        self.rect.x = self.__pos_x
        self.rect.y = self.__pos_y
        self.poses[estado].append(self.image)


    def congelar(self):
        """ Congela a troca de poses """
        self.__congelado = True
        self.__p = 0
        self.image = self.poses[self.retornar_estado()][self.__p]


    def descongelar(self):
        """ Descongela a troca de poses """
        self.__congelado = False


    def update(self):
        """ Reimplementa o metodo update() """
        if not self.__congelado:
            self.__p = (self.__p + 1) % len(self.poses[self.retornar_estado()])
            self.image = self.poses[self.retornar_estado()][self.__p]
