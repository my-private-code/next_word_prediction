# Next word prediction
Updated from https://github.com/renatoviolin/next_word_prediction

Simple application using transformers models to predict next word or a masked word in a sentence.

The purpose is to demo and compare the main models available up to date.

The first load take a long time since the application will download all the models. Beside 6 models running, inference time is acceptable even in CPU.

### Application
This app implements two variants of the same task (predict <mask> token). The first one consider the <mask> is at end of the sentence, simulating a prediction of the next word of the sentece.

The second variant is necessary to include a <mask> token where you want the model to predict the word.


![Word prediction](word_prediction.gif)

### Running 

```sh
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
venv/bin/python app.py
```

Open your browser http://localhost:8000

bart模型我刚测试了，貌似也不错。但是内存占用比较大，启用后到了2.24G内存，api响应也变慢了一点


