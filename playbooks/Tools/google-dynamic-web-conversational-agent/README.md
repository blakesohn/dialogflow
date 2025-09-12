# Building Dynamic Web Experiences with Conversational Agent

In today's digital landscape, creating engaging and personalized web experiences is crucial for effective user interaction. With the advancement of Large Language Models (LLMs) and conversational AI, we can now build websites that dynamically adapt their content based on user interactions through natural language conversations.

In this blog, you'll learn how to:
- Create dynamic web pages that respond to user intents using Google Conversational Agent
- Use function tools to bridge the gap between conversation and web pages

We will demonstrate a simulated use case where customer is chatting with a Conversational Agents chatbot. When the customer is asking about baggage or frequent flyer miles, the webpage will change according to the intent respectively.

## What is Conversation Agent Function Tool?

A Conversation Agent Function Tool is a powerful feature that allows your chatbot to interact with external systems and trigger actions based on user conversations. In this article, we use it to:

1. Detect user intents from natural language input
2. Map those intents to specific function tool
3. Dynamically update the UI based on the conversation flow


## Playbook Configuration

Set up a new Function tool in Playbook with the following input/output schemas.

```yaml
# Input
type: object
required:
  - intent
properties:
  intent:
    type: string
    description: Intent for web client rendering.

# Output
null
```

Setup example:

```text
Customer want to check about travel miles. For example, customer asks the following questions:
- How can I earn Cymbal miles besides just flying with Cymbal Airlines?
- What can I use my accumulated Cymbal miles for?
- What are some of the general benefits I get as a Cymbal member?
- Are there different membership levels, and what additional perks do higher tiers offer?
- Where can I use my Cymbal miles for flights?

```

The rest of the configuration as follows:
![config](example-miles.png)

## How to Setup Dynamic Web Experience

## Configuration

1.  Copy `config.js.template` to `config.js`:
    ```bash
    cp config.js.template config.js
    ```
2.  Open `config.js` and enter your configuration details.

## How to demo?

- Open `dynamic_page_v1.html`
- Type `호텔 패키지 정보 좀 알려줘` to display hotel package page
- Type `여행자 마일리지 정책 확인해줘` to diaply krisflyer page
