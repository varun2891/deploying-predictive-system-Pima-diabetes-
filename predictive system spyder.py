import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users\Hp\Downloads/machinelearning/trained_model.sav','rb'))

input_data = (1,103,80,11,82,19.4,0.491,22)

# changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are finding the output for one instance
reshaped_numpy_array = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_as_numpy_array)
print(prediction)
if (prediction[0]) == 0:
  print("The patient is non-diabetic")
else:
  print('The patient is diabetic')