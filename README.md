# Plagiarism Detection

This is a Python-based project that detects plagiarism between text documents by comparing their content and calculating similarity scores.

## Features

- Compare two or more text documents.
- Generate a similarity percentage using text analysis.
- Simple command-line interface for easy testing.

## Technologies Used

- Python 3
- Standard libraries (`os`, `re`, etc.)
- [difflib](https://docs.python.org/3/library/difflib.html) for text comparison

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ommisandeep/Plagarism_Detection.git
cd Plagarism_Detection
```

### 2. Install dependencies

If there's a `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Or if not, just make sure you have Python 3 installed.

### 3. Run the script

```bash
python app.py
```
You will be prompted to input the filenames you want to compare. Make sure the files exist in the same directory.

## Example

You can place two `.txt` files in the directory, like:
- `file1.txt`
- `file2.txt`

Then run the program and input these filenames when prompted.

## Output

- The program prints a similarity percentage.
- Highlights matching lines (optional depending on implementation).

## 📬 Contact

Developed by Ommi Sandeep  
Email: [ommisandeep16@gmail.com](mailto:ommisandeep16@gmail.com)  
GitHub: [@ommisandeep](https://github.com/ommisandeep)
