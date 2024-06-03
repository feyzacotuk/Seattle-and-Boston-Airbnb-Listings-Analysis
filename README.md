# Seattle and Boston Airbnb Listings Analysis

## Installation
This project requires Python 3.x and the following libraries:

- pandas
- seaborn
- matplotlib

You can install these libraries using pip:
`
pip install pandas seaborn matplotlib `

## Project Motivation

This project aims to analyze Airbnb listings in Seattle and Boston to uncover insights about hosts and their impact on review scores. Specifically, we investigate the relationships between host characteristics (e.g., response rate, acceptance rate, superhost status) and review scores. This analysis can help potential hosts understand factors that contribute to higher review scores and improve their listings accordingly.

## Summary of the Results
The analysis reveals interesting insights into the factors influencing review scores for Airbnb listings in Seattle and Boston. The following are the key findings:

Seattle:
The correlation between price and review scores is 0.0551.
Boston:
The correlation between price and review scores is 0.0960.
These results suggest a slight positive correlation between listing price and review scores in both cities. However, the correlation is relatively weak, indicating that price is not a major determinant of review scores.
You can read the my medium write in this[https://medium.com/@feyzacotukk/understanding-what-influences-airbnb-review-scores-a-tale-of-two-cities-f14276289c68] link

## File Descriptions
`listings_seatle.csv`: Dataset containing Airbnb listings information for Seattle.
`listings.csv`: Dataset containing Airbnb listings information for Boston.
`compare_seatle_boston`.ipynb: Python script for loading, cleaning, and analyzing the datasets.

## Licensing, Authors, Acknowledgements
This project was developed by [feyzacotuk]. Special thanks to the data providers, Airbnb, for making this data publicly available. This project is licensed under the MIT License.
