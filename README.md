[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# KeepConversion
Convert Keep data downloads to new versions/platforms

## Google Keep has NO ability to transport the contents of the Notes to any other platform OR a new version.
## While Google ATTEMPTS to transfer to new versions, it fails MANY times..

Therefore, I wrote this script to create an UPLOAD candidate that you can import into other platforms,
under Python and JSON to make it as cross-platform as possible...

## Application Execution

**To perform the conversion and prepare the import file for a new implementation or installation of Google Keep,**

- Go to Google Takeout
- Sign in with your Google account
- Click "Deselect all" (since Google defaults to exporting everything)
- Scroll down and check the box for "Keep"
- Click "Next step"
- Choose your export preferences:
- File type: .zip (standard) or .tgz
- Archive size: Split into chunks if you have a lot of notes
- Delivery method: Email download link, Google Drive, Dropbox, etc.
- Click "Create export"
- Wait for the email (can take minutes to hours depending on data volume)
- Download the .zip file and extract it (By right-clicking on it, and then selecting extract to CURRENT DIR)
What you get: Your notes as HTML files, plus any attached images/audio in their original formats.
---
- [Saved location] Location where you've downloaded the script itself
- [Base directory] Location of the download file from Google Takeout. 
```bash
python3 [Saved location]/main.py --input [Base directory]  --output ./test.json
