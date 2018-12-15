# Majorcord
[Majorcord](https://github.com/ThomasFrew/Majorcord) is an open-source messaging platform inspired by a love for [Discord](https://discordapp.com/) and sheet music, hence the pun! Built using [Python 3.7](https://www.python.org/downloads/release/python-370/), Majorcord allows an infinite number of users to communicate freely on a shared plain text (.txt) file. If you have the time, feel free to download and test it on your network [here](https://github.com/ThomasFrew/Majorcord/releases)!

## Installing
This simple how-to guide will show to download and run Majorcord on your local machine for testing purposes.


### Prerequisites
All your macine will need to run Majorcord is [Python 3.7](https://www.python.org/downloads/release/python-370/). This should install all modules that the program requires. *(i.e. Tkinter, datetime, ect)*.

### Installation
To run Majorcord, you will need the following files:
* The Python (.py) file that contains all Source Code.
* Four plain text (.txt) files for the program to reference and write messages to.

Currently, the application only references the location of the text files by name: meaning that they must be kept in the same folder.  To change this, edit the `file_location` attrbiute of each `Server` object. These can be found in the top-level section of the program:
```
server_1_attributes = Server("Server 1 (G♯)", "server_1_button", "Server 1 (G sharp).txt")
```

## Interface
Majorcord uses three core aspects within its interface to ensure ease of access for the user:

### Menu bar
Majorcord's menu bar (referenced as `menu_bar`) contains various menus with commands vital to the application. Some allow users to change previous variables (such as their `username`), others reload the past N messages to check for new messages.

### Canvas
Majorcord's canvas (refrenced as `window`) is arguably the most important aspect of the program, which dynamically adjusts its widgets to serve the user's various needs. This uses a unique for-array system, which allows developers to add new widgets at ease.
```
enter_username_widgets = ["username_entry", "username_button"]

    for i in write_messages_widgets:
        eval(i).grid_forget()
```

### Console
Majorcord also utilises Python's console to display lines of text too great in number to be diplayed in the interface.However, Majorcord may later be developed to no longer rely on this console.

## Contributing 
*Contribution documents have not been developed yet. Sorry about that!*

## Versioning
Musicord is currently at Version 1.0.0 (v1.0.0). See [Semantic Versioning](https://semver.org/) if you do not understand what this means.

## Lisence
Musicord is lisenced under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)- see [LISENCE.md](https://github.com/ThomasFrew/Majorcord/blob/master/LICENSE) a full disclosure of this.

## Acknowledgments
* Hats off to [Discord](https://discordapp.com/) for providing me with such the great inspiration and puns!
* Thanks to anyone who has checked out this repository: that means you!
