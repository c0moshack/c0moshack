#############################################################
#
#
#
#
#
#############################################################

# Perform basic updates
apt-get update
apt-get -y upgrade
apt-get -y dist-upgrade

# Install drop down shell, sensors, conky
apt-get install yakuake lm-sensors qtcurve conky-all

sensors-detect

#Install oh-my-zsh
curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh

# Kali install plasma desktop
apt-get install kali-defaults kali-root-login desktop-base kde-plasma-desktop

#
ln -s c0moshack/dotfiles/conkyrc .conkyrc
ln -s c0moshack/dotfiles/conky_wireless .conky_wireless

ln -s ~/c0moshack/dotfiles/themes/placidTheme2a ~/.themes/placidTheme25a
ln -s ~/c0moshack/dotfiles/yakuakerc ~/.kde/share/config/yakuakerc
ln -s ~/c0moshack/dotfiles/themes/placidTheme23c.yakuake placidTheme23c.yakuake
ln -s ~/c0moshack/dotfiles/themes/placidTheme25b ~/.kde/share/apps/QtCurve/placidTheme25b
ln -s ~/c0moshack/dotfiles/themes/placidTheme25a.qtcurve ~/.kde/share/apps/QtCurve/placidTheme25a.qtcurve
ln -s c0moshack/dotfiles/gtkrc-2.0 .gtkrc-2.0
ln -s /home/c0moshack/c0moshack/dotfiles/nautilus-scripts .gnome2/nautilus-scripts
ln -s /home/c0moshack/c0moshack/dotfiles/nemo-scripts .gnome2/nemo-scripts

