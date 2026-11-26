# 학습과 인수인계 방법

각 단계에서 에이전트가 전부 작성하더라도 사용자가 설명·검증할 수 있어야 한다. 아래 다섯 항목을 단계 기록에 남긴다.

1. 개념: 기존 방식과 도입 도구의 차이, 해결하려는 업무 문제.
2. 데이터 흐름: 입력 → AI/규칙/도구 → 출력 → 검증 → 실패/승인. 각 단계의 실제 코드·API를 연결해 설명한다.
3. 실습: 사용자가 직접 한 번 재현하는 명령/UI와 예상 결과. 실제 환경 값은 확인 후 넣는다.
4. 역질문: "도구가 다운되면?", "권한 없는 입력이면?", "데이터가 바뀌면?"에 설명 가능한지 확인한다. 필요한 경우 사용자에게 작은 실습을 제안한다.
5. 성과: 검증 수치와 누적 운영 지표를 기록하고 포트폴리오에 공개할 수 있는지 구분한다.

에이전트는 긴 교과서 설명보다 구현과 검증을 우선한다. 단계가 끝나면 다음 에이전트가 바로 이어갈 수 있도록 현재 SHA, 실행 환경, 검증 결과, 미완료 조건, 다음 한 가지 행동을 기록한다. 작업 시점의 원본 비밀값·실제 사내 문서·로그 원문은 로드맵 저장소에 보존하지 않는다.

## 외부 공식 문서 진입점

- Langfuse: https://langfuse.com/docs ; self-host 규모: https://langfuse.com/self-hosting/configuration/scaling ; 운영 체크: https://langfuse.com/resources/engineering/self-hosted-langfuse-production-checklist
- Ragas: https://docs.ragas.io/
- Promptfoo: https://www.promptfoo.dev/docs/ ; 외부 전송 경계: https://www.promptfoo.dev/docs/red-team/troubleshooting/data-handling/
- MCP: https://modelcontextprotocol.io/
- Tool Calling: 사용 모델/런타임의 공식 function calling, JSON schema/structured output 문서 (Ollama 등).
- n8n: https://docs.n8n.io/
- LangGraph: https://docs.langchain.com/oss/python/langgraph/overview
- LiteLLM: https://docs.litellm.ai/
- vLLM: https://docs.vllm.ai/
- pgvector: https://github.com/pgvector/pgvector

도입 시 실제 버전의 문서를 다시 확인하고 버전·라이선스·설치 방법·특이 사항을 기록한다. 현재 링크의 내용이 영구 불변이라고 가정하지 않는다.


## V2 학습 검증 강화
단계별 이해 확인: 개념 설명, 실제 입력→출력 코드, 핵심 설정 직접 변경, 실패 재현/디버깅, 전후 비교, 보안·복구, 기술 선택 근거. 사용자 설명이나 직접 재현이 확인되지 않으면 미확인으로 남긴다. 학습/격리 구현/실제 운영/누적 성과를 구분한다. 새로운 기술의 첫 실습은 빠르게 하되 운영 채택은 필요한 경우에만. 취업 준비는 단기부터 `docs/06-employment-readiness.md`로 평가한다.
