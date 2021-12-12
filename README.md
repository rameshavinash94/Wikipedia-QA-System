# NLP QA System for Wikipedia 

Wiki QA Web Applicaiton that dynamically locates wikipedia sources and applies NLP to answer user questions. A QA system will assist in quickly locating information.

**Deployment URL:** _https://cmpe256-q4uake3apq-uc.a.run.app_

# Project Overview
Question Answering (QA) system is a computer applicaiton that responds to inquiries in natural languages such as English.
For instance, a user might inquire, “Who is Mark Zuckerberg?” In this situation, the Q&A system should respond with "Facebook Founder or CEO of Facebook".

A QA system can be open domain or domain-specific. Based on wiki pages, we created a real-time open domain question answering system.

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
