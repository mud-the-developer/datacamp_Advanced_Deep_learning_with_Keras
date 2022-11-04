# Imports
from tensorflow.keras.layers import Subtract
from tensorflow.keras.models import Model

# Subtraction layer from previous exercise
score_diff = Subtract()([team_1_strength, team_2_strength])

# Create the model
model = Model([team_in_1, team_in_2], score_diff)

# Compile the model
model.compile(optimizer='adam', loss = 'mean_absolute_error')