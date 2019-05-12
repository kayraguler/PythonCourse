### classroom data ###
import pandas as pd
import os
os.chdir('KocPython2019/12.GaussianProcesses')
tt = pd.read_csv('immSurvey.csv')
tt.head()

alphas = tt.stanMeansNewSysPooled
sample = tt.textToSend

from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
X = vec.fit_transform(sample)
X
### Word Frequency ###

from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
X = vec.fit_transform(sample)
pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,
random_state=1)

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)
np.corrcoef(ytest, mu_s)
### bigram frequency ###

pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)
X = bigram_vectorizer.fit_transform(sample)
pd.DataFrame(X.toarray(), columns=bigram_vectorizer.get_feature_names()).head()

 rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)
np.corrcoef(ytest, mu_s)