#!/bin/bash

function advanceMenu(){
    ADVSEL=$(whiptail --title "Menu" --fb --menu "Choisir l'options" 15 60 14 \
    "1" "options"\
    "2" "options"\
    "3" "options" 3>&1 1>&2 2>&3)

    case $ADVSEL in

    1) 
        echo "Options 1"
        whiptail --title "options 1" --msgbox "you choose options 1 " 8 45

    ;; 

    
    2) 
        echo "Options 2"
        whiptail --title "options 2" --msgbox "you choose options 2 " 8 45

    ;; 
    
    esac
}

advanceMenu