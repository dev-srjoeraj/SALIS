#!/usr/bin/env python

from os import system as xec
import sys

def pacman_install(package):
    xec('figlet "{} ... "| lolcat'.format(package))
    xec("sudo pacman -S {} --noconfirm --needed --noprogressbar ".format(package))


def yay_install(package):
    xec('figlet "{} ... "| lolcat'.format(package))
    xec("yay -S  --noconfirm {} ".format(package))

def systemd_enable_service(service_name):
    xec("sudo systemctl enable {}".format(service_name))


def git_clone(user,repo):
    xec("git clone https://www.github.com/{0}/{1}.git".format(user, repo))


def p(string):
    xec('echo "{}"'.format(string))

def restart():
    xec("sudo reboot now")

def base_install():
    base_packages = list(("xorg", # The entire xorg package.
                          "i3-gaps", # Tiling window manger. required to complet install
                          "i3status", # status bar for i3
                          "lightdm", # Cross platform Display Manager 
                          "lightdm-gtk-greeter", # Standard greeter for the i3 window manger.
                          "picom", # Compositor for transparency and other effects.
                          "feh", # Image viewer. Can be used to set the wallpaper.
                          "ttf-jetbrains-mono", # Default System Font.
                          "figlet", # Used to create fancy text.
                          "alacritty", # Terminal used by the setup in GUI.
                          "lolcat" # To give random colour to a colourful text.
                          ))

    for pkg in base_packages:
        pacman_install(pkg)

def setup_config(username):
    home_dir = "/home/" + username
    xec("mkdir -p {0}/.config/i3/ && mkdir -p {0}/.config/alacritty/ ".format(home_dir))
    xec("mv config {0}/.config/i3/ && mv alacritty.yml {0}/.config/alacritty/ ".format(home_dir))


def installer():
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--usr"):
            setup_config(sys.argv[2])
            base_install()
            systemd_enable_service("lightdm.service")
            

        elif(sys.argv[1] == "--final"):
            p("We are in the final step of the installation ...")

    




installer()










