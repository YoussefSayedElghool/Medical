import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


data=pd.read_csv("C:\\Users\\m\\Desktop\\Medical\\Disease_data.csv")
data.head()


data=data.drop(columns=["Age"])


la=LabelEncoder()
data['Age_Category']=la.fit_transform(data['Age_Category'])
data['Gender']=la.fit_transform(data['Gender'])



d=data.replace("yes",1)
d=d.replace("no",0)
d.head()


x_train,x_test,y_train,y_test=train_test_split(d.drop(columns=['Disease']),d['Disease'],test_size=0.2,random_state=42)


model1=RandomForestClassifier(random_state=42)
model1.fit(x_train,y_train)
model1.score(x_test,y_test)

print(x_test)
import pickle

# Example: Assuming `model` is your trained model or any Python object

# Serialize model to a pickle file
with open('model_test_two.pkl', 'wb') as file:
    pickle.dump(model1, file)

print("Model has been saved as 'model.pkl'.")





