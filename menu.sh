#!/bin/bash
#!/usr/bin/env python3

function advanceMenu(){
    ADVSEL=$(whiptail --title "Menu" --fb --menu "Choisir l'options" 15 60 14 \
    "1" "Informations générale"\
    "2" "Informations Réseaux"\
    "3" "Informations Processus" 3>&1 1>&2 2>&3)

    case $ADVSEL in

    1) 
        echo "Informations générale"
        whiptail --title "" --msgbox "Voici les informations générale" 8 45
        python3 generalinfo.py
    ;; 

    
    2) 
        echo "Informations Réseaux"
        whiptail --title "" --msgbox "Voici les informations Réseaux " 8 45
        python3 inforeseaux.py
    ;; 
    
    3) 
        echo "Informations Processus"
        whiptail --title "" --msgbox "Voici les informations Processus " 8 45
        python3 STOP.py
    ;; 
    
    esac
}

advanceMenu
