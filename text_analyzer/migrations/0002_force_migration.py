from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('text_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
            CREATE TABLE IF NOT EXISTS text_analyzer_textanalysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                content TEXT NOT NULL,
                created_at DATETIME NOT NULL,
                word_count INTEGER NOT NULL,
                sentence_count INTEGER NOT NULL,
                unique_words_count INTEGER NOT NULL,
                most_common_word VARCHAR(100) NOT NULL,
                most_common_word_count INTEGER NOT NULL,
                average_word_length FLOAT NOT NULL,
                longest_words JSON NOT NULL,
                frequency_words JSON NOT NULL,
                equal_length_sequences JSON NOT NULL
            );
            ''',
            reverse_sql='DROP TABLE IF EXISTS text_analyzer_textanalysis;'
        ),
    ] 