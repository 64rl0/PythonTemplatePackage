#! /bin/bash

# Command used in the external tool is:
# --login -c "./execute_on_save.sh"

# Colors
red=$'\033[31m'
green=$'\033[32m'
yellow=$'\033[33m'
blu=$'\033[34m'
bold_red=$'\033[1m\033[31m'
bold_green=$'\033[1m\033[32m'
bold_yellow=$'\033[1m\033[33m'
bold_blu=$'\033[1m\033[34m'
bold=$'\033[1m'
end=$'\033[0m'

# Emoji
green_check_mark="\xE2\x9C\x85 "
hammer_and_wrench="\xF0\x9F\x9B\xA0"
clock="\xE2\x8F\xB0 "
sparkles="\xE2\x9C\xA8 "
stop_sign="\xF0\x9F\x9B\x91"
warning_sign="\xE2\x9A\xA0\xEF\xB8\x8F"


# Set venv with iSor and Black binaries here
path_to_venv_root='/Users/carlogtt/Library/CloudStorage/Dropbox/SDE/VirtualEnvs/dev_tools'
source ${path_to_venv_root}/bin/activate
echo

echo -e "${bold_green}${green_check_mark} Virtual environment activated:${end}"
echo "venv: $VIRTUAL_ENV"
echo "running: $(python --version)"
echo

echo -e "${bold_green}${hammer_and_wrench} Project Root:${end}"
pwd
echo

echo -e "${bold_green}${sparkles} Running iSort...${end}"
isort="N"
if  [[ $isort == "Y" ]]; then
    isort . 2>&1
else
    echo -e "${bold_red}[DISABLED]${end}"
fi
echo

echo -e "${bold_green}${sparkles} Running Black...${end}"
black="N"
if  [[ $black == "Y" ]]; then
    black . 2>&1
else
    echo -e "${bold_red}[DISABLED]${end}"
fi
echo

echo -e "${bold_green}${sparkles} Running Flake8...${end}"
flake8="N"
if  [[ $flake8 == "Y" ]]; then
    flake8 -v . 2>&1
else
    echo -e "${bold_red}[DISABLED]${end}"
fi
echo

echo -e "${bold_green}${sparkles} Running mypy...${end}"
mypy="N"
if  [[ $mypy == "Y" ]]; then
    mypy ./src 2>&1
else
    echo -e "${bold_red}[DISABLED]${end}"
fi
echo

echo -e "${bold_yellow}${warning_sign} Virtual environment deactivated!${end}"
deactivate
