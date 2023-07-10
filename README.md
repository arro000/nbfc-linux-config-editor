
# NBFC Config Editor

This is a simple configuration editor for NBFC (NoteBook FanControl) on Linux, built with Python and GTK. This tool allows you to modify the NBFC JSON configuration file through an intuitive graphical interface.

## Requirements

This project requires:

- Python 3
- GTK 3
- PyGObject

## Installation

To install the dependencies, you can use your preferred package manager. For example, on Ubuntu, run:

```
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

## Usage

To start the application, run `main.py`:

```
python3 main.py
```

In the graphical interface, you can modify the values in the NBFC configuration file. When you're done, click "Save" to save your changes and restart the NBFC service.

## Notes

Keep in mind that running commands that require root privileges (like `sudo systemctl restart nbfc`) from a Python program can be risky. Make sure you understand the potential security implications before using this tool.

## License

This project is released under the MIT license. See the `LICENSE` file for details.
