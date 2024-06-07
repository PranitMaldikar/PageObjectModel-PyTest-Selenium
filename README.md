# Portfolio Test Automator

## Project Overview
The Portfolio Test Automator is designed to automate the testing of virtual stock trading functionalities on platforms like *TBD. Using Pytest and the Page Object Model, this framework aims to ensure robust performance of trading platforms by automating tests for adding, managing, and selling stocks in a virtual portfolio.

### Problem Statement
Develop a test automation framework using Pytest and the Page Object Model to validate functionalities of a virtual stock trading website. The tests should verify the following functionalities:
1. **Adding Stocks to a Virtual Portfolio**: Ensure that users can add stocks to their virtual portfolio and verify the addition.
2. **Selling Stocks Based on Criteria**: Implement functionality to wait for certain market criteria or stock performance thresholds to be met before executing a sell order.
3. **Updating Portfolio Values**: After selling the stock, the test should confirm that the stock has been removed from the portfolio and that the portfolio's value has been updated correctly.

### Key Test Scenarios
1. **Test Adding Stock**:
   - Navigate to the stock addition page.
   - Select a stock and add it to the portfolio.
   - Assert that the stock appears in the user's portfolio.
2. **Test Selling Stock**:
   - Monitor the stock's criteria (e.g., price reaching a specific target).
   - Once the criteria are met, sell the stock.
   - Assert that the stock has been removed from the portfolio.
3. **Test Portfolio Value Update**:
   - After the sale, check if the total value of the portfolio reflects the recent transaction.
   - Assert that the updated value is calculated correctly based on the sale.
     
## Conclusion
The Portfolio Test Automator ensures that virtual trading platforms function as expected, making it a critical tool for maintaining the reliability and performance of financial software.
