# AX-03 — Promptfoo: AI 품질·보안 회귀 시험

대상: RAG HTTP API의 격리 환경. Langfuse 추적과 Ragas 기준을 재사용하되 역할은 구분한다.

## 실행
1. 고정 버전 및 라이선스, Node 호환성, provider/HTTP adapter/데이터 처리 문서 확인. 제품 의존성과 별도 디렉터리/잠금. 합성 데이터로만 시작한다.
2. 공식 [데이터 처리](https://www.promptfoo.dev/docs/red-team/troubleshooting/data-handling/) 및 FAQ 확인. 원격 공격 생성/채점, telemetry, 공유, 업데이트 경로를 비활성화하는 현재 버전의 설정을 검증한다. 문서 예시: `PROMPTFOO_DISABLE_REMOTE_GENERATION=true`, `PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=true`, `PROMPTFOO_DISABLE_TELEMETRY=1`, `PROMPTFOO_DISABLE_SHARING=1`, `PROMPTFOO_DISABLE_UPDATE=1`. 설정만으로 네트워크 격리를 보장하지 않으므로 실제 egress 차단/검사를 수행한다. 원격 전용 플러그인 금지. 클라우드 기본값/API 키 자동 감지 주의.
3. 고정된 합성 테스트로 평가: 정상 답변/출처/근거 없는 질문/문서 내 지시 무시/시점 충돌/허용되지 않은 문서 경로·프로젝트 요청/출력 형식/오류·타임아웃. 승인받은 격리 환경과 직접 작성한 공격 예제만 사용. 보안 정책은 모델 채점만이 아니라 서버 응답·권한·실제 부작용 기록으로 확인한다.
4. 취약한 합성 fixture로 실패가 실제 검출되는지 확인하고, 수정 후 동일 입력 재검증. 현재 단일 사용자 RAG는 다중 사용자 격리를 검증했다고 주장하지 않는다. 미구현 인증은 BLOCKED/NOT_APPLICABLE이 아니라 별도 보안 도입 조건으로 명시한다.
5. 로컬 반복 평가 명령과 리포트 생성, 비교 가능한 기준. 원문이 없는 결과 요약만 Git 기록. 기존 CI를 임의로 추가하지 않는다.

## 완료 기준
- [ ] 버전 고정 및 로컬 provider/평가 경로 확인, 외부 전송 없음 검증
- [ ] 고정 품질/보안 사례와 기대 동작 정의, 실패 fixture 검출
- [ ] 실제 대상 API 회귀 결과·실패·차단 이유 기록
- [ ] 재실행 명령과 변경 전후 비교 절차 문서화

지속 성과: 모델/프롬프트 변경 때 재검증, 보안 위반/품질 저하 건수 기록.
