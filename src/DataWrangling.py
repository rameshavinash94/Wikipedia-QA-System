import spacy
import pandas
import re
class DataWrangler:
    def __init__(self, nlp):
         self.nlp=nlp

    def DataWranglerDf(self,df):
        '''
        This functions cleans the provided Dataframe
        :return: Cleaned Dataframe (removed_sp_char_Df)
        '''
        removed_sp_char_Df = df
        removed_sp_char_Df['Wikipedia_Paragraphs'] = [re.sub(r"[^a-zA-Z0-9]+", ' ', doc) for doc in df['Wikipedia_Paragraphs']]
        #removed_sp_char_Df = removed_sp_char_Df[removed_sp_char_Df['Wikipedia_Paragraphs'].apply(len) > 2*len(query)]
        return removed_sp_char_Df

    def lemmatization(self,corpus):
        '''
        This Function removes stop words and lemmatizes the provided corpus
        :return: Stop word removed & Canonical form corpus (canonical)
        '''
        canonical=[]
        for x in corpus:
            temp=[]
            for token in self.nlp(x):
                if not token.is_stop:
                    temp.append(token.lemma_)

            canonical.append(" ".join(temp))

        return canonical