**Task:** SMS Spam Detection 

**Dataset**: SMS Spam Collection Data Set from the UCI Machine Learning Repository. The data consists of a text file with a set of SMS messages labeled as either spam or ham.

**Model**: Fine-Tuning BERT for Text Classification

the original project https://towardsdatascience.com/fine-tuning-bert-for-text-classification-54e7df642894

Optimal hyperparameters:
	
	- Batch size: 16 
	- Learning rate (Adam): 5e-5 
	- Number of epochs: 2, 3, 4

**Scores**: 

	 - validation Accuracy: 0.9871
	 - validation Precision: 0.9887
	 - validation Recall: 0.9167


**Client**: Telegram Bot


![IMG_4568](https://user-images.githubusercontent.com/105422158/202902256-6d3d6548-04e6-405d-a438-fa031cd0e407.PNG)


**Repo structure**: 

	
| name | function | 
|----------------|---------|
| smsspamcollection | dataset | 
| spamham.ipynb | notebook with model generation code | 
| spamham.bin | trained model  | 
| server.py, telegram_bot.py |  bot's codebase| 
| Dockerfile | the file to build the bot image  | 
| docker-compose.yml | used to start the bot  | 
| requirements.txt |  used to specify dependencies | 


**User instructions**: 

1. Clone this repo 
2. Get the TELEGRAM_TOKEN and fill it in the appropriate places in the code
3. Run the spamham.ipynb and train the spamham.bin model
4. Run docker-compose up -d and wait for the build to finish 
