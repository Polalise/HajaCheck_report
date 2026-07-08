"""HTML(스크린샷 PNG) -> pptx 조립 스크립트.
사용법: html/ 의 slide-*.html을 Playwright로 1920x1080 스크린샷 떠서
output/ 에 동일 이름의 .png로 저장한 뒤 이 스크립트를 실행하면
output/kimkwanyoung_임시.pptx 로 조립됩니다.
"""
import glob
import os

from pptx import Presentation
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(HERE, "output")
PPTX_PATH = os.path.join(OUTPUT_DIR, "kimkwanyoung_임시.pptx")

SLIDE_ORDER = [
    "slide-01-cover.png",
    "slide-02-toc.png",
    "slide-03-intro.png",
    "slide-05-plan.png",
    "slide-08-wrapup.png",
    "slide-09-mockup.png",
    "slide-10-ia-tree.png",
]


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    for name in SLIDE_ORDER:
        path = os.path.join(OUTPUT_DIR, name)
        if not os.path.exists(path):
            raise FileNotFoundError(f"스크린샷 없음: {path} (먼저 Playwright로 캡처 필요)")
        slide = prs.slides.add_slide(blank_layout)
        slide.shapes.add_picture(path, 0, 0, width=prs.slide_width, height=prs.slide_height)

    prs.save(PPTX_PATH)
    print(f"저장 완료: {PPTX_PATH} ({len(SLIDE_ORDER)}슬라이드)")


if __name__ == "__main__":
    main()
