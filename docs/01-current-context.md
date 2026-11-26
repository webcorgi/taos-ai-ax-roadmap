# 기존 업무 환경과 검증 근거

기준일 2026-11-26. 아래는 Git에서 확인한 과거 구현·검증 기록이다. 현재 서비스 실행 여부나 실제 운영 성과를 이 자료만으로 단정하지 않는다. 새 에이전트는 현재 브랜치와 실환경을 재확인한다.

## 대상 저장소

| 저장소 | 역할 | 기본 브랜치 (확인 당시) |
|---|---|---|
| [TAOS RAG](https://github.com/taosdevelopments/RAG) | Python/FastAPI, Qdrant, 로컬 Ollama, 문서 검색·생성 | main |
| [TAOS 공식 홈페이지](https://github.com/taosdevelopments/taos.kr) | Dify/Ollama 번역, Sentry 오류 자동화, PostHog | master |
| [ESS](https://github.com/taosdevelopments/ess.taos.kr) | BMAD/ECC, 관제·검증·모의 AI 이상 탐지 | master |
| [EV-CARE API](https://github.com/taosdevelopments/evcare-nestjs-msa) | 차량·BMS 통계 등 업무 API 후보 | main |
| [포트폴리오](https://github.com/webcorgi/k.corg.app) | 사용자 역량·검증된 AX 사례 공개용 | master |

## RAG 구현과 제약 (첫 도입 대상)

- Python 3.12, FastAPI, Qdrant, SQLite, multilingual-E5-small, Qwen3 4B Instruct Q4_K_M, Ollama, Docker Compose 독립 프로젝트. 기존 Dify와 볼륨·DB·설정 분리.
- 과거 검증 환경은 CPU 중심, API 2CPU/2GiB, Ollama 4CPU/8GiB 제한, 기본 생성 동시성 1. 현재 서버 여유 자원과 GPU는 미확인.
- 기본 질문 화면은 localhost `127.0.0.1:8765` (신뢰된 단일 사용자 범위). 외부·다중 사용자 권한은 별도 구현 필요.
- `scripts/maintenance.sh` 및 `scripts/schedule_maintenance.py`: 기존 03:00 KST 배치. API 일시 중지 후 색인/백업 및 재시작. 신규 평가·추적 작업은 이 배치와 충돌하지 않도록 설계한다.
- 기존 설계 기준 `core_make.md` 변경 금지(명시 요청 제외). 기존 `taos_make.md`의 단계 0~8과 AX 단계 번호를 혼동하지 않는다. 기존 미완료 단계 7/8은 따로 유지한다.
- 주요 파일: `AGENTS.md`, `README.md`, `pyproject.toml`, `requirements.lock`, `compose.yaml`, `src/rag/api.py`, `src/rag/settings.py`, `src/rag/middleware.py`, `src/rag/generation/{service,lifecycle,policy,protocol,prompt}.py`, `src/rag/retrieval/{service,context,store}.py`, `scripts/evaluate_search.py`, `scripts/evaluate_answers.py`, `evals/questions.json`, `tests/`, `docs/operations.md`.

| 역사적 측정 | 값 | 의미 |
|---|---|---|
| 승인 문서·검색 데이터 | 443개·12,437 벡터 | 2026-11-05 당시 규모 |
| 분류별 검색·원문 연결 | 19/19 범위 | 분류와 원문 해시 확인, 답변 정확도 아님 |
| 고정 근거 검색 | 21/25 (84%) | 확장 문서 기준 Top-5 포함, 기존 90% 목표 미달 |
| 사후 동등 근거 포함 평가 | 25/25 | 독립 평가 아님. 기존 지표 대체 금지 |
| 대표 답변 핵심 동작 | 9/9 | 생성 7, 현재 상태 질문 보류 2. 전체 정확도 아님 |
| 정기 배치 | 벡터 12,437 재사용, 수집 실패 0 | 2026-11-05 03:00 실행 기록 |
| CPU 생성 지연 | 첫 모델 출력 중앙값 66.34초(7건), 전체 중앙값 70.22초(9건) | 서버 내부 첫 출력과 HTTP 첫 바이트는 다름. 최신 재측정 필요 |

근거: [RAG 생성 검증](https://github.com/taosdevelopments/RAG/commit/297f65fea), [문서 확장 검증](https://github.com/taosdevelopments/RAG/commit/f2194a7dd), [운영 가이드](https://github.com/taosdevelopments/RAG/blob/main/docs/operations.md).

## 다른 사내 시스템

- 홈페이지 번역: Dify Workflow + Ollama, 한국어 원문 → 다국어 생성 → 관리자 입력 필드. 2026-04-02 도입, 2026-09-09 러시아어 기존 콘텐츠 86건 확장. 실제 의미 정확도/사용량 추가 측정 필요. [도입](https://github.com/taosdevelopments/taos.kr/commit/8dec06a53), [확장](https://github.com/taosdevelopments/taos.kr/commit/9bbe5ef35).
- Sentry 오류 대응: Webhook → 큐 → PM2/Codex CLI → 테스트·빌드 → Notion → Git·Woodpecker 배포 확인 → Resolve → 감사. 2026-11-20 당시 기존 이슈 10건 보고·상태 확인, 테스트 89개 통과. 기존 운영 규칙 보존. **문의 폼·GAS·시트·텔레그램 변경 및 테스트 제출 금지**가 명시되어 있으므로 n8n 첫 업무로 고객 문의를 선택하지 않는다. [구축](https://github.com/taosdevelopments/taos.kr/commit/a3e423b56), [검증 강제](https://github.com/taosdevelopments/taos.kr/commit/4cde5cd4f).
- ESS: BMAD Epic/Story를 현행 상태 기준으로 사용, ECC는 선택 스킬과 독립 리뷰에 사용. P단계/AEP 호환 실행 경로는 폐기됨. 운영 DB·실로봇·119 및 현장 AI 안전 승인은 별도다. [ECC/BMAD](https://github.com/taosdevelopments/ess.taos.kr/commit/955b11836), [로컬 통합 검증](https://github.com/taosdevelopments/ess.taos.kr/commit/eea73da2b).
- 새 도구의 실제 사용 경험 여부는 현재 저장소·실행 환경에서 확인. 이미 있는 도구라면 중복 설치하지 말고 실제 사용 범위·검증 근거를 보완한다.
