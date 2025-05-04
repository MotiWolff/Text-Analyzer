# Text Analyzer

A modern Django web application for analyzing text content with advanced features and insights.

## Features

- Text analysis through direct input or file upload
- Support for multiple file formats (TXT, DOCX, PDF)
- Word frequency analysis
- Sentence statistics
- Word length patterns
- Equal length word sequences
- Modern, responsive UI with dark mode support
- Print-friendly results

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cyberLibrary
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Usage

1. **Text Input**
   - Visit the home page
   - Enter or paste your text
   - Click "Analyze Text"

2. **File Upload**
   - Click "Upload File"
   - Select a supported file (TXT, DOCX, PDF)
   - Click "Analyze File"

3. **View Results**
   - See word statistics
   - Explore frequency analysis
   - Check word length patterns
   - Print or save results

## Technologies

- Python 3.x
- Django 5.x
- Bootstrap 5.x
- Font Awesome 6.x
- python-docx
- PyPDF2
- chardet

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 