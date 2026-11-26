# AX-16 — 클라우드·CI/CD·컨테이너 운영
목표: AI 서비스를 실제 배포하고 문제 발생 시 진단·복구할 수 있다. 기존 Docker/Nginx/CI 경험 활용. AWS/GCP/Azure 중 목표 기업과 접근 가능한 1개; 유료 자원은 명시적 승인·예산 상한 전 생성 금지.
## 실행
1. 독립 합성 FastAPI/Agent를 Docker 이미지로 빌드, 비밀값 미포함·이미지 취약점 점검·버전 고정. IaC(Terraform/OpenTofu 등) 최소 설정, private network/IAM/TLS/secret/backup의 개념·실제 설정 확인.
2. 승인된 클라우드 테스트 계정 또는 로컬 VM으로 격리 배포. 클라우드 접근 불가면 로컬 실습 성과와 클라우드 미실행 분리. K8s 기본 Deployment/Service/readiness/liveness/limits/rolling update를 로컬 kind/minikube 등 승인 환경에서 시험; 운영 K8s 강제 금지.
3. CI 테스트 → 이미지 → 배포 → health/trace 확인 → rollback 재현. 기존 GitHub Actions를 추가 실행하지 않는다. 부하/실패/자원 부족/secret 누락/재시작 시험; SLO 예시·p95·오류율·알림/복구 시간을 기록. 테스트 자원 정리와 비용 확인.
## 완료
- [ ] 격리 배포·복구·실패 테스트, 클라우드 실제 수행 범위 명시
- [ ] 최소 IAM/네트워크·비밀·운영 관측·비용 통제 증빙
