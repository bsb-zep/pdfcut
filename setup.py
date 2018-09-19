import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["sys", "csv", "winsound", "os", "tkinter", "io", "PyPDF2"], "includes": ["pfdcut/step_one", "pdfcut/step_two"]}

setup(
    name = "pdfcut",
    version = "3.1",
    description = "cut volume pdfs into granular sizes",
    options = {"build_exe": build_exe_options},
    executables = [Executable("pdfcut/__main__.py", base = "Console")])