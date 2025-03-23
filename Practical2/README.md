# Data Processing and Streaming for Restaurant Receipts

## Project Overview

This project performs data processing and analysis of restaurant receipts, utilizing Apache Spark for both batch and stream processing. The main objectives are to enrich the receipt data with weather information, filter and classify orders based on item count, and generate visitor preferences based on these classifications.

The workflow is divided into two main parts:

1. **Batch Processing**:
   - Reads and processes receipt data for 2022.
   - Enriches data with weather information (temperature, city, etc.).
   - Classifies orders based on item count (Tiny, Small, Medium, Large).
   - Computes the original total cost (total cost + discount).
   - Calculates the most popular order type by restaurant.

2. **Stream Processing**:
   - Reads 2021 receipt data continuously in streaming mode.
   - Performs similar transformations and classifications as the batch processing.
   - Joins data with promo offers (cold drinks based on temperature).
   - Saves the processed stream data with additional metadata like batch timestamp.

## Contents of the Output Folder

- **final_state**:
   - Contains processed batch data from the year 2022.
   - Includes columns for restaurant franchise ID, item counts, order types, and the most popular order type per restaurant.
   - Also includes computed fields like `original_total_cost`, `promo_cold_drinks`, and `batch_timestamp`.

- **streamed_2021_state**:
   - Contains real-time streamed data from the year 2021.
   - Similar structure to `final_state`, but data is continuously processed and saved with a batch timestamp.

## How to Run the Project

1. **Set up Apache Spark**: This project requires Spark installed in your environment (locally or in a cloud environment).
2. **Dependencies**: Install necessary Python libraries (`pyspark`), if not already installed.
3. **Running the notebook**: Execute the code in the Colab notebook provided. It will automatically:
   - Process the batch data.
   - Perform the streaming processing.
   - Write the final results to the output folders.

## Download the Output

The following files are available for download:

- **final_results.zip**:
   - Contains both the batch processed data and the streamed data in zip format.
   - Ready to use for further analysis or reporting.

## Additional Notes

- The output files are saved in CSV format.
- This notebook demonstrates how to use Spark for both batch and streaming data processing.
- You can extend this project by adding more filters, enhancing data joins, or integrating with other systems.

