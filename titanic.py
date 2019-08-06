import pickle
filename = 'finalized_titanic_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
predict_vars = [1,1,1,0,2,6,1,3,4]
pred = loaded_model.predict([predict_vars])  
if pred == 0:
     result="lost beneath the waves!"
else:
    result="My..heart..will..go..on! "
print(result)