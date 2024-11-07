# Customer Churn Prediction Model

Customer churn poses a significant challenge for businesses across industries. In order to address this issue, we present a customer churn prediction model that utilizes machine learning techniques to identify customers who are likely to churn. By accurately predicting customer churn in advance, businesses can take proactive measures to retain valuable customers and mitigate revenue loss.

## About IndiaMart

IndiaMART is India's largest online B2B marketplace, connecting buyers with suppliers. With a commanding 60% market share of the online B2B classified space in India, the platform focuses on providing a robust platform for Small & Medium Enterprises (SMEs), large enterprises, and individuals.

## Data Source

This project is built upon real-world data provided by IndiaMART. The customer churn model leverages a diverse set of features, primarily classified into Engagement, Enrichment, Profile, and Sales. Let's explore each type of feature in detail.

### Engagement Features

Engagement features provide insights into a customer's interaction and engagement with the company and its products. The following parameters fall under this category:

- Logic Rating: Represents the customer's rating based on their purchase history and other factors.
- Logic TAT Slab: Measures the Turn Around Time (TAT) for customer requests.
- Logic PL: Refers to the number of days the customer was active within 30 days from service activation (DAU - Daily Active Users).
- >=3 Multi Angle Img: Indicates whether the customer has uploaded three or more multi-angle images.
- Logic DAU: Captures the frequency of customer activity.
- Logic D rank and Logic A rank: These parameters categorize customers into different ranks based on their engagement level.

### Enrichment Features

Enrichment features evaluate the services provided to customers. Some examples include:

- Customer care support: Assesses the customer support services provided by the company.
- Mcat Count Slab: Measures the number of products listed in the catalog.
- Logic IA (Internal Audit): Represents an internal quality score for the catalog produced for the customer.

### Profile Features

Profile features provide information about the customer's characteristics and background. They include:

- Vertical: Indicates the industry or vertical to which the customer belongs.
- Logic Turnover: Represents the customer's turnover.
- Logic Tier: Indicates the tier of the customer.
- PNS Count: Measures the count of PNS (Payment and Settlement System) transactions.
- Industry Slab: Represents the industry category of the customer.
- Logic Nob: Provides information about the customer's nature of business.
- Entity: Captures the entity type of the customer.
- Logic Broad Industry: Represents the broad industry category.
- Code Bank: Indicates the bank code associated with the customer.

### Sales Features

Sales features provide insights into the customer's purchasing behavior and sales-related activities. They include:

- Convincing: Measures the level of effort required to convince the customer to make a purchase.
- Sales Pitches: Indicates the number of sales pitches made before the customer's purchase decision.

## Project Tasks

This project focuses on the following tasks to develop an effective churn prediction model:

### Task 1: Identify the Most Predictive set of Features

The first task involves identifying which among the engagement, enrichment, profile, and sales features are most helpful in predicting customer churn. By evaluating this we can get an understanding of what kind of features are most detrimental in customer churn.

This repository contains four Jupyter Notebook files, namely Engagement.ipynb, Enrichment.ipynb, Profile.ipynb, and Sales.ipynb. Each notebook focuses on analyzing a specific set of features to determine their effectiveness in predicting customer churn. It is important to note that the primary objective of these notebooks is to compare the relative accuracy among the four types of features, rather than achieving the highest absolute accuracy.

### Task 2: Feature Selection using Weight of Evidence (WoE) and Information Value (IV)

In Task 2, we calculate the Weight of Evidence (WoE) and Information Value (IV) for each variable individually. This analysis helps us determine the best feature for our machine learning classification task. WoE and IV provide valuable insights into the predictive strength of each feature and their overall contribution to the model's accuracy.

### Task 3: Model Deployment and Selection

In Task 3, we deploy different machine learning models using the selected features and evaluate their performance. By comparing the accuracy of various models, we select the one that yields the highest accuracy for predicting customer churn. In this project, multiple models have been trained and evaluated to predict customer churn. By comparing the accuracy of these different models, the one that yields the highest accuracy for predicting customer churn has been identified and included in the repository.

Accurate customer churn predictions enable informed decision-making and facilitate the development of effective strategies to enhance customer retention and drive business growth.

For any inquiries or suggestions, please feel free to contact me.

Best Regards,
Shishir Hardia
