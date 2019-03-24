# Final Capstone Proposal



1) What are you trying to do? Articulate your objectives using absolutely no jargon (i.e. as if you were explaining to a salesperson, executive, or recruiter).

    * My goal for this project is to use natural language processing and different modeling techniques to predict where the article was published. I will be using articles from "The Onion", "CNN", and "Fox News". The first step will be to build a model that can differentiate between satire and actual news. Then I will see if my model can differentiate between "CNN", and "Fox News".

2) How has this problem been solved before? If you feel like you are addressing a novel issue, what similar problems have been solved, and how are you borrowing from those?

    * I found a similar study done by Dawn Graham. Her results can be found here: https://towardsdatascience.com/fake-news-or-not-edad1552aa02. She used natural language processing to build a logistic regression model that would predict whether or not an article came from r/TheOnion or r/nottheonion based on the headlines of the articles. 

    * Another similar project was done by Geraldine Moriba, and can be found here: https://medium.com/jsk-class-of-2019/how-to-identify-bias-in-cable-news-febc6ae0f22e. In this project the author used natural language processing techniques to build a model that could "analyze cable television news for patterns and trends in content, bias and coverage" (Moriba). Moriba used transcripts from cable news segments to build this model and then attempted to build bias lexicons to help the model distinguish the overall sentiment of the segment, and catagorize it as left or right leaning. 

3) What is new about your approach, why do you think it will be successful?
    * My approach is different from the previous two approachs because I am using the content of news articles from the respective article sources. The projects addressed above used transcripts from news segments on cable television and headlines from different reddit pages. I believe my approach will be more successful because the articles have more context than a headline, and is coming from one author. The cable news segments have multiple opinions from many panelists, which makes it much more difficult for the model to identify the bias in the segment. The articles I am using have one voice. 


4) Who cares? If you're successful, what will the impact be?
    * Fake news is a hot topic in todays news, and distiguishing between "real news" and "fake news" is very important. Ideally this project will develop a model that is able to tell if an article is satirical (being from the onion) or from a real news source like Fox News or CNN. 

    * Secondarily, it is well known that different news sources either lean to the left or to the right politically. Hopefully the model constructed will be able to pick up on those biases and determine if the article was published on Fox News or CNN. 

5) How will you present your work?
    * I will be presenting my work through a PowerPoint presentation. 


6) What are your data sources? What is the size of your dataset, and what is your storage format?
    * The CNN and Fox news articles are coming from a dataset that I found online. The data is stored as a CSV and can be found here: https://www.kaggle.com/lenamkhanh/analyzing-the-news/code. There are around 5,000 Fox News articles and around 15,000 CNN articles. 
    
    * For the Onion articles, I built a webscrapper that scraped the content of each article and stored them into MongoDB. Ideally I will have upwards of 5,000 articles, so that I can have the same size set of articles for each "news" source. 

7) What are potential problems with your capstone, and what have you done to mitigate these problems?

    * Just like with any NLP project, dimensionality will be a huge problem. I will use dimensionality reduction techniques like PCA, SVD, and random forests to address this issue. 

    * Another potential problem with this project will be in the interpretability of the model. If I end up using a non-supervised learner for a model, it will be difficult to interpret the underlying meaning of the model. Ideally I will be able to build a logistic regression model, so interpretability will be easier. 

8) What is the next thing you need to work on?
    * The next step in my project will be to finish scraping all of my onion articles. 
    * After that I will need to use natural language processing techniques, so I can develop several different learners, and identify the best modeling technique for this project. 
    