# NLP Chat Bot for Wikipedia 

NLP Chat Bot that dynamically locates wikipedia sources and applies NLP to answer questions

**Deployment URL:** _https://cmpe256-q4uake3apq-uc.a.run.app_

# Project Overview
- Chat Bot wrapper
- Wikipedia content locator
- NLP question answering

# Project Architecture Diagram
![](https://github.com/coryroyce/wiki_based_nlp_chat_bot/blob/main/reference/High_Level_Architecture.png)

# Deployment Diagram
![](https://github.com/coryroyce/wiki_based_nlp_chat_bot/blob/main/reference/Deploymnet_Diagram.png)
# Project Modules

- Application.py : Main Application
- DocumentRetrival.py : Retrieving Wiki pages based on user query.
- ContextExtraction.py : Extract only the Necessary Paragraphs from the Wiki pages.
- DataWrangling.py : Perform Data Wrangling tasks.
- ContextSimilarity.py : Perform Context Similarity using google universal sentence encoder and retrieve only topN out of it.
- MLModel.py : Pass the TopN similarities from ContextSimilarity to Roberta model and select only topN predictions that matches user query.
- Finally ML model Predictions are captured along with context/wiki page.
