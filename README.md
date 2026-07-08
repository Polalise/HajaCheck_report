# 김관영 담당 슬라이드 — HTML→PPTX 임시 빌드

`hajaCheck착수 보고.pptx`(공용 원본)는 건드리지 않고, 김관영 담당 슬라이드만 별도로 임시 제작하는 작업 폴더입니다.

## 구조

```
kimkwanyoung-slides/
  html/            슬라이드별 HTML+CSS 원본 (1920x1080 고정 캔버스)
    base.css       공통 스타일(색상 변수, 카드, 배지, 헤더/푸터)
    slide-01-cover.html      표지
    slide-02-toc.html        목차(브랜딩만 김관영 담당분)
    slide-03-intro.html      01 프로젝트 소개
    slide-05-plan.html       03 수행 계획
    slide-08-wrapup.html     06 검증 및 마무리
    slide-09-mockup.html     (신규) 화면설계 목업
    slide-10-ia-tree.html    (신규) IA 트리
  output/          렌더링된 PNG + 최종 pptx (kimkwanyoung_임시.pptx)
  build.py         output/*.png → pptx 조립 스크립트
```

## 재빌드 절차 (내용 수정 후)

1. `html/slide-*.html` 수정
2. 로컬 서버 기동: `python -m http.server 8794` (html 폴더 안에서, `file://`는 브라우저에서 차단되어 반드시 HTTP 서버 경유)
3. Playwright로 각 슬라이드를 1920x1080 뷰포트에서 스크린샷 → `output/슬라이드이름.png`로 저장(같은 파일명으로 덮어쓰면 됨)
4. `python build.py` 실행 → `output/kimkwanyoung_임시.pptx` 갱신

## 참고

- 내용 근거는 `docs/hajaCheck_착수보고_슬라이드_가이드.md`(김관영 섹션)와 `docs/PRD_hajaCheck_v0.41.md`
- 최종적으로 공용 `hajaCheck착수 보고.pptx`에 반영할 때는 이 산출물을 참고해 유병현 슬라이드와 합치는 단계가 별도로 필요합니다(이 폴더는 병합 대상이 아니라 김관영 개인 작업용 임시본).
