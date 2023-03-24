#!/bin/sh

# isnt done yet

if which apt-get &> /dev/null; then
    PACKAGE_MANAGER="apt-get"
elif which yum &> /dev/null; then
    PACKAGE_MANAGER="yum"
elif which dnf &> /dev/null; then
    PACKAGE_MANAGER="dnf"
elif which pacman &> /dev/null; then
    PACKAGE_MANAGER="pacman"
else
    echo "cannot find a package manager for your system! what tf are you using bro"
    exit 1
fi


if ! which python &> /dev/null; then
    echo "Python isn't installed! installing..."
    if [[ "${PACKAGE_MANAGER}" == "pacman" ]]; then
        sudo ${PACKAGE_MANAGER} -S python
    else
        sudo ${PACKAGE_MANAGER} install python
    fi
fi


if ! ${PACKAGE_MANAGER} -qq list python-pip 2>/dev/null | grep -q "^python-pip/"; then
    echo "Python pip isn't installed! installing.."
    if [[ "${PACKAGE_MANAGER}" == "pacman" ]]; then
        sudo ${PACKAGE_MANAGER} -S python-pip
    else
        sudo ${PACKAGE_MANAGER} install python-pip
    fi
fi

