from convokit import Corpus, download

corpus = Corpus(filename=download("supreme-2019"))
corpus.dump("supreme-2019", base_path="./")
