# AX-18 — PEFT·LoRA·QLoRA 미세조정
목표: 모델을 바꾸는 것과 RAG/프롬프트/미세조정의 선택 이유를 설명한다. https://huggingface.co/docs/peft/ , https://huggingface.co/docs/transformers/.
## 실행
1. 합성 문의 유형 분류 또는 승인 비식별 데이터 소량을 준비. 학습·검증·고정 독립 테스트를 분리, 개인정보/라이선스 확인. base model + prompting/few-shot 기준 측정.
2. 작은 호환 모델에 PEFT LoRA 학습과 어댑터 저장/로드, 파라미터 수·trainable 비율·메모리 비교. QLoRA는 양자화 가중치+LoRA 원리를 이해하고 지원 하드웨어/라이브러리 환경에서 실제 최소 실습. 불가하면 QLoRA 실측 미완료 및 대체 환경/차단 사유 기록; LoRA를 QLoRA로 둔갑 금지.
3. 동일 고정 평가셋 accuracy/macro F1/실패/지연/자원 비교. 개선 없으면 prompting 유지. 모델/데이터 외부 업로드·실제 사내 자동 분류 도입은 별도 승인.
## 완료
- [ ] LoRA 실제 실험과 QLoRA 실습 범위·미확인 조건 명시(미실행 필수 항목은 BLOCKED)
- [ ] 고정 평가, 재현 가능한 어댑터/모델 버전·선택 근거
