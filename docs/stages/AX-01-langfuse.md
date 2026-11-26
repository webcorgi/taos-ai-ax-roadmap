# AX-01 — Langfuse: AI 운영 추적

업무 문제: 검색/생성 중 어디에서 지연·실패하는지, AI 요청별 모델·사용량·응답 상태가 어떻게 달라지는지 반복적으로 확인하기 어렵다.

대상: `taosdevelopments/RAG`. 기존 API/검색/생성 구조 및 SQLite/Qdrant/Ollama 보존. Dify 번역 연동은 RAG 검증 후 별도 범위 승인 시에만.

## 구현 순서
1. AX-00 자원 검증과 승인 확인. 공식 [self-hosting 규모](https://langfuse.com/self-hosting/configuration/scaling), [운영 체크](https://langfuse.com/resources/engineering/self-hosted-langfuse-production-checklist), SDK 버전 문서 확인. 현재 self-host 구성은 web/worker, PostgreSQL, ClickHouse, Redis/Valkey, object storage를 요구한다. 경량 서비스로 간주하지 않는다. 운영 서버 자원 부족이면 별도 승인 환경, 아니면 BLOCKED.
2. 별도 작업 디렉터리와 Compose 프로젝트에 공식 배포 예제를 검토해 버전 고정. 독립 볼륨/포트, localhost 또는 승인 사설망, 기본 계정 차단, 비밀값 생성, 저장·백업·보관 설정. Compose는 격리 실험 우선이며 운영 고가용성은 별도 판단. 다른 서비스 DB 공유 금지.
3. 합성 이벤트로 trace 등록 및 UI 확인. SDK/OTel의 자동 입력·출력 수집을 차단하고 전송 내용 실제 점검. SDK가 문자열을 자동 전송하면 코드에서 제외/마스킹한 후 재검증한다.
4. `src/rag/api.py`, `generation/service.py`, `retrieval/service.py`, middleware/lifecycle을 확인하고 최소 추적 경계 선정. trace → 검색 span → 근거 선택 span → 생성 span. 성공/실패/보류/취소 구분, 스트리밍 수명과 일치, 실제 가능한 토큰 수만 기록. RAG 기능/응답 스키마 변경 최소화.
5. 기능 flag 기본 off, SDK 키/endpoint는 env, 시간 제한·전송 실패 독립 처리. 기존 응답 반환을 관측 시스템 장애로 막지 않는다. background buffer는 제한하고 재시작 시 유실 여부 기록. 중복 trace와 외부 전송 차단 검사.
6. 승인된 합성/독립 샘플로 기존 테스트와 trace 대조. 성공, 보류, 오류, 취소, Langfuse 비가용, tracing off, 민감 문자열 입력 등 시나리오 실행. tracing 전후 동일 모델·데이터·설정으로 지연 비교. 기존 API 동작과 배치 유지.
7. UI에서 사용자가 trace 한 건을 직접 읽는 방법을 설명하고, 일별 요청량·오류율·p50/p95·토큰(실측만) 측정 방법 문서화. 기존 관측 기록과 Langfuse 측정 중복을 구분한다.

## 완료 기준
- [ ] 격리 Langfuse 기동/health/접근 제어 및 재시작 확인
- [ ] 실제 RAG 요청과 검색/생성 span 및 상태 일치 (정상·보류·오류·취소)
- [ ] 비밀/원문/질문·답변 미저장 및 허용된 내부 endpoint만 접근 확인
- [ ] 관측 off/실패에서도 기존 응답·취소·동시성 정상, 회귀 테스트 통과
- [ ] 전후 측정 수치와 플래그 기반 롤백, 운영 미적용 여부 기록

산출물: 대상 저장소의 테스트/추적 코드/의존성 잠금/설정 예시/운영 문서 및 로드맵 검증 보고. 운영 적용 승인 전에는 격리 결과만 기록한다. AX-02로 자동 진행하지 않는다.
