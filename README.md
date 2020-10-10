This is a bot that uses the Google Universal Sentence Encoder Multilingual Model trained on data dumped from an ODS slack channel #_random_b.

We use Universal Sentence Encoder Multilingual Model, which we train on dataset retrieved from slack. The model can be downloaded here:  [https://tfhub.dev/google/universal-sentence-encoder-multilingual/3](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3)

As a basis for model training we use demonstration notebook provided by The TensorFlow Hub Authors. It can be found here: [https://www.tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa](https://www.tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa) 

Step by step instruction:

1. The data which was used for training was taken from ODS Salck Channel [https://opendatascience.slack.com/archives/C36P6D7S4/p1600449516001100](https://opendatascience.slack.com/archives/C36P6D7S4/p1600449516001100) 

    You might need to register in ODS Slack first.

2. The data in JSON format is loaded, preprocessed and stripped of numbers, special symbols etc. in data-cleaning.ipynb notebook that can be opened e.g. in Jupyter. Make sure to put all necessary JSON files in one directory and name it as the path for your data in the notebook. The result is an 'all.txt' file with all sentences that are used for teaching the model.
3. After we have the cleaned data its time to teach the model to work with it.
4. To train model use model.ipynb notebook. The model generates following vairables folder and files following: data.pickle.idx, data.pickle-data.pkl, saved_model.pb.
These files are necessary to run bot-server.py, they must be placed in the same directory with bot-server.py ('variables folder too')
4. Use bot-server.py to run telegram bot webser. In advance you sould register bot in telegram and get token that must be hardcoded in bot-server.py.