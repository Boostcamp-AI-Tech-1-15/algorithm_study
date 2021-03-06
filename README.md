# Algorithm Study



## TOC

- [팀원](https://github.com/Boostcamp-AI-Tech-1-15/algorithm_study#-%ED%8C%80%EC%9B%90)
- [스터디 방법](https://github.com/Boostcamp-AI-Tech-1-15/algorithm_study#%EF%B8%8F-%EC%8A%A4%ED%84%B0%EB%94%94-%EB%B0%A9%EB%B2%95)
- [Schedule](https://github.com/Boostcamp-AI-Tech-1-15/algorithm_study#-schedule)
- [컨벤션 및 규칙](https://github.com/Boostcamp-AI-Tech-1-15/algorithm_study#-%EC%BB%A8%EB%B2%A4%EC%85%98-%EB%B0%8F-%EA%B7%9C%EC%B9%99)

---

## 👋 팀원

|김다영|김아경|문하겸|박지민|이요한|전준영| 정민지|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [![Avatar](https://avatars.githubusercontent.com/u/68893924?v=4)](https://github.com/keemdy) |[![Avatar](https://avatars.githubusercontent.com/u/70522267?v=4)](https://github.com/EP000)| [![Avatar](https://avatars.githubusercontent.com/u/44228269?v=4)](https://github.com/ddobokki) | [![Avatar](https://avatars.githubusercontent.com/u/82632580?v=4)](https://github.com/ddeokbboki-good) | [![Avatar](https://avatars.githubusercontent.com/u/49181231?v=4)](https://github.com/l-yohai) | [![Avatar](https://avatars.githubusercontent.com/u/50571795?v=4)](https://github.com/20180707jun) | [![Avatar](https://avatars.githubusercontent.com/u/45448731?v=4)](https://github.com/minji-o-j) |

---

## 🙋‍♂️ 스터디 방법

- 여러 알고리즘 문제 플랫폼에서 문제를 선별(주에 3개)하여 문제풀이를 진행한다.
- 리뷰는 매주 월요일 피어세션마다 진행한다.
- 문제풀이를 진행하고, 본인계정으로 fork한 레포지토리에서 본 레포지토리로 Pull Request한다.
  - **월요일 피어세션 전까지 반드시 PR할 것!**
  - PR할 폴더구조: ./week_{}/문제이름/본인이름.py
- 코드리뷰가 끝난 후 모두의 Approve를 받았으면 Merge한다.
- Merge가 되었으면 충돌 해결을 위해 `git pull` 을 한 뒤 PR한 레포지토리에 다시 push 한다.

---

## 🗓 Schedule

| WEEK |                           PROBLEM                            |        DURATION         |   REVIEW DATE   |
| :--: | :---------------------------------------------------------- | :---------------------: | :-------------: |
|  01  | 1. [2020 카카오 인턴십 코딩테스트 - 경주로 건설](https://programmers.co.kr/learn/courses/30/lessons/67259) | 2021.08.06 ~ 2021.08.08 | 2021.08.09 (월) |
|  02  |1. [2019 KAKAO BLIND RECRUITMENT - 오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888)<br> 2. [월간 코드 챌린지 시즌1 - 풍선 터트리기](https://programmers.co.kr/learn/courses/30/lessons/68646)<br> 3. [2018 KAKAO BLIND RECRUITMENT - [1차] 셔틀버스](https://programmers.co.kr/learn/courses/30/lessons/17678)<br> +) [연습문제 - 하노이의 탑](https://programmers.co.kr/learn/courses/30/lessons/12946)| 2021.08.10 ~ 2021.08.15 | 2021.08.17 (화) |

---

## 🤙 컨벤션 및 규칙

### 💻 Code Conventions

- 코드마다 주석을 작성한다.
- 변수와 함수 이름은 역할에 대한 책임을 반영할 수 있는 이름으로 작성할 것.

### 📄 Commit Rules

- 커밋 메세지는 아래의 메세지 템플릿을 사용한다. ([깃에 커밋메세지 템플릿 적용하기](https://github.com/Boostcamp-AI-Tech-1-15/ddobokki_log/wiki/%EC%BD%94%EB%93%9C%EB%A6%AC%EB%B7%B0%EB%A5%BC-%EC%9C%84%ED%95%9C-%EA%B9%83-%EC%82%AC%EC%9A%A9-%EB%A7%A4%EB%89%B4%EC%96%BC#%EA%B7%B8-%EC%99%B8-%ED%8C%81%EB%93%A4))

  ```
  # <타입>: <제목>
  
  ##### 제목은 최대 50 글자까지만 입력 ############## -> |
  
  # 본문은 위에 작성
  ######## 본문은 한 줄에 최대 72 글자까지만 입력 ########################### -> |
  
  # 꼬릿말은 아래에 작성: ex) #이슈 번호
  ```

- <타입>은 전부 영어 소문자로 작성하며, <제목>은 한글 영문 모두 사용가능.

- 성의없는 커밋메세지는 지양하고, 작업 내용을 요약할 수 있는 커밋메세지를 지향한다.

  - 제목에는 문제이름 혹은 번호 등이 포함되어야 하며, 본문에는 자기가 사용한 핵심 로직 등을 간단하게 서술할 것.

  - 예시

    ```
    -- 예시 1
    
    # <타입>: <제목>
    feat: Week1 경주로 건설
    ##### 제목은 최대 50 글자까지만 입력 ############## -> |
    경주로 건설 문제를 dfs를 사용하여 해결하였습니다.
    시간복잡도 때문에 삽질을 했는데, 어떻게 하니까 풀렸습니다.
    # 본문은 위에 작성
    ######## 본문은 한 줄에 최대 72 글자까지만 입력 ########################### -> |
    # 꼬릿말은 아래에 작성: ex) #이슈 번호
    
    -- 예시 2
    
    # <타입>: <제목>
    style: typo 경주로 건설
    ##### 제목은 최대 50 글자까지만 입력 ############## -> |
    이전 커밋에 사용하지 않는 변수와 함수를 제거하였습니다.
    또한 다른거 뭘 잘못해서 타이포를 변경하였습니다.
    # 본문은 위에 작성
    ######## 본문은 한 줄에 최대 72 글자까지만 입력 ########################### -> |
    # 꼬릿말은 아래에 작성: ex) #이슈 번호
    ```

- 파일이 여러 개가 있을 때 무지성 `git add .` 는 지양하고, 파일 별 커밋으로 분리합니다. (대부분 하나씩만 있을 듯!)

  - ex) `git add README.md` , `git add 경주로건설_요한.py`

### 📝 PR & Review Convention

- PR 템플릿은 아래를 따른다.
  ```
  # 문제

  ## 해결방법 및 핵심로직

  ## 작성한 테스트케이스 (있을 경우만)

  ## 그 외 팁들 혹은 레퍼런스
  ```
- 리뷰는 꼼꼼하게! 성의없는 코멘트 X
- 칭찬에 익숙해집시다.
- 피드백을 남기기 전에 상대방의 기분을 상하게 할 수 있는 말인지 다시 한 번 생각해볼 것!
- 리뷰를 마치면 Approve를 하고, 마지막 Approve를 한 사람이 Merge 합니다.

