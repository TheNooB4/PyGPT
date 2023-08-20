#!/bin/bash

packages=("setuptools" "requests" "pyfiglet" "termcolor" "openai" "colorama")

for package in "${packages[@]}"
do
    if ! pip show "$package" > /dev/null 2>&1; then
        # Package is not installed, install it
        pip install "$package"
    fi  
done
clear
termux-setup-storage
rm -f /data/data/com.termux/files/usr/bin/Gpt
echo -e '#!/bin/bash\npython3 /data/data/com.termux/files/home/PyGPT/Gpt.py' > /data/data/com.termux/files/usr/bin/Gpt
chmod +x /data/data/com.termux/files/usr/bin/Gpt
source /data/data/com.termux/files/usr/.bashrc
clear
sleep 1
echo -e "\033[1;33mShortcut 'Gpt' has been created. You can run the code by typing 'Gpt' in Termux terminal anytime you want to use.\033[0m"
