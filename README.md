# All in One Configuration

`nvm`, `yarn`, `pnpm` 같은 패키지 매니저부터 `golang`, `python`, `java` 등의 프로그램까지 원하는 프로그램을 명령 한두번으로 설정할 수 있도록 만들기 위해 만든 프로그램입니다.

명령은 다음과 같이 구성됩니다.

- `one help`: 프로그램 명령을 보여줍니다.
- `one install <app>`: `<app>`을 설치합니다.
- `one install <app> <command>`: `<app>`에서 `<command>`를 실행합니다.

## 작업 현황

- [ ] git hook 설정
  - [ ] 매 커밋 전, `requirements.txt` 재설정 되도록 설정하기
- [x] 운영체게 구분 모듈
- [ ] 괸리자 권한
  - [ ] 운영체제별 관리자 권한 감지 코드
  - [ ] 운영체제별 관리자 권한 요청 코드
- [ ] 설치 기능 구현
  - [ ] `nvm` (진행 중)
  - [ ] `yarn`
  - [ ] `pnpm`
  - [ ] `turborepo`
  - [ ] `travisci`
  - [ ] `circleci`
  - [ ] `git`
  - [ ] `gh`
  - [ ] `vscode`
