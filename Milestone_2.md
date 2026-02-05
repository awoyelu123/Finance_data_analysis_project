# Milestone 2: Extract the loans data

The goal of this milestone will be to create the required Python Classes to extract the loan payment data from a database in the cloud.
Once extracted, familiarise yourself with the data before moving on to performing data cleaning tasks and Exploratory Data Analysis.

---

<details>
<summary><h4>Prerequisites Content: Task 1</h4></summary>

`1. What is Python?` `2. Google Colab` `3. Variables` `4. Comments` `5. Numbers` `6. Strings` `7. Booleans` `8. Lists` `9. Dictionaries` `10. Tuples` `11. Sets` `12. Intro to Control Flow ` `13. Functions ` `14. For Loops, Iteration and Control Flow Tricks` `15. Error Handling with Control Flow` `16. Assertions` `17. Context Managers` `18. Comprehensions` `19. Defining Functions` `20. Object Oriented Programming` `21. Principles of OOP Design` `22. What is `self` in Python?` `23. Magic Methods` `24. Principles of OOP - Abstraction` `25. Principles of OOP - Encapsulation` `26. Principles of OOP - Inheritance` `27. Principles of OOP - Polymorphism` `28. Checks for code quality` `29. What is SQL?` `30. SQL Setup`

</details>

<details>
<summary><h3>Task 1: Initialise a class to extract the data</h3></summary>

In this task you will initialise the class and script that you will use to extract the data from the cloud.
The definition of the classes and methods are meant as guidance. If you would like to follow a difference project/class structure feel free to do so.
The class methods won't be defined in this step, they will be defined once required in subsequent tasks.

Step 1: Create a new Python script `db_utils.py` which will contain your code to extract the data from the database.

Step 2: Within the script create a new class called `RDSDatabaseConnector`. This class will contain the methods which you will use to extract data from the RDS database.

Step 3: Create and Restore the database to be used for the `RDSDatabaseConnector` class.

You can find the `.tar` file required for the restore function at this [link](../project-data/eda_raw_db.tar).

To do this:

1. Open `PGAdmin4` and right click on Databases then select `"Create"` > `"Database"` then name it `EDA_Data`

2. Once create, right-click the new database and select `"Restore"`

  - In the Format selection make sure to select the option with `"tar"`.

  - Tip: If you cannot see the `.tar` file in its location then its likely currently set to "Custom Files". You must change this to "All Files" to make the `.tar` file available for restore!

3. After the restore completes, check the tables to make sure the data is there.

</details>

<details>
<summary><h4>Prerequisites Content: Task 2</h4></summary>

`1. Tabular Data` `2. YAML` `3. What is SQL?` `4. SQL Setup` `5. SQL Tools Setup` `6. SQL Commands` `7. psycopg2 and SQLAlchemy` `8. What is the Cloud?` `9. Essential Cloud Concepts` `10. What is AWS?` `11. AWS Identity and Access Management (IAM)` `12. Amazon EC2` `13. Virtual Private Cloud (VPC)` `14. Amazon RDS `

</details>

<details>
<summary><h3>Task 2: Extract the data from the PGAdmin4 database</h3></summary>

The loan payments data is stored in your local `EDA_Data` database. You will need to create the methods which will enable you to extract the data from this database.

Step 1: Create a `credentials.yaml` file to store the database credentials.

Remember to add this file to your `.gitignore` file in your repository, as you don't want your credentials being pushed to GitHub for security reasons.

Add the following credentials to your `credentials.yaml` file which will allow you to connect to the local database:

RDS_HOST: localhost

RDS_PASSWORD: your_password

RDS_USER: your_user

RDS_DATABASE: EDA_Data

RDS_PORT: 5432

Step 2: If you haven't already installed Python `PyYAML` package you should do so before the next step. This can be installed by running `pip install PyYAML` in the terminal and imported using `import yaml`. This will allow you to load your `credentials.yaml` file as a dictionary.

Step 3: After installing the package create a function which loads the `credentials.yaml` file and returns the data dictionary contained within.
This will be be passed to your `RDSDatabaseConnector` as an argument which the class will use to connect to the local database.

Step 4: Write the `__init__` method of your `RDSDatabaseConnector` class. It should take in as a parameter a dictionary of credentials which your function from the previous step will extract.

Step 5: Define a method in your `RDSDatabaseConnector` class which initialises a `SQLAlchemy` engine from the credentials provided to your class.
This engine object together with the `Pandas` library will allow you to extract data from the database.

Step 6: Develop a method which extracts data from the RDS database and returns it as a `Pandas` DataFrame.
The data is stored in a table called `loan_payments`.

Step 7: Now create another function which saves the data to an appropriate file format to your local machine.
This should speed up loading up the data when you're performing your EDA/analysis tasks.
The function should save the data in `.csv` format, since we're dealing with tabular data.

</details>

<details>
<summary><h3>Task 3: Familiarise yourself with the data</h3></summary>

With the data being stored locally, create a function which will load the data from your local machine into a `Pandas` DataFrame.

In this step you might want to print the shape of the data to understand the size of the data you're working with.
Printing out a sample of the data can help give a quick overview of its columns and values.
The columns names might be quite alien to you if you've never used data from the financial domain before.
Below is a data dictionary which describes all columns of the database to help you understand their meaning:

