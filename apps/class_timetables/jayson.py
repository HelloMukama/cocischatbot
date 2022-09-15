import fitz
import json


def upload_timetable_logic(request):
    document = fitz.open('filename.pdf')
    page = document.loadPage(14)  # enter page
    text = page.getText('dict')
    # print(text)

    with open('data.json', 'w') as f:
        text_data = json.dump(text, f)
