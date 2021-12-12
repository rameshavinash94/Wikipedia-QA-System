
import spacy
import pandas as pd
import spacy_universal_sentence_encoder
from ContextExtraction import ContextExtraction
from DocumentRetrival import DocumentRetrival
from DataWrangling import DataWrangler
from ContextSimilarity import ContextSimilarity
from MLModel import MLModel

if __name__ == "__main__":
  #load  spacy english language module(large)
  nlp = spacy.load('en_core_web_lg')

  # Load Universal Sentence Encoder and later find context similarity for ranking paragraphs
  use_nlp = spacy_universal_sentence_encoder.load_model('en_use_lg')

  #create a Document retrival object
  doc_retrive_obj = DocumentRetrival(nlp)

  #call UserInput func to get query input
  query = doc_retrive_obj.UserInput()

  #call preprocess func to preprocess query if required
  doc_retrive_obj.PreprocessUserInput()

  #call Retrive func with required top_n docs for retrival from Wiki
  pages = doc_retrive_obj.Retrive(2)

  #create a Extraction retrival object
  context_extract_obj = ContextExtraction(nlp)

  # Create a spacy matcher for the user query to parse the pages
  context_extract_obj.AddPhraseMatcher(query)

  # extract necessary context
  context_extract_obj.RetriveMatch(pages)

  # convert to pandas df
  text = context_extract_obj.StoreFindingAsDf()

  # store_results in csv for further reference
  text.to_csv("Matching_Wiki_contexts.csv")

  #create a Data Wrangler object
  data_wrangler_obj = DataWrangler(nlp)

  #cleaned Dataframe
  cleaned_df = data_wrangler_obj.DataWranglerDf(text)

  # store_results in csv for further reference
  cleaned_df.to_csv("Cleaned_Wiki_contexts.csv")

  #create a Context Similarity object
  context_similarity_obj = ContextSimilarity(use_nlp)

  #find the Similarites of Different context
  con_list = context_similarity_obj.ContextSimilarity(query,cleaned_df['Wikipedia_Paragraphs'])

  context_similarity_df = context_similarity_obj.ConvertToDf(con_list)

  Merged_Df = context_similarity_obj.MergeDf(context_similarity_df,cleaned_df)

  #retreive top N rows from dataframe
  TopNDf = context_similarity_obj.TopNSimilarityDf(Merged_Df)

  #create a ML Model object
  ML_Model_obj = MLModel()

  #call the Roberta model
  roberta_finding = ML_Model_obj.RobertaModel(TopNDf,query)

  #final Df post model prediction
  Final_DF = ML_Model_obj.ConverttoDf()

  #filtering only top N out of it.
  Results = ML_Model_obj.TopNDf(Final_DF)
  Results.to_csv("Final_results.csv")