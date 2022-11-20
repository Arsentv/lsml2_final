Task: SMS Spam Detection 

Dataset: SMS Spam Collection Data Set from the UCI Machine Learning Repository. The data consists of a text file with a set of SMS messages labeled as either spam or ham.

Model: Fine-Tuning BERT for Text Classification
	optimal hyperparameters:
		- Batch size: 16 
		- Learning rate (Adam): 5e-5 
		- Number of epochs: 2, 3, 4

Scores: 
	 - Validation Accuracy: 0.9871
	 - Validation Precision: 0.9887
	 - Validation Recall: 0.9167


Client: Telegram Bot

![IMG_4568](https://user-images.githubusercontent.com/105422158/202901250-922c0b8e-f6d3-4bff-b03c-9642f2455e5e.PNG)


Repo structure: 
	smsspamcollection: dataset
	spamham.ipynb: notebook with model generation code 
	spamham.bin: trained model 
	server.py, telegram_bot.py: bot's codebase
	Dockerfile: the file to build the bot image 
	docker-compose.yml: used to start the bot 
	requirements.txt: used to specify dependencies

User instructions: 
Clone this repo 
Get the TELEGRAM_TOKEN and fill it in the appropriate places in the code
Run the spamham.ipynb and train the spamham.bin model
Run docker-compose up -d and wait for the build to finish 
