from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from transcription_service import TranscriptionService
from summarization_service import SummarizationService
from important_dates_service import ImportantDatesService
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Make sure this folder exists

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

transcription_service = TranscriptionService()
summarization_service = SummarizationService()
important_dates_service = ImportantDatesService()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run', methods=['POST'])
def run_the_thing():
    # link = request.form['link']
    video_type = request.form['video_type']
    whisper_model = request.form['whisper_model']
    gpt_model = request.form['gpt_model']
    api_key = request.form['api_key']

    file = request.files.get('file')
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        link = file_path

    transcript = transcription_service.transcribe(link, whisper_model, api_key)
    summary = summarization_service.summarize(transcript, gpt_model, api_key)
    if (video_type == "lecture"):
        important_dates = important_dates_service.get_dates(
            transcript, gpt_model, api_key)
    else:
        important_dates = "N/A"

    return render_template('index.html', summary=summary, important_dates=important_dates)


if __name__ == '__main__':
    app.run(debug=True)
