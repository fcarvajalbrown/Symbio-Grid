"""Build paper-polis.docx from paper-polis.md per Polis (Revista Latinoamericana) format,
verified directly against https://polis.ulagos.cl/index.php/polis/about/submissions:
title 14pt bold centered; body Century Gothic 10pt justified, 1.5 line spacing; headings
(no numbering) 12pt/11pt bold centered; abstract/keywords blocks 10pt left-aligned, single
spacing; references single-spaced. Blind review: no author identity in the manuscript body,
and author metadata is stripped from the docx file properties."""
import re
from pathlib import Path
import pypandoc
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

HERE = Path(__file__).resolve().parent
BODY_FONT = "Century Gothic"
TITLE_TEXT = ("Cooperación evolutiva frente al límite biofísico de un recurso de uso común: "
              "una simulación basada en agentes de una economía de intercambio")
LANGUAGE_BLOCK_PREFIXES = (
    "Resumen:", "Abstract:", "Resumo:",
    "Palabras clave:", "Keywords:", "Palavras-chave:",
    "English title:", "Título em português:",
)


def strip_front_matter(src: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    body = m.group(2) if m else src
    return re.sub(r"<!--.*?-->", "", body, flags=re.S)


def set_line_spacing(paragraph, multiple):
    paragraph.paragraph_format.line_spacing = multiple


def style_run_sizes(paragraph, size_pt):
    for run in paragraph.runs:
        run.font.size = Pt(size_pt)
        run.font.name = BODY_FONT


def main():
    src = (HERE / "paper-polis.md").read_text(encoding="utf-8")
    body = strip_front_matter(src)

    tmp = HERE / "_polis_build.md"
    tmp.write_text(body, encoding="utf-8")
    docx_path = HERE / "paper-polis.docx"
    pypandoc.convert_file(str(tmp), "docx", outputfile=str(docx_path),
                          extra_args=["--resource-path", str(HERE)])
    tmp.unlink()

    doc = Document(str(docx_path))

    # Document-wide defaults: Century Gothic 10pt, justified, 1.5 line spacing.
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(10)
    normal.paragraph_format.line_spacing = 1.5
    for paragraph in doc.paragraphs:
        set_line_spacing(paragraph, 1.5)
        if paragraph.alignment is None:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        style_run_sizes(paragraph, 10)

    # Heading styles: no numbering (already removed in source), 12pt/11pt bold centered.
    for level, size in ((1, 12), (2, 12), (3, 11)):
        try:
            style = doc.styles[f"Heading {level}"]
            style.font.name = BODY_FONT
            style.font.size = Pt(size)
            style.font.bold = True
            style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        except KeyError:
            pass

    in_references = False
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()

        if text.startswith("Referencias"):
            in_references = True
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_line_spacing(paragraph, 1.0)
            style_run_sizes(paragraph, 12)
            for run in paragraph.runs:
                run.bold = True
            continue

        if text == TITLE_TEXT:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_line_spacing(paragraph, 1.0)
            style_run_sizes(paragraph, 14)
            for run in paragraph.runs:
                run.bold = True

        elif text.startswith(LANGUAGE_BLOCK_PREFIXES):
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
            set_line_spacing(paragraph, 1.0)
            style_run_sizes(paragraph, 10)

        elif in_references and text:
            set_line_spacing(paragraph, 1.0)
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Strip author identification from document properties (blind review requirement).
    props = doc.core_properties
    props.author = ""
    props.last_modified_by = ""
    props.comments = ""

    doc.save(str(docx_path))
    print(f"wrote {docx_path}")

    try:
        tmp2 = HERE / "_polis_build.md"
        tmp2.write_text(body, encoding="utf-8")
        pypandoc.convert_file(str(tmp2), "pdf", outputfile=str(HERE / "paper-polis.pdf"),
                              extra_args=["--resource-path", str(HERE), "--pdf-engine=xelatex"])
        tmp2.unlink()
        print(f"wrote {HERE / 'paper-polis.pdf'}")
    except Exception as e:
        print(f"PDF build skipped ({type(e).__name__}); docx is ready. Detail: {str(e)[:200]}")


if __name__ == "__main__":
    main()
