import json
from pathlib import Path
from typing import Optional

import requests

from src.snippet.language import Language
from src.snippet.theme import Theme

SOURCECODESHOTS_URL = "https://sourcecodeshots.com/api/image"


class Snippet:
    def __init__(self, content: str, language: Language) -> None:
        self._content = content
        self._language = language

    def __repr__(self) -> str:
        return f"Snippet(content={self._content}, language={self._language})"

    @property
    def content(self) -> str:
        return self._content

    @property
    def language(self) -> Language:
        return self._language

    @classmethod
    def from_file(cls, path: Path) -> "Snippet":
        """Create a Snippet object from a file.

        Args:
            path (Path): The path of the file.

        Returns:
            Snippet: The Snippet object.
        """
        with open(path) as f:
            content = f.read()
        return cls(content, Language.from_suffix(path.suffix[1:]))

    def get_image(
        self,
        theme: Theme,
        location: Optional[Path] = None,
        filename: Optional[str] = None,
    ) -> Path:
        """Get the image of a code snippet, from the Source Code Shots API.

        https://sourcecodeshots.com/docs

        Args:
            theme (str): The theme of the code snippet.
            location (Optional[Path], optional): The location of the image file. Defaults to None.
            filename (Optional[str], optional): The filename of the image file. Defaults to None.

        Returns:
            Path: The path of the image file.
        """
        filename = (
            f"snippet-{hash((self._content, self._language, theme))}"
            if filename is None
            else filename
        )
        location = Path("snippets") if location is None else location

        if not location.is_dir():
            raise ValueError("Location must be a valid directory path.")
        if not filename.isidentifier():
            raise ValueError("Filename must be a valid identifier.")

        image_path = location / f"{filename}.png"

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "CodeFluencer",
        }
        data = {
            "code": self._content,
            "settings": {
                "language": self._language.value,
                "theme": theme.value,
            },
        }
        response = requests.post(
            url=SOURCECODESHOTS_URL,
            headers=headers,
            data=json.dumps(data),
            timeout=10,
            verify=True,
            stream=True,
        )

        # Ensure the request was successful
        response.raise_for_status()

        # Ensure the directory exists
        image_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the image data to a file
        with open(image_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return image_path
