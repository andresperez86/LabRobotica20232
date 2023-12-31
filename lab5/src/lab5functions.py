#!/usr/bin/env python3
# encoding: utf-8

import numpy as np
from copy import copy

cos=np.cos; sin=np.sin; pi=np.pi


def dh(d, theta, a, alpha):
    """
    Calcular la matriz de transformacion homogenea asociada con los parametros
    de Denavit-Hartenberg.
    Los valores d, theta, a, alpha son escalares.

    """
    T = 0
    return T
    
    

def fkine_ur5(q):
    """
    Calcular la cinematica directa del robot UR5 dados sus valores articulares. 
    q es un vector numpy de la forma [q1, q2, q3, q4, q5, q6]

    """
    # Longitudes (en metros)

    # Matrices DH (completar)
    T1 = 0
    T2 = 0
    T3 = 0
    T4 = 0
    T5 = 0
    T6 = 0
    # Efector final con respecto a la base
    T = 0
    return T


def jacobian_ur5(q, delta=0.0001):
    """
    Jacobiano analitico para la posicion. Retorna una matriz de 3x6 y toma como
    entrada el vector de configuracion articular q=[q1, q2, q3, q4, q5, q6]

    """
    # Alocacion de memoria
    J = np.zeros((3,6))
    # Transformacion homogenea inicial (usando q)

    
    # Iteracion para la derivada de cada columna
    for i in xrange(6):
        # Copiar la configuracion articular inicial
        dq = copy(q);
        # Incrementar la articulacion i-esima usando un delta

        # Transformacion homogenea luego del incremento (q+dq)

        # Aproximacion del Jacobiano de posicion usando diferencias finitas

    return J


def ikine_ur5(xdes, q0):
    """
    Calcular la cinematica inversa de UR5 numericamente a partir de la configuración articular inicial de q0. 

    """
    epsilon  = 0.001
    max_iter = 1000
    delta    = 0.00001

    q  = copy(q0)
    for i in range(max_iter):
        # Main loop
        pass
    
    return q


