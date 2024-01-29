import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Sample data
input_instructions = [
    "Start by preheating the oven to 350°F.",
    "In a large mixing bowl, combine the flour and sugar.",
    "Beat the eggs and add them to the mixture.",
    "Pour the batter into a greased baking pan."
]

# Target labels (desired step for each instruction)
target_steps = [1, 2, 3, 4]

# Tokenize the input instructions
tokenizer = Tokenizer()
tokenizer.fit_on_texts(input_instructions)
total_words = len(tokenizer.word_index) + 1

# Convert text to sequences
input_sequences = tokenizer.texts_to_sequences(input_instructions)

# Pad sequences for uniform length
max_sequence_length = max(len(seq) for seq in input_sequences)
padded_input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='post')

# Build the model
model = tf.keras.Sequential([
    Embedding(total_words, 64, input_length=max_sequence_length),
    LSTM(100),
    Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(padded_input_sequences, target_steps, epochs=50)

# Test the model
test_instruction = ["Mix all the ingredients thoroughly."]
test_sequence = tokenizer.texts_to_sequences(test_instruction)
padded_test_sequence = pad_sequences(test_sequence, maxlen=max_sequence_length, padding='post')

predicted_step = model.predict(padded_test_sequence)
print(f"Predicted Step: {round(predicted_step[0][0])}")