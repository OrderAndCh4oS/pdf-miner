# PDF Text Extractor

A Python script to extract text from PDF documents and filter the extracted content based on paragraph length and regex patterns.

## Features

- Extracts text from PDF files
- Splits the extracted text into paragraphs
- Filters paragraphs based on specified minimum length and regex pattern (long chain of numbers)
- Saves filtered results as a pickle file
- Displays stored_results as output

## Requirements

- Python 3.x
- pdfminer.six library (For details, check: <https://pdfminersix.readthedocs.io/>)

To install required libraries, run:

```bash
pip install pdfminer.six 
```

## Usage

Place the desired PDF files in `./documents/` directory. Update the `path` variable in the script with your chosen filename.

```python
path = Path("./documents/Your-PDF-Filename.pdf")
```

Run the script:

```bash
python main.py
```

Results will be saved in a pickle file inside `./results/` directory, with a name format as: `Filename.pickle`.

To read stored results from pickle file, use this code snippet:

```python
with open(f'results/{path.stem}.pickle', 'rb') as handle:
    stored_result = pickle.load(handle)
print(stored_result)
```

## Example Output Structure for Stored Result 

The structure of saved result is a dictionary containing following keys:
 
 ```
{
    "total_lines": int,
    "total_chars": int,
    "skipped_lines": int,
    "skipped_chars": int,
    "selected_lines": int,
    "selected_chars": int,
    "paragraphs": List[str]
}
 ```

Where,

 - total_lines: Total number of lines in extracted text.
 - total_chars: Total number of characters in extracted text.
 - skipped_lines: Number of lines skipped during filtering process.
 - skipped_chars: Number of characters skipped during filtering process.
 - selected_lines: Number of lines retained after filtering.
 - selected_chars: Number of characters retained after filtering.
 - paragraphs: List containing filtered paragraphs.


## License

This project is open-sourced under the [MIT license](LICENSE).
