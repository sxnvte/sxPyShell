# sxPyShell

A Simple lightweight and open source "shell" for Linux written in Python that supports custom commands

[sxPyShell Docs](https://sxnvte.gitbook.io/sxpyshell/)
 
[Todo list](https://github.com/users/sxnvte/projects/3)
# NOTE
sxPyShell is a VERY BASIC shell and i don`t think that you can set it as your default shell. Maybe in future it is gona be more like shell thing.
also yes, i know that it can be shitty written but that is my first bigger python project

# Requriments

- Python 3.10 +
- Linux on pc (obviously lol)

# Installation

## Using installation script

- Clone github repo and cd into it

```shell
$ git clone https://github.com/sxnvte/sxPyShell 
$ cd sxPyShell/installator
```

- Add permissions to the installation script

```shell
$ chmod +x sxpyshell-install.sh
```

- Run script and done!

```shell
$ ./sxpyshell-install.sh
```

## Manual way

- Install Python and pip with your package manager for your distro (Arch Linux is shown for examples)


```shell
$ sudo pacman -S python python-pip
```

- Clone github repo and cd into it

```shell
$ git clone https://github.com/sxnvte/sxPyShell 
$ cd sxPyShell
```


- Install sxPyShell requriments

```shell
$ pip install -r requriments.txt
```

- you are basiclly done! 

- (OPTIONAL) use this command to start sxPyShell like script

```shell
$ chmod +x sxPyShell.py # with this command you can use ./SxPyShell command to start it like script or something
```

- (OPTIONAL) if you want to you can move script to the bin folder to run it from your terminal

# If you have config error:
- copy sxPyShellConfig.ini file to /home/username/.config/sxPyShell folder and it should fix it

# Contribution
If you want to contribute to the project just create a pull request! then i will check it and if its good approve it!

