import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def html_content():
    with open("CSS0201.html", "r", encoding="utf-8") as file:
        return file.read()

def test_name_box_styles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    style_tag = soup.find('style')
    assert style_tag is not None, "Style tag is missing."
    
    styles = style_tag.string
    assert '.name-box' in styles, "Class .name-box not found in styles."
    assert 'border: 3px solid #800080' in styles, "Border style is incorrect."
    assert 'padding: 17px' in styles, "Padding style is incorrect."
    assert 'margin: 10%' in styles, "Margin style is incorrect."

def test_name_box_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    name_box = soup.find('div', class_='name-box')
    assert name_box is not None, "Div with class 'name-box' is missing."
    assert name_box.has_attr('contenteditable'), "Name box should be editable."
