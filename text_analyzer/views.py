from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TextAnalysisForm, FileUploadForm
from .models import TextAnalysis
from .utils import analyze_text
import os
from django.conf import settings
import docx
import PyPDF2
import chardet
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

def home(request):
    try:
        if request.method == 'POST':
            form = TextAnalysisForm(request.POST)
            if form.is_valid():
                analysis = form.save(commit=False)
                analysis.analyze()
                return redirect('results', analysis_id=analysis.id)
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = TextAnalysisForm()
        return render(request, 'text_analyzer/home.html', {'form': form})
    except Exception as e:
        logger.error(f"Error in home view: {str(e)}")
        messages.error(request, 'An error occurred. Please try again.')
        return render(request, 'text_analyzer/home.html', {'form': TextAnalysisForm()})

def upload_file(request):
    try:
        if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES['file']
                file_content = ''
                
                try:
                    # Read file content based on file type
                    if uploaded_file.name.endswith('.txt'):
                        # Detect encoding for text files
                        raw_data = uploaded_file.read()
                        result = chardet.detect(raw_data)
                        encoding = result['encoding']
                        file_content = raw_data.decode(encoding)
                    
                    elif uploaded_file.name.endswith('.docx'):
                        doc = docx.Document(uploaded_file)
                        file_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
                    
                    elif uploaded_file.name.endswith('.pdf'):
                        pdf_reader = PyPDF2.PdfReader(uploaded_file)
                        file_content = ''
                        for page in pdf_reader.pages:
                            file_content += page.extract_text() + '\n'
                    
                    else:
                        form.add_error('file', 'Unsupported file format')
                        return render(request, 'text_analyzer/upload.html', {'form': form})
                    
                    # Create and save analysis
                    analysis = TextAnalysis(
                        title=form.cleaned_data['title'] or uploaded_file.name,
                        content=file_content
                    )
                    analysis.analyze()
                    return redirect('results', analysis_id=analysis.id)
                except Exception as e:
                    logger.error(f"Error processing file: {str(e)}")
                    form.add_error('file', 'Error processing file. Please try again.')
                    return render(request, 'text_analyzer/upload.html', {'form': form})
        else:
            form = FileUploadForm()
        return render(request, 'text_analyzer/upload.html', {'form': form})
    except Exception as e:
        logger.error(f"Error in upload_file view: {str(e)}")
        messages.error(request, 'An error occurred. Please try again.')
        return render(request, 'text_analyzer/upload.html', {'form': FileUploadForm()})

def results(request, analysis_id):
    try:
        analysis = TextAnalysis.objects.get(id=analysis_id)
        return render(request, 'text_analyzer/results.html', {'analysis': analysis})
    except TextAnalysis.DoesNotExist:
        messages.error(request, 'Analysis not found.')
        return redirect('home')
    except Exception as e:
        logger.error(f"Error in results view: {str(e)}")
        messages.error(request, 'An error occurred. Please try again.')
        return redirect('home')