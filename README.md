# SummaVid

## Getting started

Below is a quick start guide on how to install and obtain everything this projects need in order to run, with version numbers at the time of writing this guide. We recommend installing the same versions as we did (by specifying version numbers and modifying the below given commands) as we cannot promise compatibility wihin the codebase and between different libraries:

- Python (3.11.5)
- PyTorch (2.0.1)
- FFmpeg through Chocolatey (Windows) or Homebrew (MacOS)
- a local installation of OpenAI's Whisper,
- The OpenAI library,
- Flask, and
- An API key from OpenAI.

### Python

Install Python by going to http://python.org. Choose the appropriate version for your operating system. Remember to select add to PATH when installing.
Make sure you know which interpreter you are using when installing packages and running the project.

### PyTorch

Go to https://pytorch.org/get-started/locally

Install **Stable**. Choose CUDA if you have a high performance GPU and your computer supports it. Apple silicon users do NOT select this option.

### FFmpeg

Depending on your operating system, either install Chocolatey (Windows) or Homebrew (MacOS) in order to have a package manager for installing FFmpeg.

- Chocolatey: https://chocolatey.org/install (Choose Individual)
- Homebrew: https://brew.sh

We do not currently have any developers on Linux, but an installation option for Linux is theoretically possible.
Again, remember to add the package managers to PATH.

Install FFmpeg by:

- On windows, open PowerShell with admin privillages and type `choco install ffmpeg`.
- On MacOS, open the Terminal and type `brew install ffmpeg `

### OpenAI's whisper

- On windows, open Command Prompt with admin privillages and type `pip install -U openai-whisper`.
- On MacOS, open the Terminal and type `sudo pip install -U openai-whisper `

If it does not work, try replacing `pip` with `pip3`.

### OpenAI library

- On windows, open Command Prompt with admin privillages and type `pip install --upgrade openai`.
- On MacOS, open the Terminal and type `sudo pip install -- openai `

If it does not work, try replacing `pip` with `pip3`.

### Flask

- On windows, open Command Prompt with admin privillages and type `pip install flask`.
- On MacOS, open the Terminal and type `sudo pip install flask `

If it does not work, try replacing `pip` with `pip3`.

### OpenAI key

You will have to register for an OpenAI account and obtain an OpenAI secret key from them. The process is very straightforward.
https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key

New users have free credits for API use for a certain quota. Then you can pay per use or do a subscription.
https://openai.com/pricing
Note that you will only be paying for GPT prices. Whisper is running locally and you will NOT be charged by the Whisper API.

## Usage

Navigate (cd) to the project directory and type the following in your terminal/command prompt
`python app.py` or `python3 app.py`, whichever works.

The program will specify which address the web front-end is located. For example: http://127.0.0.1:5000

You will be able to upload your file and specify parameters when running the project.

### Video/ Audio type

You will be able to choose from

- Lecture: Summary, Important dates and Transcript in output
- Meeting: Summary, Important dates and Transcript in output
- Other: Summary and Transcript in output

Each option will have a different prompt tweaked to best capture the most accurate and useful information in that context.

### Language

Whisper offers spcialized models that works specifically for the English language. Choose English if the file is in English. This will ensure better recognition. Many other languages are supported, have fun trying it out!

### Transcription

You can select the precision when transcribing the audio here. Higher settings lead to more accurate transcription but exponentially increases the processing time.

### Context

If your content is relatively short (within ~3000) words, you can choose between **Standard Complexity (Under ~3000 words)** and **Complex Ideas (Under ~3000 words)**, which uses **gpt-3.5-turbo** and **gpt-4** respectively. **Complex Ideas** can understand more complicated topics and often give more accurate summarizations of the transcript.

If your content is relatively longer, choose **Standard Complexity (Under ~12000 words)**. The model will be able to be fed longer videos with more words.

### API key

Paste your API key from OpenAI here.

### Run

Hit run and wait patiently, you will be able to watch the script do its work in the terminal if you wish to.

## Stopping the program

Simply close the terminal or command prompt or hit Ctrl+C.
