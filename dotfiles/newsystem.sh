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

# Install drop down shell
apt-get install yakuake

# Kali install plasma desktop
apt-get install kali-defaults kali-root-login desktop-base kde-plasma-desktop

#
apt-get install qtcurve
#Download placidTheme25a.qtcurve  
wget http://kde-look.org/CONTENT/content-files/160458-placidTheme25a.qtcurve+gtk3.tar.gz
#get placid colors
wget http://kde-look.org/CONTENT/content-files/159869-placidTheme25a.colors
#get conky
wget http://kde-look.org/CONTENT/content-files/161096-placidTheme25a.conkyrc.tar.gz
#placid plasma
wget http://kde-look.org/CONTENT/content-files/163107-placidTheme25b.plasma.tar.gz
#placid yakuake
wget http://kde-look.org/CONTENT/content-files/161222-placidTheme23c.yakuake.tar.gz
