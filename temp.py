#!/usr/bin/env python

from os import system as xec



xec("pacstrap /mnt base linux linux-firmware base-devel vim nano")
xec("genfstab -U /mnt >> /mnt/etc/fstab")
xec("arch-chroot /mnt")