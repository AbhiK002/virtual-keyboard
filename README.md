![logo](https://user-images.githubusercontent.com/68178267/153721662-5dc1a1c3-3cee-488b-be72-d0750750d367.png)
# Virtual Keyboard 
A GUI application made in python using tkinter

This is my first ever proper GUI based application project after learning tkinter recently. I made it to practice and get more used to working with tkinter

## Features
- You can open the keyboard settings menu with the button in the bottom right corner
- The keyboard comes in 5 sizes:
	- Very Small
	- Small
	- Medium
	- Large
	- Very Large
- You can also change the opacity of the keyboard window! Opacity ranges from 30% to 100%
- You can pin the keyboard so that it always stays on top of other windows. Opacity setting makes it really nice to use while pinned to the top.
- For the CTRL, SHIFT, ALT and WIN (special) keys, you can right click any of these to hold down them for as long as you want until you right click them again (like how we sometimes just hold the shift key to type instead of pressing CAPSLOCK)
- Adding to the last point, left clicking any of the 4 special keys will temporarily press them till you click any other key (excluding other special keys) (kind of like how we use CTRL+C or CTRL+ALT+DELETE)
- Has a [cute logo](https://github.com/AbhiK002/virtual-keyboard/blob/43b1af6691aec87d4a50ab47f79fb9d369935c3a/vkblogo.png)

## Requirements
Only needs the keyboard module to work properly.
How to install the `keyboard` module through `cmd`:

```
pip install keyboard
```
Read more about the [keyboard](https://pypi.org/project/keyboard/) module

## Note
- The program will flash everytime you press any key (trying my best to fix)
- It might lose focus of the window you were typing in sometimes, so just pin the keyboard and click once wherever you want to enter the text; it will work 98% of the time.

## Screenshots

![s1main](https://user-images.githubusercontent.com/68178267/153722634-f70a6942-4976-4807-9fac-9efb7e188f05.png)
![s6shift](https://user-images.githubusercontent.com/68178267/153722731-90f4930c-7ff1-43ea-8144-0a10b901410e.png)
![s2settings](https://user-images.githubusercontent.com/68178267/153722636-43548ac7-1a73-41ff-80ab-bc8d2685408e.png)
![s3vsmall30](https://user-images.githubusercontent.com/68178267/153722638-7d52a45a-c658-4125-9709-19a36536b212.png)
![s4vlarge70](https://user-images.githubusercontent.com/68178267/153722640-ebcbe5aa-b820-4638-96e9-86c4ce4a9d47.png)
![s5fun](https://user-images.githubusercontent.com/68178267/153722641-1d16bcbe-a3f2-451c-a553-d86b92ee57cd.png)

### Thank You!
Enjoy the program :)
I would *really* appreciate some feedback and tips!

( fun thing to do: add any PNG image in the same folder as the main python file and name it "vkblogo.png".... it should become the icon in the title bar of the keyboard :P )
