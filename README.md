**Task:** SMS Spam Detection 

**Dataset**: SMS Spam Collection Data Set from the UCI Machine Learning Repository. The data consists of a text file with a set of SMS messages labeled as either spam or ham.

**Model**: Fine-Tuning BERT for Text Classification

Optimal hyperparameters:
	
	- Batch size: 16 
	- Learning rate (Adam): 5e-5 
	- Number of epochs: 2, 3, 4

**Scores**: 

	 - validation Accuracy: 0.9871
	 - validation Precision: 0.9887
	 - validation Recall: 0.9167


**Client**: Telegram Bot




**Repo structure**: 

	- smsspamcollection: dataset
	- spamham.ipynb: notebook with model generation code 
	- spamham.bin: trained model 
	- server.py, telegram_bot.py: bot's codebase
	- Dockerfile: the file to build the bot image 
	- docker-compose.yml: used to start the bot 
	- requirements.txt: used to specify dependencies
	
| LEFT | LEFT | 
|----------------|:---------:|
| smsspamcollection | dataset | 


**User instructions**: 

1. Clone this repo 
2. Get the TELEGRAM_TOKEN and fill it in the appropriate places in the code
3. Run the spamham.ipynb and train the spamham.bin model
4. Run docker-compose up -d and wait for the build to finish 
