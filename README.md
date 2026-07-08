# HajaCheck 착수보고서 — 리포트 산출물 레포

착수보고서 pptx 제작과 관련된 모든 문서·소스·산출물을 모아두는 레포입니다. 실제 작업(HajaCheck 메인 개발 레포와 분리)은 여기서 진행합니다.

## 구조

```
data/
  hajaCheck_착수보고_역할분담.md      담당자별 진행 체크리스트 (완료 항목은 지우는 방식으로 운영)
  hajaCheck_착수보고_슬라이드_가이드.md  슬라이드별 상세 작성 가이드 (PRD 기준, 담당자별 섹션)
  PRD_hajaCheck_v0.41.md            제품 요구사항 정의서 (원본 기준 문서)
  hajaCheck착수 보고.pptx            공용 원본 pptx (미리캔버스에서 실제 편집 중인 파일과 동기화)
html/            김관영 담당 슬라이드 HTML+CSS 원본 (1920x1080 고정 캔버스) — HTML→PPTX 임시 빌드용
  base.css       공통 스타일(색상 변수, 카드, 배지, 헤더/푸터)
  slide-01-cover.html      표지
  slide-02-toc.html        목차(브랜딩만 김관영 담당분)
  slide-03-intro.html      01 프로젝트 소개
  slide-05-plan.html       03 수행 계획
  slide-08-wrapup.html     06 검증 및 마무리
  slide-09-mockup.html     (신규) 화면설계 목업
  slide-10-ia-tree.html    (신규) IA 트리
output/          렌더링된 PNG + 최종 pptx (kimkwanyoung_임시.pptx)
build.py         PPTX 조립 및 공용 PPTX 병합 스크립트
capture.py       Playwright 기반 HTML 자동 캡처 스크립트 (Retina 고해상도 지원)
build_all.py     통합 빌드 파이프라인 (캡처 + PPTX 조립/병합 일괄 처리)
```

## 재빌드 및 병합 절차 (html/ 내용 수정 후)

1. `html/slide-*.html` 수정
2. 통합 빌드 실행: `python build_all.py`
   - 이 명령어 하나로 Playwright가 HTML 파일을 1920x1080 고해상도(Retina Scale)로 자동 캡처하여 `output/*.png`로 저장합니다.
   - 캡처가 끝나면 `output/kimkwanyoung_임시.pptx`와 공용 PPTX 원안을 병합한 `output/hajaCheck착수보고_최종.pptx`를 일괄 생성합니다.
   - *참고: 처음 실행하는 환경이라면 `playwright install chromium`을 먼저 수행해야 캡처가 가능할 수 있습니다.*

## 참고

- html/ 폴더는 김관영 담당 슬라이드의 HTML→PPTX 임시 빌드본입니다. `build_all.py`를 실행하면 유병현 담당 슬라이드가 유지된 채 김관영 담당본만 덮어씌워진 `output/hajaCheck착수보고_최종.pptx`가 자동으로 합성되므로 수동 병합이 불필요합니다.
- `data/hajaCheck착수 보고.pptx`는 미리캔버스(miricanvas.com)에서 실제 편집 중인 공용 원본의 로컬 사본입니다. 미리캔버스에서 편집한 뒤에는 이 파일도 다운로드해 갱신·커밋해주세요.

