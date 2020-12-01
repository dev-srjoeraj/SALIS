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

def create_user(username):
    xec("useradd -m -p wheel {}".format(username))
    xec("passwd {}".format(username))
    xec("su {}".format(username))


def base_install():
    base_packages = list(("xorg",
                 "lightdm",
                 "lightdm-gtk-greeter",
                 "i3-gaps", 
                 "i3status",
                 "i3blocks",
                 "pulseaudio",
                 "pavucontrol",
                 "nitrogen",
                 "picom",
                 "polkit-gnome",
                 "rofi",
                 "terminator",
                 "alacritty",
                 "pcmanfm",
                 "ttf-jetbrains-mono",
                 "ttf-font-awesome",
                 "arc-gtk-theme",
                 "noto-fonts-emoji"
                 ))


    for pkg in base_packages:
        pacman_install(pkg)

def lightdm_config():
    xec("rm /etc/lightdm/lightdm-gtk-greeter.conf")
    xec("mv wall.png /usr/share/backgrounds")
    xec("mv lightdm-gtk-greeter.conf /etc/lightdm/")
    systemd_enable_service("lightdm.service")


def install_config(username):
    git_clone("dev-srjoeraj", "dotfiles-arch")

    xec("mkdir -p /home/{0}/.statusbar".format(username))
    xec("mkdir -p /home/{0}/.config".format(username))

    xec("cd dotfiles-arch/config && mv * /home/{0}/.config".format(username))
    xec("cd dotfiles-arch/statusbar && mv * /home/{0}/.statusbar".format(username))
    xec("cd /home/{0}/.statusbar && chmod 777 *".format(username))



def installer():
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--usr"):
            
            base_install()
            install_config(sys.argv[2]) 
            lightdm_config()
            restart()
            

        elif(sys.argv[1] == "--final"):
            p("We are in the final step of the installation ...")

    




installer()










