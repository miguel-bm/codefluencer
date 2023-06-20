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
        headers = {"Content-Type": "application/json"}
        data = {
            "code": self._content,
            "settings": {
                "language": self._language.value,
                "theme": theme.value,
            },
        }
        response = requests.post(
            SOURCECODESHOTS_URL, headers=headers, data=json.dumps(data)
        )

        # Ensure the request was successful
        response.raise_for_status()

        # Create a Path object for the new file
        filename = (
            f"snippet-{hash((self._content, self._language, theme))}"
            if filename is None
            else filename
        )
        location = Path("snippets") if location is None else location
        image_path = location / f"{filename}.png"
        image_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the image data to a file
        with open(image_path, "wb") as f:
            f.write(response.content)

        return image_path
