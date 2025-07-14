from fpdf import FPDF
from typing import Callable, Dict, List, Optional, Tuple
from translations import TRANSLATIONS, REQUIRED_KEYS


class PDFStyle:
    def apply(self, pdf: FPDF):
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_margins(left=15, top=15, right=15)
        pdf.set_font("Arial", size=12)
        pdf.set_fill_color(240, 240, 240)


class PDFGenerator:
    def __init__(self, language: str = 'en'):
        if language not in TRANSLATIONS:
            raise ValueError(f"Unsupported language '{language}'")
        self.language = language
        self.translations = TRANSLATIONS[language]
        self._check_required_keys()

        self.pdf = FPDF()
        self.style = PDFStyle()
        self.part_generators: List[Callable[[FPDF, Dict[str, str]], None]] = []

    def _check_required_keys(self):
        missing = [k for k in REQUIRED_KEYS if k not in self.translations]
        if missing:
            raise KeyError(f"Missing translations for keys: {missing}")

    def translate(self, key: str) -> str:
        if key not in self.translations:
            raise KeyError(f"Missing translation for key '{key}' in language '{self.language}'")
        return self.translations[key]

    def add_part(self, generator_func: Callable[[FPDF, Dict[str, str]], None], title: Optional[str] = None):
        """Register a section generator function or method, with optional title"""
        self.part_generators.append((title, generator_func))

    def generate(self, output_path: str):
        self.pdf.add_page()
        self.style.apply(self.pdf)

        # Title
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, self.translate('title'), ln=True, align='C')
        self.pdf.ln(10)

         # Render parts
        for idx, (title, part_func) in enumerate(self.part_generators):
            if idx > 0:
                self.pdf.add_page()
                self.style.apply(self.pdf)

            if title:
                self.pdf.set_font("Arial", 'B', 14)
                self.pdf.cell(0, 10, title, ln=True)
                self.pdf.ln(5)

            part_func(self.pdf, self.translations)


        # Footer
        self._add_footer()

        self.pdf.output(output_path)

    def _add_footer(self):
        self.pdf.set_y(-15)
        self.pdf.set_font("Arial", 'I', 10)
        self.pdf.cell(0, 10, self.translate('footer'), 0, 0, 'C')
