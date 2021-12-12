from spacy.matcher import PhraseMatcher
import pandas as pd

class ContextExtraction:
    def __init__(self, nlp):
        self.nlp=nlp
        self.phrase_matcher = PhraseMatcher(nlp.vocab)
        self.findings=[]

    def AddPhraseMatcher(self,search_text):
        '''
        This Function Creates a Spacy Phrase Matcher based on User Query
        '''
        phrases = [x for x in search_text.split()]
        patterns = [self.nlp(text) for text in phrases]
        Upper_Case = [self.nlp(text.upper()) for text in phrases]
        Capitalize = [self.nlp(text.capitalize()) for text in phrases]
        Lower = [self.nlp(text.lower()) for text in phrases]
        self.phrase_matcher.add('Matches', None, *patterns)
        self.phrase_matcher.add('Upper_Case', None, *Upper_Case)
        self.phrase_matcher.add('Capitalize', None, *Capitalize)
        self.phrase_matcher.add('Lower', None, *Lower)

    def paragraphs(self,document):
        '''
        This Function yields the paragraphs of the matched sentences
        '''
        start = 0
        for token in document:
            if token.is_space and token.text.count("\n") > 1:
                yield document[start:token.i]
                start = token.i
        yield document[start:]

    def RetriveMatch(self,search_results_pages):
        '''
        This Function retrieves the required Matches for all the Pages from the created Matcher
        :return: list of Findings (self.findings)
        '''
        temp=[]
        for x in search_results_pages:
            for y in self.paragraphs(self.nlp(x.content)):
                b=self.nlp(y.text)
                for match_id, start, end in self.phrase_matcher(b):
                    if self.nlp.vocab.strings[match_id] in ["Matches","Upper_Case","Capitalize","Lower"]:
                        if b.text not in temp:
                            self.findings.append([x,b.text])
                            temp.append(b.text)

        return self.findings

    def StoreFindingAsDf(self):
        '''
        This Function store the context finding in a pandas dataframe
        :return: Pandas Dataframe of Findings (findingsdf)
        '''
        findingsdf = pd.DataFrame(self.findings,columns=['Wiki_Page','Wikipedia_Paragraphs'])
        return findingsdf