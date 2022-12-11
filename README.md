![logo](https://user-images.githubusercontent.com/68178267/153721662-5dc1a1c3-3cee-488b-be72-d0750750d367.png)
# Virtual Keyboard 
A GUI application made in python using tkinter

### [Download Here](https://github.com/AbhiK002/virtual-keyboard/releases/latest)

This is my first ever proper GUI based application project after learning tkinter recently. I made it to practice and get more used to working with tkinter.

### Features
- You can open the **keyboard settings menu** with the button in the bottom right corner
- The keyboard comes in 5 sizes:
	- Very Small
	- Small
	- Medium
	- Large
	- Very Large
- You can also change the opacity of the keyboard window! _Opacity ranges from 30% to 100%_.
- You can pin the keyboard so that it always stays on top of other windows. Opacity setting makes it really nice to use while pinned to the top.
- For the CTRL, SHIFT, ALT and WIN (special) keys, you can right click any of these to hold down them for as long as you want until you right click them again (like how we sometimes just hold the shift key to type instead of pressing CAPSLOCK).
- Adding to the last point, left clicking any of the 4 special keys will temporarily press them till you click any other key (excluding other special keys) (kind of like how we use CTRL+C or CTRL+ALT+DELETE).
- Has a [cute logo](https://github.com/AbhiK002/virtual-keyboard/blob/43b1af6691aec87d4a50ab47f79fb9d369935c3a/vkblogo.png).

## Usage
- Run the file `vkeyboard.pyw` directly

OR 
- Import the class `VirtualKeyboard` to your python program.
- To create (not display) the keyboard Graphical User Interface use:
```
objectName = VirtualKeyboard()
```
- To make the keyboard functional (i.e. bind the graphical keys to actual keypresses), use:
```
objectName.engine() 
```
- To start displaying your virtual keyboard (window), use:
```
objectName.start()
```
- Your keyboard is ready to use!
 
_(You can skip the `engine()` part if you only want a non functional dummy keyboard)_


## Requirements
Only needs the keyboard module to work properly.

How to install the `keyboard` module through `cmd`:

```
pip install keyboard
```
Read more about the [keyboard](https://pypi.org/project/keyboard/) module.

_Note: If the keyboard module is missing from user's computer (Windows only), the program will attempt to install the keyboard module automatically. In case that fails too, the virtual keyboard will still open in a non functional state allowing you admire its appearance and press all the buttons as much as want. 
You can also change the keyboard settings or pin/unpin the keyboard in non functional state._

### Please note:
- The program will _"flash"_ everytime you press any key, but will **definitely still be functional** in almost any text-entry application window.

## Screenshots

- Keyboard in action.
![s1main](https://user-images.githubusercontent.com/68178267/153722634-f70a6942-4976-4807-9fac-9efb7e188f05.png)
- Shift button right clicked to hold down SHIFT key until next click on the button.
![s6shift](https://user-images.githubusercontent.com/68178267/153722731-90f4930c-7ff1-43ea-8144-0a10b901410e.png)
- Keyboard with 70% opacity and Medium size (default).
![s2settings](https://user-images.githubusercontent.com/68178267/153747659-8aa5a779-a85b-492a-bb66-e0f5a165a3d3.png)
- Keyboard with 30% opacity and Very Small size.
![s3vsmall30](https://user-images.githubusercontent.com/68178267/153747661-ecb3de0b-8fba-4185-88c1-f7a4f5be06f9.png)
- Keyboard with 100% opacity and Very Large size.
![s4vlarge100](https://user-images.githubusercontent.com/68178267/153747662-7c05fe98-a5a9-461c-acb3-cab8a4330688.png)
- No background view blocked with the keyboard pinned :)
![s5fun](https://user-images.githubusercontent.com/68178267/154735178-765cd2aa-fe44-45f8-8a67-6bad5464ebfc.png)

### Thank You!
Hope you enjoy the keyboard!

I would *really* appreciate some feedback and tips!
[Reddit Post](https://www.reddit.com/r/Python/comments/svoo79/i_made_a_virtual_keyboard_my_first_ever_gui_based/)

( fun thing to do: add any PNG image in the same folder as the main python file and name it "vkblogo.png".... it should become the icon in the title bar of the keyboard :P )

GitHub: https://github.com/AbhiK002/virtual-keyboard
