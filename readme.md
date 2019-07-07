<div align="center">
  <a href="clipco.de"><img src="https://i.imgur.com/qvolQzy.png" alt="Clipcode" width="40%" height="40%"></a><h4 align="center">Easiest way to share your code snippets</h4>
</div>

## Usage
+ Select and Copy your code
+ Hit Insert button
+ Select Syntax Highlighting and Upload
+ Get Sharable link

<div>
  <a href="https://marketplace.visualstudio.com/items?itemName=SmellyCharlie.clipcode"><img src="https://clipco.de/img/vs.png"></a>
</div>

##  Linux
```bash
$ git clone https://github.com/shobhit99/clipcode
$ cd clipcode
$ chmod +x install.sh
$ sudo ./install.sh
```
> Additionally for arch users
```bash
 $ sudo pacman -S tk
```
> If you get error "Pyperclip could not find a copy/paste mechanism for your system" Install the listed packages in [here](https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error) 

##  Windows
```powershell
> git clone https://github.com/shobhit99/clipcode
> cd clipcode
> python3.7 -m pip install requirements.txt
> python3.7 clipcode.py
# Or generate Exe
> python3.7 -m pip install pyinstaller
> pyinstaller clipcode.py
```
> Execute clipcode.exe from dist/clipcode/clipcode.exe

