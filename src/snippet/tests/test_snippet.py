import pytest
from src.snippet.snippet import Snippet
from src.snippet.language import Language
from src.snippet.theme import Theme
from pathlib import Path

PYTHON_CONTENT = """# Define a function that calculates the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Call the factorial function and print the result
result = factorial(num)
print("The factorial of", num, "is", result)
"""


@pytest.fixture
def sample_snippet():
    return Snippet(
        content=PYTHON_CONTENT,
        language=Language.PYTHON,
    )


def test_from_file(sample_snippet: Snippet):
    snippet = Snippet.from_file(Path("src/snippet/tests/samples/python_sample.py"))
    assert snippet.content == sample_snippet.content
    assert snippet.language == sample_snippet.language


def test_get_image(sample_snippet: Snippet):
    image_path = sample_snippet.get_image(
        theme=Theme.DARK_PLUS,
        location=Path("src/snippet/tests/images/"),
        filename="python_sample",
    )
    assert image_path.exists()
    assert image_path.suffix == ".png"