- `id`: Unique id of the loan
- `member_id`: Id of the member to took out the loan
- `loan_amount`: Amount of loan the applicant received
- `funded_amount`: The total amount committed to the loan at that point in time
- `funded_amount_inv`: The total amount committed by investors for that loan at that point in time
- `term`: The number of monthly payments for the loan
- `int_rate (APR)`: Annual (APR) interest rate of the loan
- `instalment`: The monthly payment owned by the borrower. This is inclusive of the interest.
- `grade`: Loan company (LC) assigned loan grade
- `sub_grade`: LC assigned loan sub grade
- `employment_length`: Employment length in years
- `home_ownership`: The home ownership status provided by the borrower
- `annual_inc`: The annual income of the borrower
- `verification_status`: Indicates whether the borrowers income was verified by the LC or the income source was verified
- `issue_date`: Issue date of the loan
- `loan_status`: Current status of the loan
- `payment_plan`: Indicates if a payment plan is in place for the loan. Indication borrower is struggling to pay.
- `purpose`: A category provided by the borrower for the loan request
- `dti`: A ratio calculated using the borrower's total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income
- `delinq_2yr`: The number of 30+ days past-due payments in the borrower's credit file for the past 2 years
- `earliest_credit_line`: The month the borrower's earliest reported credit line was opened
- `inq_last_6mths`: The number of inquiries in past 6 months (excluding auto and mortgage inquiries)
- `mths_since_last_record`: The number of months' since the last public record
- `open_accounts`: The number of open credit lines in the borrower's credit file
- `total_accounts`: The total number of credit lines currently in the borrower's credit file
- `out_prncp`: Remaining outstanding principal for total amount funded
- `out_prncp_inv`: Remaining outstanding principal for portion of total amount funded by investors
- `total_payment``: Payments received to date for total amount funded
- `total_rec_int`: Interest received to date
- `total_rec_late_fee`: Late fees received to date
- `recoveries`: Post charge off gross recovery
- `collection_recovery_fee`: Post charge off collection fee
- `last_payment_date`: Date on which last month payment was received
- `last_payment_amount`: Last total payment amount received
- `next_payment_date`: Next scheduled payment date
- `last_credit_pull_date`: The most recent month LC pulled credit for this loan
- `collections_12_mths_ex_med`: Number of collections in 12 months' excluding medical collections
- `mths_since_last_major_derog`: Months' since most recent 90-day or worse rating
- `policy_code`: Publicly available `policy_code=1` new products not publicly available `policy_code=2`
- `application_type`: Indicates whether the loan is an individual application or a joint application with two co-borrowers

A markdown copy of the data dictionary can be found at the following [link](../project-data/loan_data_dict.md).

</details>

<details>
<summary><h4>Prerequisites Content: Task 4</h4></summary>

`1. Operating Systems` `2. What is the command line` `3. File Navigation & File Paths` `4. Git and Version Control` `5. Commits and Branches` `6. What is Github?` `7. Github README files`

</details>

<details>
<summary><h3>Task 4: Update the latest code changes to GitHub</h3></summary>

Update your GitHub repository with the latest code changes from your local project. Start by staging your modifications and creating a commit. Then, push the changes to your GitHub repository.

Additionally, document your progress by adding to your GitHub `README` file.
You can refer to the relevant lesson in the prerequisites for this task for more information.

At minimum, your `README` file should contain the following information:
  - Project Title
  - Table of Contents, if the `README` file is long
  - A description of the project: what it does, the aim of the project, and what you learned
  - Installation instructions
  - Usage instructions
  - File structure of the project
  - License information

  You don't have to write all of this at once, but make sure to update your `README` file as you go along, so that you don't forget to add anything.

</details>

<details>
<summary><h3>Task 5: Refactor and optimise current code</h3></summary>

Refactoring will be a continuous and constant process, but this is the time to really scrutinise your code.

You can use the following list to make improvements:

- Meaningful Naming: Use descriptive names for methods and variables to enhance code readability. For example, `create_list_of_website_links()` over `links()` and use `for element in web_element_list` instead of `for i in list`.
- Eliminate Code Duplication: Identify repeated code blocks and refactor them into separate methods or functions. This promotes code reusability and reduces the likelihood of bugs.
- Single Responsibility Principle (SRP): Ensure that each method has a single responsibility, focusing on a specific task. If a method handles multiple concerns, split it into smaller, focused methods.
- Access Modifiers: Make methods private or protected if they are intended for internal use within the class and not externally accessible
- Main Script Execution: Use the `if __name__ == "__main__":` statement to include code blocks that should only run when the script is executed directly, not when imported as a module
- Consistent Import Order: Organize `import` statements in a consistent manner, such as alphabetically, and place `from` statements before `import` statements to maintain readability
- Avoid Nested Loops: Minimize nested loops whenever possible to improve code efficiency and reduce complexity
- Minimal Use of self: When writing methods in a class, only use `self` for variables that store information unique to each object created from the class. This helps keep the code organized and ensures that each object keeps its own special data separate from others.
- Avoid `import
* `: Import only the specific methods or classes needed from a module to enhance code clarity and prevent naming conflicts
- Consistent Docstrings: Provide clear and consistent docstrings for all methods, explaining their purpose, parameters, and return values. This aids code understanding for other developers.
- Type Annotations: Consider adding type annotations to method signatures, variables, and return values to improve code maintainability and catch type-related errors during development

</details>

