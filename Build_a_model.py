# Input/dense/output layers
from tensorflow.keras.layers import Input, Dense
input_tensor = Input(shape=(1,))
output_tensor = Dense(1)(input_tensor)

# Build the model
from tensorflow.keras.models import Model
model = Model(input_tensor, output_tensor)