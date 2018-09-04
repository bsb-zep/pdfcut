import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["sys", "csv", "winsound", "os", "tkinter", "io", "PyPDF2"], "includes": ["step1", "step2"]}

setup(
    name = "pdfcut",
    version = "3.1",
    description = "cut volume pdfs into granular sizes",
    options = {"build_exe": build_exe_options},
    executables = [Executable("__main__.py", base = "Console")])