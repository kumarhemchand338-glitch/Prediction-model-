import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Data = {
	"name":["hemchand","karan","sandip","govind","omprakash","khushi"],
	"age":[18,20,18,17,19,18],
	"studying":[3,4,2,1,3,2],
	"gender":["male","male","male","male","male","female"],
	"marks":[45,50,30,25,40,35],
	"result":["pass","pass","fail","fail","pass","fail"]
}
df = pd.DataFrame(Data)

le_gender = LabelEncoder()
le_result = LabelEncoder()

df["gender"] = le_gender.fit_transform(df["gender"])
df["result"] = le_result.fit_transform(df["result"])

X = df[["age","studying","gender","marks"]]
y = df["result"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

linear = LogisticRegression()
linear.fit(X_train,y_train)

prediction = linear.predict(X_test)
print ("model accuracy = ",accuracy_score(y_test,prediction))

age = int(input("enter your age = "))
hours = int(input("how much time did you studying = "))
gender = input("what your gander = ")
marks = int(input("your marks = "))

gender_encoded = le_gender.transform([gender])[0]

X = [[age ,hours,gender_encoded,marks]]
pred = linear.predict(X)

if pred[0] == 1:
	print ("you are likely to pass")
else:
	print ("you are likely to fail ")