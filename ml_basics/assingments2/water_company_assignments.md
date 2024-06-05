## Assignment 2: Apply CRISP-DM process for Water Company Data

Note! There is a lot of "artistic freedom" in this assignment, so don't think only about the points and try to come up with something new and creative from the data.

Note! A concise and focused answer is better than a long and broad one to this assignment.

## Student Information
- **Name**: Fadi Helal
- **Student ID**: 2312951

# CRISP-DM process 

Assignments **2.1-2.2** you have an "imaginary project" where **you are consulting a water company**.
In this assignment, you will use the **CRISP-DM process model**.

* The data source is the water usage statistics published by the **Yorkshire Water** company for the years **2012–2015**
* The data source in the Assignment is from [https://datamillnorth.org/dataset/yorkshire-water-daily-customer-meter-data--local-area-](https://datamillnorth.org/dataset/yorkshire-water-daily-customer-meter-data--local-area-)

Note! You can use the Finnish-language [Yorkshire Water Jupyter Notebook document](jupyter_data/YorkshireWater_data_analysointi.ipynb) to analyze the results.
Or make your own data analysis document entirely if you have a lots of motivation to learn.

Below is some additional information about the data from its provider's website:

* A dataset showing daily water consumption readings in Cubic meters (m3) from internal and/or external meters in a discrete study in two distribution management areas (DMAs) in Yorkshire between 2013 and 2015.
* Data is taken from a live localized project investigating water use.
* Data has been anonymized to remove personal data and make its Data Protection Act compliant.
* The DMAs are also anonymized to prevent any open data activity affecting the results of the ongoing study the data has been taken from.

# CRISP-DM Process for Yorkshire Water Company Data Analysis

## Assignment 2.1: CRISP-DM: Business Understanding (max. 5p)

We are looking for answers, for example, to the following questions:
* What kind of data is involved?
* In what context can this data be useful?
* What kind of business is behind the data?
* What can be learned from data?
* What can be seen from the data?
* What can be identified from the data?
* Can something unusual be detected in the data?
* Is any other additional information needed in addition to this?

You can also tell us other considerations related to this assignment.
## Assignment 2.1 (ANSWER): Business Understanding

### Overview of Data
The dataset comprises daily water consumption readings in cubic meters (m³) from internal and external meters across two anonymized Distribution Management Areas (DMAs) in Yorkshire from 2013 to 2015. This anonymization ensures compliance with the Data Protection Act and prevents data misuse.

### Utility of Data
- **Demand Forecasting**: The data helps in predicting water demand, facilitating efficient water supply management.
- **Leak Detection**: Anomalies in the data could indicate potential leaks, allowing for timely maintenance and water conservation.
- **Customer Segmentation**: Usage patterns can help segment customers by consumption levels, guiding targeted conservation programs.

### Insights from Data
- **Consumption Patterns**: Initial analysis can reveal daily, seasonal, or annual trends in water usage.
- **Anomalies**: Sudden spikes or unusual consumption rates might be detected, indicating possible leaks or meter faults.

### Additional Data Needs
- **Weather Data**: Incorporating weather conditions could help explain fluctuations in water usage due to temperature or rainfall.
- **Consumer Feedback**: Surveys about water usage habits could provide deeper insights into the data, improving demand management strategies.


# Assignment 2.2: CRISP-DM: Data Understanding (max. 5p)

We are looking for answers, for example, to the following questions:
* What kind of columns are there in the data?
* What value has been used as a filler value?
* What kind of correlations can be found in the data?
* Review data at specific time intervals (e.g., week, month or year).
* Visualized data can be attached to support observations
* You can calculate basic statistics and summaries of the data
* Think about what can possibly be done with this data in the real project?

You can also tell us other considerations related to this assignment.
## Assignment 2.2 (ANSWER): Data Understanding

### Data Structure and Contents
- **Columns**: The datasets include columns for meter readings by date, meter ID, and location, along with DMA identifiers.
- **Filler Values**: A value of `-1` is commonly used to indicate missing or unavailable data across several datasets.

### Exploratory Data Analysis
- **Correlations**: Initial review may show correlations between the number of occupants in a household and water usage, influencing further analysis.
- **Time-Based Analysis**: Reviewing data over different intervals (weekly, monthly, yearly) reveals usage trends and helps in capacity planning.

### Potential Uses of Data
- **Predictive Maintenance**: Using anomaly detection algorithms to predict and prevent leaks.
- **Resource Allocation**: Optimizing water supply based on predicted demand from historical usage patterns.

### Additional Considerations
- **Data Quality**: Significant attention is needed to handle missing data (-1 values) to ensure analysis accuracy.
- **Visualization**: Charts and graphs can be used to visually represent consumption trends and anomalies, aiding in more intuitive data understanding.





Note! Comprehensive data analysis is not required for full points. At this stage, the aim is to get an overall picture of 
the problem and dataset to be used for the future analysis phase and modeling phase.

The answer will be returned to the repository by the given return date:
* the return is made in MarkDown format (extension .md) or Jupyter Notebook (extension .ipynb) format.
* The images and figures are directly linked to the documents to be returned.

### Data processing

* See published [Yorkshire Water Jupyter Notebook document](jupyter_data/YorkshireWater_data_analysointi.ipynb). Note that this document is currently available only in _Finnish_.
* You can use this to help you understand the data in the dataset.
* It can also be supplemented to make additional observations and analysis (you can improve it yourself, implement new tool or use other tools to explore Data)

Note that the data also includes a [survey of consumer habits](jupyter_data/Yorkshire_Water_consumer_habits.csv). That should also be addressed in the assignments.






