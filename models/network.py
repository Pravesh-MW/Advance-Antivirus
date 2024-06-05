
import pickle
import os


def sanitization(web):
    web = web.lower()
    token = []
    dot_token_slash = []
    raw_slash = str(web).split('/')
    for i in raw_slash:
        raw1 = str(i).split('-')
        slash_token = []
        for j in range(0, len(raw1)):
            raw2 = str(raw1[j]).split('.')
            slash_token = slash_token + raw2
        dot_token_slash = dot_token_slash + raw1 + slash_token
    token = list(set(dot_token_slash))
    if 'com' in token:
        token.remove('com')
    return token


class Network:
    def __init__(self):
        # Get the current file's directory
        self.current_file_path = os.path.abspath(__file__)
        self.parent_directory = os.path.dirname(self.current_file_path)
        self.__load_model()

    def __load_model(self):
        # Loading the model
        model_file = f"{self.parent_directory}\\ML\\pickel_model.pkl"
        with open(model_file, 'rb') as f1:
            self.lgr = pickle.load(f1)
        f1.close()
        vectorizer_file = f"{self.parent_directory}\\ML\\pickel_vector.pkl"
        with open(vectorizer_file, 'rb') as f2:
            self.vectorizer = pickle.load(f2)
        f2.close()

    def predict(self, urls):
        # Using whitelist filter as the model fails in many legit cases since the biggest problem is not finding the malicious urls but to segregate the good ones
        whitelist = ['hackthebox.eu', 'root-me.org', 'gmail.com']
        s_url = [i for i in urls if i not in whitelist]

        # Predicting
        x = self.vectorizer.transform(s_url)
        y_predict = self.lgr.predict(x)

        for site in whitelist:
            s_url.append(site)
        # print(s_url)

        predict = list(y_predict)
        for j in range(0, len(whitelist)):
            predict.append('good')
        print("\nThe entered domain is: ", predict[0])
        return predict[0]

# urls = []
# urls.append(input("Input the URL that you want to check (eg. google.com) : "))
# network = Network()
# network.__load_model()
# print(network.predict(urls))