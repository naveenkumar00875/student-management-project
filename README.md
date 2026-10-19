Student Performance Analysis System And Automation alert System

Project Summary
The Student Performance Analysis System is a Python-based project that analyzes student marks, calculates total marks and average scores, generates a performance report, and automates sending performance updates to parents through email.

The project uses workflow automation to simplify repetitive reporting tasks and reduce manual effort.

Features
- Reads student marks from a CSV file.
- Calculates total marks and average scores.
- Generates a performance report in a text file.
- Sends student performance updates to parents through an automated email workflow.
- Runs the analysis using GitHub Actions.
- Integrates with Make.com through a webhook for email automation.

Technologies Used
- Python
- Pandas
- CSV and text-file processing
- Make.com
- Webhooks and HTTP requests
- GitHub Actions

How It Works
1. Student marks are stored in a CSV file.
2. The Python program reads and processes the data.
3. Total marks and average scores are calculated.
4. A report is generated as `report.txt`.
5. The program sends data to a Make.com webhook.
6. The automation workflow sends performance updates to parents.
7. GitHub Actions can run the analysis workflow on demand.

Project Structure
'''
student-management-project/
├── main.py
├── Student.csv
├── requirements.txt
├── report.txt
├── READ_ME
└── .github/
    └── workflows/
        └── workflow.yml
'''
How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/naveenkumar00875/student-management-project.git
cd student-management-project
```

 2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the project
```bash
python main.py
```

Make sure the CSV file and required automation configuration are available before running the project.

Automation
The GitHub Actions workflow can execute the Python analysis in a cloud environment. The program sends the required data to the configured Make.com webhook, which handles the email automation.

Configure your webhook securely using GitHub Secrets or environment variables. Do not publish private webhook URLs, email credentials, or API keys in the repository.

Learning Outcomes
- Python file handling and data processing
- Working with CSV data using Pandas
- Automating repetitive tasks
- Integrating Python with webhooks and external services
- Creating GitHub Actions workflows
- Generating reports programmatically

Future Improvements
- Add a web dashboard to view student performance.
- Store student records in a database.
- Add performance charts and visualizations.
- Build a FastAPI backend for managing student records.
- Add authentication and role-based access.

Author
Naveen Kumar M.

GitHub: https://github.com/naveenkumar00875
