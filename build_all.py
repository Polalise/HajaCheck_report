"""통합 빌드 파이프라인 스크립트.
Jinja2 템플릿 컴파일 ➡️ HTML 캡처(Playwright) ➡️ PPTX 조립/병합을 한 번에 수행합니다.
"""
import sys
from compile_templates import compile_all
from capture import capture_all
from build import build_individual, build_merged


def main():
    print("=== [1/3] HTML 템플릿 컴파일 시작 (Jinja2) ===")
    try:
        if not compile_all():
            print("템플릿 컴파일에 실패했습니다.", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"템플릿 컴파일 중 치명적인 에러 발생: {e}", file=sys.stderr)
        sys.exit(1)

    print("\n=== [2/3] HTML 슬라이드 캡처 시작 (Playwright) ===")
    try:
        capture_all()
    except Exception as e:
        print(f"캡처 단계 에러 발생: {e}", file=sys.stderr)
        print("Playwright가 제대로 설치되었는지 확인해 주세요.", file=sys.stderr)
        sys.exit(1)

    print("\n=== [3/3] PPTX 슬라이드 빌드 및 병합 시작 ===")
    try:
        success_ind = build_individual()
        if success_ind:
            build_merged()
            print("\n모든 작업이 성공적으로 완수되었습니다!")
        else:
            print("\n임시 PPTX 조립에 실패했습니다.", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"PPTX 빌드 단계 에러 발생: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
