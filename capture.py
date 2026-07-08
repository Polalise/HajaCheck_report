import os
import glob
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(HERE, "html")
OUTPUT_DIR = os.path.join(HERE, "output")


def capture_all():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # html/ 디렉터리 밑에 존재하는 slide-*.html을 동적으로 검색
    html_pattern = os.path.join(HTML_DIR, "slide-*.html")
    html_files = glob.glob(html_pattern)

    if not html_files:
        print(f"경고: 캡처할 HTML 슬라이드 파일(slide-*.html)이 {HTML_DIR} 에 존재하지 않습니다.")
        return

    # 1. 파일명 번호 기준으로 순서 정렬
    html_files.sort()

    with sync_playwright() as p:
        print("Headless Chromium 브라우저를 실행하는 중...")
        browser = p.chromium.launch(headless=True)
        # 1920x1080 해상도를 고해상도(Scale factor=2)로 렌더링하도록 컨텍스트 생성
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2
        )
        page = context.new_page()

        for html_path in html_files:
            html_name = os.path.basename(html_path)
            # png 파일명은 html 확장자를 png로 단순히 변경
            png_name = html_name.rsplit(".", 1)[0] + ".png"
            png_path = os.path.join(OUTPUT_DIR, png_name)

            # 로컬 파일 절대 경로를 URI 포맷으로 변환
            file_url = Path(html_path).as_uri()
            print(f"렌더링 및 캡처 중: {html_name} -> {png_name}")
            
            page.goto(file_url)
            # 네트워크 활동이 끝날 때까지 대기
            page.wait_for_load_state("networkidle")
            # 폰트 로드 및 애니메이션 정지용 여유 대기시간 부여
            time.sleep(0.5)
            
            page.screenshot(path=png_path)
            print(f"저장 성공: {png_path}")
        
        browser.close()
    print("모든 HTML 슬라이드 캡처 프로세스가 완료되었습니다.")


if __name__ == "__main__":
    capture_all()
