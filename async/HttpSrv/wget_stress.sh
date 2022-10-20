#!/bin/bash
# VladVons@gmail.com


x_terminal()
{
    Cmd="./wget.sh"

    for i in {1..50}; do
        echo "terminal : $i"

        #xfce4-terminal --minimize --hold --geometry=20x20 --initial-title="$Cmd $i" --command="$Cmd"
        xterm -e bash -c $Cmd &

        sleep 0.1
    done

    rm wget-log.*
}

x_terminal
