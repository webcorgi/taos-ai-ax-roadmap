# AX-11 — LLM 기본기와 Python/FastAPI
목표: 이미 사용한 Ollama를 넘어 모델·토크나이저·API의 연결을 이해하고 AI 코드의 동작과 실패를 직접 설명한다. 공식 https://huggingface.co/learn/llm-course/ , https://fastapi.tiangolo.com/ , https://pytorch.org/docs/stable/ 참조.
## 실행
1. 기존 RAG Python 3.12 / FastAPI / httpx / Pydantic / pytest 구조를 읽고, 별도 가상환경에서 typing, venv/lock, async/await, 예외, HTTP/JSON, SSE 스트리밍·취소를 직접 재현한다. 기존 제품 의존성 변경 금지.
2. 토큰화, embedding, Transformer attention, context window, autoregressive decoding, temperature/top-p, quantization의 개념을 짧게 설명하고 동일 한글·영문 입력의 토큰 수/문맥 절단 및 생성 설정 차이를 비교한다. 작은 승인 오픈 모델/토크나이저를 Hugging Face Transformers로 직접 로딩하고 모델 태그·리비전·라이선스를 기록한다. 대규모 학습이나 GPU 구매 금지.
3. 로컬 LLM을 호출하는 최소 FastAPI endpoint를 독립 구현한다. Pydantic 검증, 타임아웃, 취소, 오류 처리, 실제 호출/모의 호출 pytest를 작성한다. 상용 API는 승인된 합성 데이터로만 별도 비교; 키/비용 승인 전 외부 전송 금지.
4. 사용자에게 핵심 코드 1개를 수정하게 하거나 직접 설명하게 하고 실패를 재현한다. 모델 변경/잘못된 출력/응답 지연에 대한 원인 분석을 기록한다.
## 완료
- [ ] 작은 모델/토크나이저 직접 실행과 비교 기록
- [ ] Python API 정상·오류·타임아웃·취소 테스트와 코드 설명
- [ ] 독립적으로 데이터 흐름과 모델/API 선택 근거를 설명 가능. 미확인 사용자 이해는 별도 표시.
