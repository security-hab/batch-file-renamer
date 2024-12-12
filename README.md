# BatchFileRenamer 🗂

**BatchFileRenamer** is a Python utility for automatically renaming all files in a specified directory by assigning them sequential numeric names while preserving their original extensions.

## Features 🌟
- ✨ Automatically renames all files in a directory with sequential numbers starting from 0.
- 📝 Preserves file extensions.
- 🔒 Skips directories within the target folder.
- 🔔 Provides user-friendly error handling and status updates.

## Requirements 📚
- Python 3.6 or higher

## Installation 📥
Clone the repository:
```bash
git clone https://github.com/security-hab/batch-file-renamer.git
cd batch-file-renamer
```

## Usage 🚀
1. Edit the `directory` variable in the script to specify the path of the directory you want to process:
   ```python
   directory = "/path/to/your/directory"
   ```

2. Run the script:
   ```bash
   python main.py
   ```

## Example 🖌
Before renaming:
```
document1.pdf
photo1.jpg
notes.txt
```

After renaming:
```
0.pdf
1.jpg
2.txt
```

## Notes 📊
- Ensure you have write permissions for the target directory.
- Files are processed in sorted order for predictable renaming.

## Contributing 📚
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License 🔒
This project is licensed under the MIT License. See the `LICENSE` file for details.

