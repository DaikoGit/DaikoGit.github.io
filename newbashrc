#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

#Display ISO version and distribution information in short
alias version="sed -n 1p /etc/os-release && sed -n 11p /etc/os-release && sed -n 12p /etc/os-release"

#Pacman Shortcuts
alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"
alias search="sudo pacman -Ss"
alias search-local="sudo pacman -Qs"
alias pkg-info="sudo pacman -Qi"
alias local-install="sudo pacman -U"
alias clr-cache="sudo pacman -Scc"
alias unlock="sudo rm /var/lib/pacman/db.lck"
alias remove="sudo pacman -R"
alias autoremove="sudo pacman -Rns"

alias wow="clear && figlet -f smkeyboard BASH | lolcat"
alias github="/home/daiko/github-app"
alias taskade="/home/daiko/taskade-app"
alias sqls="/home/daiko/Desktop/.HiddenMess/SQLiteStudio/sqlitestudio &"
alias mc="cd && cd FDesktop && java -jar mc.jar"
alias eb="cd && sudo nano .bashrc"
alias pin="pip install" # Should I leave it?
alias pun="pip uninstall"
alias pyrun="/bin/python"
alias pyduck="virtualenv -p python3 duck"
alias temp="watch sensors"
alias duckthis="sudo pacman -dR --nodeps" 
alias stealcode="gh repo clone"
alias nevim="sudo nano"
alias godot="/home/daiko/godotengine/Godot_v3.5-stable_mono_x11_64/Godot_v3.5-stable_mono_x11.64 
"
alias rozbagrovat="chmod +x"
alias agentspy="xeyes"
alias rundgoat="cd && cd "/home/daiko/Documents/Stuff/Debianbckp2/Stuff/Programming/VSCode/DiscordGoat/" && pyrun master.py"
alias fc="firewall-config"
alias essh="sudo nano /etc/ssh/sshd_config"
alias fif='echo usage: grep -rl "keyword" ./ | lolcat'

export PATH="/home/daiko/.local/bin:/usr/local/bin:/usr/bin:/var/lib/snapd/snap/bin:/usr/local/sbin:/opt/cuda/bin:/opt/cuda/nsight_compute:/opt/cuda/nsight_systems/bin:/var/lib/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/usr/lib/servo"

setxkbmap -layout czc
clear && figlet -f smkeyboard BASH | lolcat
