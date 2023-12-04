import pickle

file = open('model.pkl', 'wb')
pickle.dump(modle, file)

save_model_file = open('model.pkl', 'rb')
save_model = pikle.load(save_model_file)

car_data = {
	'throttle' : [0.364332455],
	'distance' : [6.674762726]
}

data = pd.DataFrame(car_data, columns=['throttle', 'distance'])
predicated_data = save_model.predict(data)
print("your prediction from dta is:"predicted_data)