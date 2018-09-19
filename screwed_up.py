#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import os

ROOT_DIR = os.path.dirname(__file__)
VIDEO_FILE_1 = os.path.join(ROOT_DIR, 'videos', 'exorcista.mp4')
VIDEO_FILE_2 = os.path.join(ROOT_DIR, 'videos', 'se_fudeu.mp4')
VIDEO_OUT = os.path.join(ROOT_DIR, 'videos', 'out.avi')  #TODO: Usar tempfile ou gerar nome randomico


def get_mousepos():
    curr = subprocess.check_output(["xdotool", "getmouselocation"]).decode("utf-8")
    return [int(it.split(":")[1]) for it in curr.split()[:2]]


def run():
    current1 = get_mousepos()  # QUER QUE DESENHE?!
    while True:
        time.sleep(0.5)
        current2 = get_mousepos()
        if not current1 == current2:
            # GRAVAR A CARA DO MELIANTE
            os.system('streamer -q -c /dev/video0 -f rgb24 -r 3 -t 00:01:00 -o %s &' % VIDEO_OUT)
            # BLOQUEAR O TECLADO E MOUSE
            os.system('xtrlock &')
            os.system('amixer sset \'Master\' 100%')  # SOM NO MÁXIMO
            # EXIBIR UM VIDEO DA GAROTA DO EXORCISTA "GRITANDO".
            # COM TECLADO BLOQUEADO E VOLUME NO MÁXIMO, ESPERO QUE A PESSOA ENTRE
            # EM DESESPERO
            os.system('vlc --play-and-exit --fullscreen %s' % VIDEO_FILE_1)
            os.system('vlc --play-and-exit --fullscreen %s' % VIDEO_FILE_2)  # VIDEO 'SE FUDEU', KKK
            os.system('amixer sset \'Master\' 50%')  # BAIXAR O VOLUME
            os.system('xdotool key XF86AudioPlay')  # PLAY NO SPOTIFY (PROVAVELMENTE VAI ESTAR TOCANDO ROCK)
            os.system('pkill xtrlock')  # DESBLOQUEAR O TECLADO PARA EU PODER ACESSAR O SISTEMA QNDO VOLTAR
            os.system('xdotool key Super_L+l')  # BLOQUEAR A TELA NO LINUX DEEPIN (Ctrl+Alt+l: Outras distros)
            break  # THIS IS THE END
        current1 = current2


if __name__ == '__main__':
    run()
