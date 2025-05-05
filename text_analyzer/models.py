from django.db import models, transaction
from django.utils import timezone
from .utils import analyze_text
import logging

logger = logging.getLogger(__name__)

class TextAnalysis(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    # Analysis results
    word_count = models.IntegerField(default=0)
    sentence_count = models.IntegerField(default=0)
    unique_words_count = models.IntegerField(default=0)
    most_common_word = models.CharField(max_length=100, blank=True)
    most_common_word_count = models.IntegerField(default=0)
    average_word_length = models.FloatField(default=0.0)
    longest_words = models.JSONField(default=list)
    frequency_words = models.JSONField(default=dict)
    equal_length_sequences = models.JSONField(default=list)
    
    @transaction.atomic
    def analyze(self):
        """Analyze the text content and save results"""
        try:
            results = analyze_text(self.content)
            
            # Update model fields with analysis results
            self.word_count = results['word_count']
            self.sentence_count = results['sentence_count']
            self.unique_words_count = results['unique_words_count']
            self.most_common_word = results['most_common_word'][0]
            self.most_common_word_count = results['most_common_word'][1]
            self.average_word_length = results['average_word_length']
            self.longest_words = results['longest_words']
            self.frequency_words = results['frequency_words']
            self.equal_length_sequences = results['equal_length_sequences']
            
            # Save and refresh from database
            self.save()
            self.refresh_from_db()
            
            logger.info(f"Analysis saved successfully with ID: {self.id}")
            return self.id
        except Exception as e:
            logger.error(f"Error in analyze method: {str(e)}")
            raise
    
    def __str__(self):
        return self.title or f"Analysis {self.id}"