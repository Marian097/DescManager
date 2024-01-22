from cx_Freeze import setup, Executable


setup(
    name="DescManager",
    version="1.0",
    description="'DescManager' este o aplicație intuitivă și prietenoasă, proiectată pentru a-ți ușura gestionarea consumurilor, a clienților și a adreselor de livrare. Cu funcționalități puternice și un design elegant, DescManager este partenerul tău de încredere în optimizarea afacerii tale.",
    executables=[Executable("main.py", base="Win32GUI")],
)

