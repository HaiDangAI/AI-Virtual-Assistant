# AI-Virtual-Assistant
<center><img src="https://user-images.githubusercontent.com/85833803/175766117-350e649b-2dfa-4c12-9418-f6693ec14d42.png" alt='Titanic' style='width:300px;'>
</center><br>

## Idea behind AI Virtual Assistant
  - To begin with an application provide a supporter for user. I created AI Virtual Assistant chatbot.
  - Using NLP basic and neural network to train the AI model
  - And Using tkinter to build an Graphical User Interface

## Progress build project

### Collect the data
{
	"intents": [
	  {
		"tag": "greeting",
		"patterns": [
		  "Hi",
		  "Hey",
		  "How are you",
		  "Is anyone there?",
		  "Hello",
		  "Good day"
		],...
  - The data included intents contain tag, patterns and responses and saved in [content.json](https://github.com/HaiDangAI/AI-Virtual-Assistant/blob/main/content.json)

### NLP preprocessing Pipeline
 - **Tokenizing sentences**
   - Split string sentences into words
    >'I am Chatboter'
    >'I', 'am', 'Chatboter'<br>
    ![image](https://user-images.githubusercontent.com/85833803/175767916-16fd5cc3-601c-438d-84d8-d2ed775d0857.png)
 - **Stemming sentences**
   - Stem words into basic word
   >'organize', 'organizing', 'organization'
   >'organ', 'organ', 'organ'<br>
   ![image](https://user-images.githubusercontent.com/85833803/175767922-ed147fe3-54a1-4392-a035-c2d956cf3ba4.png)
 - **Ignore punctuation characters in sentences**<br>
  ![image](https://user-images.githubusercontent.com/85833803/175767885-4547ded4-c123-4cbc-8ad5-73c48cb5de85.png)
 - **Creating bag of words**
   - Create the bag of words using vector<br>
   ![image](https://user-images.githubusercontent.com/85833803/175767796-084d29e8-31e9-487a-acc6-58a9679d15b7.png)
 
 ### Training model
  - Using neural network included: 3 layers
    - Dense included 128 neurons, using activation relu, with input is shape of bag words
    - Dense included 64 neurons, using activation relu
    - Dense included 7 neurons, using activation softmax
  - Stochastic gradient descent (SGD) to optimize
  - Sparse categorical crossentropy to compute loss function with epochs=1000
### Run chatbot
```
python GUI.py
```

https://user-images.githubusercontent.com/85833803/175768946-fc66d2c0-b3a7-4186-85f0-b657ca8dc0e0.mp4


