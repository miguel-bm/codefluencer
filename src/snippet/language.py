from enum import Enum

LANGUAGE_SUFFIXES = {
    "py": "python",
    "js": "javascript",
    "rs": "rust",
}


class Language(str, Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    RUST = "rust"

    @classmethod
    def from_suffix(cls, suffix: str) -> "Language":
        """Get the Language enum from a file suffix.

        Args:
            suffix (str): The suffix of the file.

        Returns:
            Language: The Language enum.
        """
        return cls(LANGUAGE_SUFFIXES[suffix])
