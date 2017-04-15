from __future__ import print_function
import keras
from keras.models import Model
import os

import experiment


def main():

    save_key = os.path.basename(__file__).split('.')[0]

    ### DEFINE MODEL ###
    input_shape = (None, None, 6)
    inputs = Input(shape=input_shape)

    y1 = Conv2D(64, (5, 5), padding='same', activation='relu', name='bendy1')(inputs)
    y2 = Conv2D(16, (60, 3), padding='same', activation='relu', name='deharm')(y1)
    y3 = Conv2D(64, (5, 5), padding='same', activation='relu', name='bendy2')(y2)
    y4 = Conv2D(64, (3, 3), padding='same', activation='relu', name='smoothy1')(y3)
    y5 = Conv2D(64, (3, 3), padding='same', activation='relu', name='smoothy2')(y4)
    y6 = Conv2D(1, (1, 1), padding='same', activation='sigmoid', name='squishy')(y5)
    predictions = Lambda(lambda x: K.squeeze(x, axis=3))(y6)

    model = Model(inputs=inputs, outputs=predictions)

    experiment.experiment(save_key, model)

if __name__ == '__main__':
    main()
