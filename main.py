from pdfminer.high_level import extract_text
import os
import pandas as pd

# Get text from a .pdf
# Needs work - does not return all text from test inputs
def pdf_parser(filepath):
    text = extract_text(filepath)
    return text

# Get text from .txt a files
def txt_parser(filename: str) -> list:
    with open(filename) as file:
        txtContents = file.read()
        lines = txtContents.split('\n')
        return lines


def text_compiler(folder):
    files = os.listdir(path=folder)
    paths = [folder + filename for filename in files if '.txt' in filename]
    data_frames = [pd.read_table(
        file,
        header=None,
        on_bad_lines='skip',
        # encoding='unicode_escape',
        # encoding_errors='replace',
        lineterminator='\n'
        ) for file in paths]
    big_df = pd.concat(data_frames, axis=0)
    os.makedirs('./output', exist_ok=True)
    big_df.to_csv('./output/out.csv', header=['line'])

    print('complete')
    return

if __name__ == '__main__':
    # filepath = './dev/test_text_3.txt'
    # print(pd.read_table(filepath, header=None))
    # lines = txt_parser(filepath)
    # print(len(lines))
    # for line in lines:
    #     {'line': line,'tag': ''}
    folder = './dev/'
    text_compiler(folder)
