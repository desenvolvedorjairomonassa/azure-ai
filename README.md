create .env file 
and included
- AI_SERVICE_ENDPOINT=your_azure_ai_services_endpoint
- AI_SERVICE_KEY=your_azure_ai_services_key

Análise de texto 
----
Analise de sentimentos das Avaliações de um hotel

install 

pip install azure-ai-textanalytics==5.3.0

pip install python-dotenv

text-analysis.py

Extract text
----

read-text-py - extract text into a image

Question Answering (qna-app.py)
------
install

pip install azure-ai-language-questionanswering

including .env
- AI_SERVICE_ENDPOINT
- AI_SERVICE_KEY
- QA_PROJECT_NAME
- QA_DEPLOYMENT_NAME

conversional language model  - clock-client.py
---
install:
-pip install azure-ai-language-conversations

speech speech-to-text , text-to-speech
------
install:
- pip install azure-cognitiveservices-speech==1.30.0
- pip install playsound==1.3.0

environment to set
-SPEECH_KEY
-SPEECH_REGION

speaking-clock.py
