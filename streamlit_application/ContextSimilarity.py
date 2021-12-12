
import spacy_universal_sentence_encoder
import spacy
import pandas as pd
from operator import itemgetter

class ContextSimilarity:
    def __init__(self,use_nlp):
        self.use_nlp=use_nlp
        self.SimilarityScore=[]
        self.query=''

    def ContextSimilarity(self,query,contexts):
        '''
        This Function finds the context simiarty of Query and Contexts
        return: SImialrity score of each context with query
        '''
        #add doc1 to nlp1 object
        self.query=query
        doc_1 = self.use_nlp(query)
        for context in contexts:
          #compute sentence semantic similarity between quesiton and contexts using Universal Sentence Encoder
          doc_2=self.use_nlp(context)
          similarity_rate=doc_1.similarity(doc_2)
          self.SimilarityScore.append([context,similarity_rate])
        return self.SimilarityScore

    def SortSimilarity(self,by='desc'):
        '''
        This Function sorts the simiarty of Query and Contexts
        return: SImialrity score in required order
        '''
        if by=='desc':
            return sorted(self.SimilarityScore, key=itemgetter(1), reverse=True)
        else:
            return sorted(self.SimilarityScore, key=itemgetter(1))

    def TopNSimilarity(self,top_n=10):
        '''
        This Function Finds the TOpN similarites
        return: TopN requested scores
        '''
        return sorted(self.SimilarityScore, key=itemgetter(1), reverse=True)[:top_n]

    def ConvertToDf(self,values):
        '''
        This Function converts the context similarity list to dataframe
        '''
        FinalDf = pd.DataFrame(values,columns=['Context','Similarity'])
        return FinalDf

    def MergeDf(self,df1,df2):
        '''
        This Function merges list to get the wikipage
        return: Merged dataframe with Context, SImilarity score, Wiki page
        '''
        Final_Df = df1.merge(df2,left_index=True, right_index=True)
        Final_Df.drop(columns=['Wikipedia_Paragraphs'],inplace=True)
        Final_Df.reset_index(inplace=True)
        Final_Df.drop(columns=['index'],inplace=True)
        return Final_Df

    def TopNSimilarityDf(self,Df,top_n=10):
        '''
        This Function sorts the simiarty of provided dataframe
        return: Dataframw sorted based on score in required order
        '''
        return Df.sort_values(by=['Similarity'], ascending=False).iloc[:top_n,]
