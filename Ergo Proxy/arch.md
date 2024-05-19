
## Installation Instructions

There are three ways to install ArchWSL.

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#method-1-zip-file)Method 1: zip file

1. [Download](https://github.com/yuk7/ArchWSL/releases/latest) the installer zip.
2. Extract all files in zip file to the same directory. Please extract to a folder that you have write permission. For example, `C:\Program Files` cannot be used since the rootfs cannot be modified there.
3. Run `Arch.exe` to extract the rootfs and register to WSL

As a side note, the executable name is what is used as the WSL instance name. If you rename it, you can have multiple installs.

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#method-2-appx-package)Method 2: appx package

1. [Download the `.appx` and `.cer`](https://github.com/yuk7/ArchWSL/releases/latest)
2. Install `.cer` to the “Trusted Root Certificate Store” of the local machine. For details, please refer to the [Install Certificate page](https://wsldl-pg.github.io/ArchW-docs/Install-Certificate/). You will need administrator privileges to install the certificate.
3. Install the `.appx`

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#method-3-online-installer)Method 3: online installer

1. [Download `Arch_Online.zip`](https://github.com/yuk7/ArchWSL/releases/latest)
2. Extract all files in zip file to the same directory.
3. Run `Arch.exe` to download rootfs and register to WSL

This zip file is doesn’t include rootfs (~200 MB), hence its zip file is very small (~2 MB), but rootfs is donwloaded in the first run.

## [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#setup-after-install)Setup after install

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#if-you-are-a-wsl1-user-you-must-change-the-glibc-package-please-see-known-issues)[If you are a WSL1 user, you **must** change the glibc package. Please see Known issues.](https://wsldl-pg.github.io/ArchW-docs/Known-issues/#wsl1--wsl2)

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#setting-the-root-password)Setting the root password

```
>Arch.exe
[root@PC-NAME]# passwd
```

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#set-up-the-default-user)Set up the default user

Please see ArchWiki [Sudo](https://wiki.archlinux.org/index.php/Sudo#Example_entries) and [User and groups](https://wiki.archlinux.org/index.php/Users_and_groups) pages.

```
>Arch.exe
[root@PC-NAME]# echo "%wheel ALL=(ALL) ALL" > /etc/sudoers.d/wheel
(setup sudoers file.)

[root@PC-NAME]# useradd -m -G wheel -s /bin/bash {username}
(add user)

[root@PC-NAME]# passwd {username}
(set default user password)

[root@PC-NAME]# exit

>Arch.exe config --default-user {username}
    (setting to default user)
```

If the default user has not been changed ([issue #7](https://github.com/yuk7/ArchWSL/issues/7)), please reboot the computer or alternatively, restart the LxssManager in an Admin command prompt.

To restart the `LxssManager`, run this:

```
net stop lxssmanager && net start lxssmanager
```

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#initialize-keyring)Initialize keyring

Please excute these commands to initialize the keyring. (This step is necessary to use pacman.)

```
>Arch.exe
[user@PC-NAME]$ sudo pacman-key --init

[user@PC-NAME]$ sudo pacman-key --populate

[user@PC-NAME]$ sudo pacman -Sy archlinux-keyring

[user@PC-NAME]$ sudo pacman -Su
```

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#install-patched-glibc-need-in-wsl1)Install patched glibc (need in WSL1)

Arch’s glibc is built for Linux kernel 4.4 and above and does not work with WSL1.

WSL1 users **should** always follow the steps in [Known issues](https://wsldl-pg.github.io/ArchW-docs/Known-issues/#wsl1--wsl2).

### [](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#install-systemctl-alternative-optional)Install systemctl alternative (Optional)

WSL does not have support for systemd however, there are several solutions. Please see [Known issues](https://wsldl-pg.github.io/ArchW-docs/Known-issues/#systemdsystemctl).


### []NeoVim / LunarVim

```
sudo pacman -S neovim

sudo pacman -S git

sudo pacman -S yarn nmp 

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

sudo pacman -S rust 

sudo pacman -S base-devel

bash <(curl -s
https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh)

```

[WARN] the folder /home/anonymous/.local/bin is not on PATH, consider adding 'export PATH=/home/anonymous/.local/bin:$PATH' to your /home/anonymous/.zshenv

### [] YAY

```shell
pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```


### [] ZSH

```
yay -S zsh
yay -S --noconfirm zsh-theme-powerlevel10k-git
echo 'source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
```

### [] asdf-vm

```
yay -S asdf-vm
lvim .zshrc
source /opt/asdf-vm/asdf.sh
```