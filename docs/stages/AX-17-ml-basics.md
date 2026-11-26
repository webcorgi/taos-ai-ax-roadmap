# AX-17 — ML·데이터·PyTorch 기본기
목표: 이미 실험한 ESS Isolation Forest의 원리와 데이터 평가를 이해하고 작은 예측 모델을 비교할 수 있다. https://scikit-learn.org/stable/ , https://pytorch.org/tutorials/ , https://numpy.org/doc/.
## 실행
1. 합성/승인 비식별 ESS 시계열 데이터만 사용. NumPy/Pandas로 데이터 타입, 결측, 정규화, 분포/상관, 특징 계산, 시간 분리 및 데이터 누출 방지. 실제 화재 레이블 부족은 명시한다.
2. scikit-learn의 단순 규칙/지속값/Isolation Forest/작은 회귀 모델을 최소 비교. 학습/검증/테스트 시간 순 분리, threshold 선택은 검증셋만 사용. 정답 라벨 있는 합성 평가에서 precision/recall/F1 및 혼동행렬, 미래값 예측은 MAE/RMSE. 이상 점수를 실제 화재 확률로 주장하지 않는다.
3. PyTorch로 작은 tensor, forward/loss/backward/optimizer, inference/no_grad, CPU/GPU 메모리 차이를 실습. 작은 모델을 동일 기준선과 비교. 학습 seed, 버전, 데이터 split, 실패, 과적합 확인.
## 완료
- [ ] 직접 ML/torch 실습 코드 및 재현, 기준선 대비 정량 비교
- [ ] 데이터 누출·오탐/미탐·과적합 설명
- [ ] ESS 현장 적용·실제 안전 정확도와 분리한 기록
