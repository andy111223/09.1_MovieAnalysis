# Movie Analysis Project
Welcome to the Movie Analysis Project! This repository contains a feature engineering and data analysis workflow aimed at exploring and extracting insights from movie data. The focus is on using the CRISP-DM methodology for data exploration, feature extraction, and visualization. This project provides a great showcase of my ability to analyze datasets, apply advanced statistical techniques, and create compelling visualizations for data storytelling.

## Project Objectives
1. Top-Rated Movies: Extract the top 10 movies with the highest ratings (vote_average), with vote_count greater than the third quartile.
2. Revenue and Budget Analysis: Analyze the average revenue and budget for movies released from 2010 to 2016.
3. Genre Integration: Integrate movie data with genre information.
4. Most Common Genre: Identify the most frequently occurring movie genre in the dataset.
5. Longest Runtime Analysis: Find out which movie genre has the highest average runtime.
6. Visualize Runtime: Create a histogram to visualize the distribution of movie runtimes for the genre with the longest average runtime.

## Libraries Used
- pandas: For data manipulation and analysis.
- numpy: For numerical computations and basic mathematical operations.
- matplotlib: For data visualization, including line plots, bar charts, and histograms.

## Concepts Learned
1. Data Cleaning and Preprocessing:
- Handling missing values using dropna() and coercing datatypes using astype().
- Filtering rows based on specific conditions (e.g., vote counts greater than the third quartile).
2. Data Aggregation and Grouping:
- Using groupby() to calculate average revenue and average budget grouped by year.
- Applying aggregation functions (mean, count) to summarize dataset features.
3. Merging Datasets:
- Merging movie information with genre information using merge() on a common key (genre_id).
4. Data Visualization:
- Bar Charts: Used to visualize average revenue per year.
- Line Plots: To overlay the average budget over time.
- Histogram: Created a histogram of the runtime of movies for the "History" genre.
- Axes Customization: Setting axis labels, titles, legends, and formats to create a well-designed visualization.
- Data Format Customization: Using FuncFormatter to format y-axis labels in millions (mln).

## Python Methods and Functions Utilized
1. Data Manipulation:
- `pd.read_csv()`: Load CSV files.
- `df.dropna()`, `df.fillna()`, `df.astype()`: Handle missing values and convert datatypes.
- `df.quantile()`, `groupby()`, `agg()`, `value_counts()`: Perform statistical calculations.
- `merge()`: Join multiple DataFrames.
2. Data Selection:
- Filtering data using boolean indexing (`movies[movies['vote_count'] > third_quartile]`).
- Selecting columns and sorting using `.sort_values()`.
3. Data Visualization:
- `plt.subplots()`, `ax.bar()`, `ax.plot()`, `plt.hist()`: Plot various types of charts.
- Customizing plots using `set_xlabel()`, `set_ylabel()`, `set_title()`, and `set_xticks()`.
- Setting up grid lines and adjusting transparency (alpha) for visual clarity.
4. Additional Formatting:
- `ticker.FuncFormatter()`: Format axis tick labels.
- `plt.tight_layout()`: Ensure appropriate spacing and padding in visualizations.
- `set_xticklabels()`: Rotate and customize x-axis tick labels.

## Example Analysis and Visualizations
1. Top 10 Highest Rated Movies
Identified the top 10 movies with the highest average rating (vote_average) among those with a vote count (vote_count) higher than the 75th percentile.
2. Revenue and Budget Analysis (2010-2016)
The average revenue and average budget were computed for movies from 2010-2016.
A bar chart was used to visualize average revenue per year, while a line plot showed the average budget on the same axes.
The y-axis was formatted to display amounts in millions (mln) of USD.
3. Most Common Genre
After merging movies with genres, we determined the most frequent genre by applying value_counts() to the genres column.
4. Longest Runtime Genre
Grouped movies by genres to determine which genre has the highest average runtime.
The "History" genre was found to have the longest average runtime.
5. Runtime Histogram for "History" Genre
Created a histogram of movie runtimes for the "History" genre.
Enhanced the histogram's appearance with custom colors, grid lines, and transparency.

## How to Run the Project
1. Clone the repository:

    `git clone https://github.com/andy111223/09.1_MovieAnalysis.git`

2. Navigate to the project directory:

    `cd 09.1_MovieAnalysis`

3. Install the required Python packages:

    `pip install pandas numpy matplotlib`

4. Run the analysis:

    `python3 main.py`

## Skills Demonstrated
- Data Wrangling and Cleaning: Leveraged pandas to clean, preprocess, and join different datasets.
- Exploratory Data Analysis (EDA): Conducted EDA to extract key insights such as top-rated movies, trends in revenue and budget, and runtime distributions.
- Data Visualization: Developed various types of visualizations using Matplotlib, demonstrating proficiency in visual communication and data storytelling.
- Feature Engineering: Added new features such as year and genres to improve the dataset for analysis.

## Future Improvements
- More Advanced Visualizations: Explore using other libraries like Seaborn for more refined and aesthetically pleasing plots.
- Deeper Feature Engineering: Create additional features that can help in a potential machine learning model, such as profit margin or budget categorization.