# AX-15 — Redis·비동기 큐·서비스 복원력
목표: AI 요청이 몰리거나 모델이 실패해도 기존 서비스를 보호한다. https://redis.io/docs/latest/.
## 실행
1. 기존 RAG 생성 동시성·timeout·취소·스케줄 확인. 합성 부하 기준값을 기록. Redis cache와 queue/worker 역할, TTL, idempotency, backpressure, retry/backoff, DLQ, circuit breaker 개념을 설명한다.
2. 별도 Redis와 테스트 API에 제한된 요청 큐 또는 중복 방지 키를 구현. 동일 요청의 중복 처리 방지, 과부하 429/503, timeout과 cancellation, 제한된 재시도, 워커 재시작 복구. 캐시가 필요한 경우 사용자/문서 버전으로 격리하고 민감 응답 캐시 금지 기본.
3. 승인된 합성 동시 요청, 모델/Redis 중단·복구, 중복, 요청 취소, 재시도 폭주 시험. 처리량·p95·queue depth·성공/실패/중복 수와 자원 측정. 기존 단일 사용자 환경에 Redis를 무조건 설치하지 않는다.
## 완료
- [ ] 실제 Redis/worker 실습 및 실패/중복/과부하 검증
- [ ] 기존 방식 대비 지표와 채택/보류 사유
