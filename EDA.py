#reading the dataset 
train= pd.read_csv('D:/data science/comic/issue3/code/dataset/heart.csv')
train.head(5)
train.describe()
#finding any co-relation by a correlation matrix
rcParams['figure.figsize'] = 20, 14
plt.matshow(train.corr())
plt.yticks(np.arange(train.shape[1]), train.columns)
plt.xticks(np.arange(train.shape[1]), train.columns)
plt.colorbar()
train.hist()
rcParams['figure.figsize'] = 8,6
plt.bar(train['target'].unique(), train['target'].value_counts(), color = ['red', 'green'])
plt.xticks([0, 1])
plt.xlabel('Target Classes')
plt.ylabel('Count')
plt.title('Count of each Target Class')
