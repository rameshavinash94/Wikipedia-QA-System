import wikipedia
class DocumentRetrival:
    def __init__(self, nlp):
        self.nlp = nlp
        self.question = ''
        self.search_text = ''
        self.search_results_pages = []

    def UserInput(self,query=''):
        '''
        This Function is to get user query for document retrival
        '''
        if query=='':
          self.question=input("Enter the Query to Retrive Pages")
        else:
          self.question=query
        if not self.question:
            raise Exception('User input is empty')
        # add search_text
        self.search_text = self.question
        return self.search_text

    def PreprocessUserInput(self):
        '''
        This Function is to preprocess user input and extract only the nceesary POS prior passing user query document retrival
        '''
        try:
            doc1 = self.nlp(self.question)
        except Exception as e:
            print ('Something went wrong, please check the below Exception\n{e}'.format(e=e))

        for token in doc1:
            if token.pos_ in ('PROPN', 'NUM', 'VERB', 'NOUN', 'ADJ'):
                self.search_text += ' ' + token.text

    def Retrive(self, top_n=1):
        '''
        This Function returns top n Wikipedia Pages results based on user query
        '''
        self.search_text = self.search_text.strip()
        search_results = wikipedia.search(self.search_text, results=top_n)
        
        # if we are not able to find any pages for the user query, then wiki search suggestions are used to find relevant page.
        if len(search_results)==0:
          self.search_text = wikipedia.suggest(self.search_text)
          search_results = wikipedia.search(self.search_text, results=top_n)
        
        for docs in search_results:
            self.search_results_pages.append(wikipedia.page(docs,
                    auto_suggest=False))
        return self.search_results_pages
