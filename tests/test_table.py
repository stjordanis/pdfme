from pdfme import PDF
import json
from pathlib import Path

from .utils import gen_table

def run_test(index):
    pdf = PDF()
    pdf.add_page()
    name = 'test_table{}'.format(index)
    input_file = Path(name + '.json')
    if input_file.exists():
        with input_file.open() as f:
            content = json.load(f)
    else:
        content = gen_table(20)
        with input_file.open('w') as f:
            json.dump(content, f, ensure_ascii=False)

    pdf.table(content)
    with open('test_table{}.pdf'.format(index), 'wb') as f:
        pdf.output(f)

def test_content(index=None):
    if index is not None:
        run_test(index)
    else:
        for i in range(3):
            run_test(i)
