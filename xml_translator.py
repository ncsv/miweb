import xml.etree.ElementTree as ET
from typing import List

try:
    from googletrans import Translator
except ImportError as exc:  # pragma: no cover - handled at runtime
    raise SystemExit(
        "googletrans package is required. Install with 'pip install googletrans==4.0.0-rc1'"
    ) from exc


def translate_elements(elements: List[ET.Element], language: str) -> None:
    translator = Translator()
    for element in elements:
        if element.text:
            element.text = translator.translate(element.text, dest=language).text


def main() -> None:
    xml_path = input("Enter path to XML file: ").strip()
    tree = ET.parse(xml_path)
    root = tree.getroot()

    xpath = input("Enter XPath of elements to translate: ").strip()
    language = input("Target language code (es for Spanish, ca for Catalan): ").strip()

    elements = root.findall(xpath)
    translate_elements(elements, language)

    output_path = input("Enter output file path: ").strip()
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
