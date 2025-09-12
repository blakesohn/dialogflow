# Official Blog

https://cloud.google.com/blog/topics/developers-practitioners/how-to-build-dynamic-web-experiences-with-conversational-agents?e=48754805

# How to Setup Dynamic Web Experience

## Import the sample conversational agent

- agent 하위에 있는 blob 파일을 이용해 해당 프로젝트 내에 conversational agent 로 import 하여 sample agent 를 만든다.

## Configuration for the chat UI

1.  Copy `config.js.template` to `config.js`:
    ```bash
    cp config.js.template config.js
    ```
2.  import 하여 만든 agent 의 정보를 이용하여 `config.js` 파일 수정한다.

## How to demo?

- local 환경에서 `dynamic_page_v1.html` 파일을 열어 테스트 한다.
- Type `호텔 패키지 정보 좀 알려줘` to display hotel package page
- Type `여행자 마일리지 정책 확인해줘` to diaply krisflyer page
