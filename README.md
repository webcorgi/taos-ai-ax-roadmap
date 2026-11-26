# TAOS AI·AX 역량 강화 / 실무 도입 로드맵

**기준일: 2026-11-26 (KST)** · 독립적인 비공개 Git 저장소용 인수인계 패키지

목표는 도구를 많이 설치하는 것이 아니라 **실제 사내 업무에 반복 적용되는 AI 시스템을 구축하고, 품질·보안·운영·업무 성과를 측정할 수 있는 AI·AX 엔지니어 역량**을 확보하는 것이다. 이미 작동하는 RAG·Dify 번역·Sentry 오류 대응·ESS 개발 체계를 활용하며 불필요한 재구축을 금지한다.

## 처음 보는 에이전트

1. `AGENTS.md` → `START_HERE.md` → `state/progress.json` → `docs/01-current-context.md` → `docs/02-roadmap.md` 순서로 읽는다.
2. `python scripts/check_progress.py`로 다음 단계와 상태를 확인한다. Python 3.10+ 외 추가 의존성 없음.
3. 현재 단계 문서 하나만 읽고 실제 대상 저장소와 환경을 확인한다. 진행 근거가 없으면 완료로 표시하지 않는다.
4. 사용자의 `next` 또는 명시적인 실행 지시에 맞춰 한 단계만 수행하고 결과를 기록한 뒤 멈춘다.

이 ZIP은 실행 지침·상태 관리·검증 양식이다. Langfuse 등 실제 도구 설치 코드나 운영 서버 변경은 포함하지 않았다. 초기 단계는 AX-00(읽기 전용 사전 점검)이다.

## 문서 지도

| 경로 | 용도 |
|---|---|
| `AGENTS.md` | 모든 에이전트가 지켜야 할 실행 계약 |
| `START_HERE.md` | 새 세션 시작·재개 방법 |
| `docs/01-current-context.md` | 검증된 기존 환경과 근거 |
| `docs/02-roadmap.md` | 단계 순서와 의존성 |
| `docs/03-security-and-operations.md` | 내부 정보 보호, 운영 승인, 롤백 |
| `docs/04-metrics-and-evidence.md` | 지속적인 AX 성과 측정 규칙 |
| `docs/05-learning-and-handoff.md` | 개념·실습·검증·포트폴리오 기록 |
| `docs/stages/` | 단계별 실제 도입 지침 및 완료 조건 |
| `state/progress.json` | 진행 상태의 유일한 기준 |
| `templates/` | 검증 보고·측정·ADR 양식 및 평가 데이터 예시 |
| `scripts/check_progress.py` | 상태 파일/단계 순서 검증 (실행·배포 기능 없음) |
| `records/` | 민감정보 제거한 단계 결과 기록 |

권장 저장소명: `taos-ai-ax-roadmap` (Private). 회사 업무 정보가 포함되어 있으므로 공개 Git에 올리지 않는다. 사용자가 생성한 독립 저장소에 압축을 풀어 저장한다. 기존 RAG/ESS/홈페이지 저장소에 이 패키지로 덮어쓰지 않는다.
