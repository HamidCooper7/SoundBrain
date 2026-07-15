import fitz
import numpy as np
from paddleocr import PaddleOCR


ocr = PaddleOCR(
    lang="fa",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
)


def load_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    pages = []

    for page_number in range(len(doc)):

        page = doc.load_page(page_number)

        pix = page.get_pixmap(
            dpi=300,
            alpha=False,
        )

        img = np.frombuffer(
            pix.samples,
            dtype=np.uint8,
        ).reshape(
            pix.height,
            pix.width,
            pix.n,
        )

        result = ocr.predict(img)

        text = ""

        try:

            if result:

                res = result[0]

                if "rec_texts" in res:

                    text = "\n".join(res["rec_texts"])

        except Exception as e:

            print(f"OCR Error Page {page_number+1}: {e}")

        pages.append(
            {
                "text": text.strip(),
                "page": page_number + 1,
                "source": pdf_path,
            }
        )

    doc.close()

    return pages