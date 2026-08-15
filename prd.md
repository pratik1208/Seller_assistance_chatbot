## Business problem
Create a seller facing chatbot which can take product listings from seller and that chatbot should validae teh listings, it chould check policy compliance and content enrichment by by natural language

## Main use cases
1. Listing creation (seller can create new product listing)
2. Check whether the listing has all required information.
3. Check marketplace policies.
4. Conversational corrections


## Conversation flow
Bot can ask user  about listing and user will provide information about the listing and if bot find anything is missing he should ask immidiately. if he find issues less than 3 then he will ask to update but issues are more than 3 then he will say to update the listing

## Knowledge Resource

## Architecture 
User → API → Intent/Router → Agent → Tools → LLM → Response

## Memory
Langgraph/Langchain - Short term memory

Postgres - Longterm Memory


## Tools
category_rules
prohibitted_items

## Safety and Validation

1. Input Validation
2. Tool permission checks
3. hallucination control
4. Human Escallation

## Evaluation
1. Answer accuracy
2. Tool call accuracy
3. Latency
4. Cost

## LLM
OpenAI

## Embedding model
Not Needed

## VectorDB
ChromaDB

## Agent Framework
Langchain


## Backend 
Django

## cache
Redis

## Observability
Langsmith

