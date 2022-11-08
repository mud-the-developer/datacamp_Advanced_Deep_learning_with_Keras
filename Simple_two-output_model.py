# Define the input
input_tensor = Input((2,))

# Define the output
output_tensor = Dense(2)(input_tensor)

# Create a model
model = Model(input_tensor,output_tensor)

# Compile the model
model.compile(optimizer='adam',loss='mean_absolute_error')