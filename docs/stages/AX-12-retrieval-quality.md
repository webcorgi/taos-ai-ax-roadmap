# AX-12 — 임베딩·하이브리드 검색·Reranker
기존 Qdrant/E5/BM25 계열 하이브리드 검색을 실제 코드 확인 후 활용한다. https://sbert.net/ , https://qdrant.tech/documentation/.
## 실행
1. 벡터·차원·정규화·cosine similarity, dense/sparse, top-k, chunking, query expansion, cross-encoder 재정렬을 합성 문서로 이해하고 수동 계산과 코드 결과를 대조한다.
2. 기존 검색 기준(21/25=84%)을 보존하고 AX-02 독립 데이터셋/동일 문서 스냅샷에서 dense, hybrid, hybrid+reranker를 비교한다. 조정용과 held-out을 분리. 후보 재정렬기는 CPU/메모리 제약을 확인하고 버전 고정한다.
3. Recall@5/MRR/검색 p50·p95/생성 품질/권한 필터/출처 보존/비용·자원 비교, 실패 사례 분석. 성능·품질 개선이 없으면 현행 유지. 신규 배포는 별도 승인.
## 완료
- [ ] 최소 재정렬 실험, 동일 평가셋 결과 및 분모 기록
- [ ] 데이터 분할/임베딩/검색/재정렬 역할·실패 사례 설명
- [ ] 변경 여부와 회귀·롤백 근거 기록
