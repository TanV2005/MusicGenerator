# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense, Dropout
# from tensorflow.keras.utils import to_categorical

# def create_model(input_shape, n_vocab):
#     model = Sequential()
#     model.add(LSTM(256, input_shape=input_shape, return_sequences=True))
#     model.add(Dropout(0.3))
#     model.add(LSTM(256))
#     model.add(Dense(128, activation='relu'))
#     model.add(Dense(n_vocab, activation='softmax'))

#     model.compile(loss='categorical_crossentropy', optimizer='adam')
#     return model


# def train_model(model, X, y, epochs=30):
#     y = to_categorical(y)
#     model.fit(X, y, epochs=epochs, batch_size=64)
#     return model





from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_model(input_shape, n_vocab):
    model = Sequential()
    model.add(LSTM(128, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(n_vocab, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model