from enum import Enum

LANGUAGE_SUFFIXES = {
    "adb": "ada",
    "bat": "batch",
    "c": "c",
    "cs": "csharp",
    "cpp": "cpp",
    "clj": "clojure",
    "cob": "cobol",
    "coffee": "coffee",
    "lisp": "commonlisp",
    "cr": "crystal",
    "css": "css",
    "feature": "gherkin",
    "d": "dscript",
    "dart": "dart",
    "diff": "diff",
    "html": "django",
    "Dockerfile": "dockerfile",
    "ex": "elixir",
    "elm": "elm",
    "erl": "erlang",
    "fs": "fsharp",
    "f": "fortran",
    "txt": "git-commit",
    "txt": "git-rebase",
    "go": "go",
    "graphql": "graphql",
    "groovy": "groovy",
    "hbs": "handlebars",
    "hs": "haskell",
    "hlsl": "hlsl",
    "html": "html",
    "gitignore": "ignore",
    "cfg": "cfg",
    "java": "java",
    "js": "js",
    "json": "json",
    "jsonc": "jsonwithcomments",
    "jsx": "jsx",
    "jl": "julia",
    "kts": "kts",
    "tex": "latex",
    "less": "less",
    "log": "log",
    "lua": "lua",
    "mk": "makefile",
    "md": "markdown",
    "m": "mathematica",
    "nt": "ntriples",
    "conf": "nginx",
    "nim": "nim",
    "m": "objective-c",
    "mm": "objective-cpp",
    "ml": "ocaml",
    "m": "octave",
    "pas": "pascal",
    "pl": "perl",
    "php": "php",
    "txt": "text",
    "ps1": "powershell",
    "py": "python",
    "r": "r",
    "rkt": "racket",
    "p6": "perl6",
    "re": "reason",
    "lisp": "reason_lisp",
    "res": "rescript",
    "s": "riscv",
    "rb": "ruby",
    "rs": "rust",
    "sass": "sass",
    "scala": "scala",
    "scm": "scheme",
    "scss": "scss",
    "shader": "shaderlab",
    "sh": "shellscript",
    "st": "smalltalk",
    "sql": "sql",
    "swift": "swift",
    "tcl": "tcl",
    "toml": "toml",
    "tsx": "tsx",
    "twig": "twig",
    "ts": "ts",
    "v": "verilog",
    "vhdl": "vhdl",
    "vb": "visualbasic",
    "vue": "vue",
    "xml": "xml",
    "xq": "xquery",
    "yaml": "yaml",
    "zig": "zig",
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
        return cls(LANGUAGE_SUFFIXES[suffix.lower()])
