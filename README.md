 <sup></sup><sub>Print("Hello World!")</sub>

### <ins>***Table of Content***</ins>
   - [Intro - About Me](#Intro_AboutMe)
   - [Projects Menu](#Project_Menu)


### <ins>***Intro_AboutMe***</ins>
  Hello! I’m Tweet, a Computer Science graduate from 2024 with a deep passion for software development. This portfolio showcases the projects and practices that have helped me grow as a developer, reflecting my continuous journey in exploring and learning new technologies. I’m always eager to tackle new challenges and refine my skills through hands-on experience. The projects you’ll find here are a testament to my commitment to growth and innovation, and my dedication to staying current with industry best practices. I’m excited to continue evolving as a developer, and I look forward to further expanding my knowledge and expertise.

  
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### <ins>***Project_Menu***</ins>
* [Job Tracker](#Job_Tracker)
* [Dog Zommie Toy](#Dog_Zommie_Toy)


**Job_Tracker**
* **Technical Specifications**
  - Software:
    - Python (Primary programming language),
    - Tkinter (GUI library for interface),
    - SQL (Structured Query Language),
    - SQLite (Database for storing job application records),
    - PyInstaller (For converting the script into an executable program).
  - Hardware:
    - Windows/macOS/Linux PC with Python installed,
    - Sufficient RAM and storage for running a GUI application,
    - Keyboard and mouse for user interaction.
  - Technical Needs:
    - Python 3.x installed,
    - Required libraries: tkinter, sqlite3, pyinstaller.

* **Functional Requirements**
  - User Interface (GUI):
    - Display a table of job applications in a Treeview widget
    - Provide input fields for adding new applications
    - Include buttons for adding, updating, deleting, and searching (CRUD)
  - Database Operations:
    - Store job applications with fields: ID, Job Name, Company Name, Applied Date, Resume Used, Details
    - Allow inserting new job applications
    - Enable updating and deleting existing records
    - Support searching by Job Name or Company Name
  - Application Features:
    - Arrange widgets using .pack() and .grid()
    - Use a scrollbar to navigate application records
    - Handle multiline text for job details using Text
    - Convert the application into an executable with pyinstaller


* **Data Requirements:**
  - Stored Data:
    - Job Applications Table (applications)
      - id: Integer (Unique identifier)
      - job_name: Text (Job title)
      - company_name: Text (Company name)
      - applied_date: Text (Date format)
      - resume_used: Text (File reference or resume version)
      - detail: Text (Multiline description)
  - Data Processing:
    - Insert new job records when the user submits a form
    - Update an existing record based on ID
    - Delete records individually or in bulk
    - Search for applications based on job name or company name
  - Data Exchange:
    - Data is retrieved from the SQLite database using SQL queries
    - The Treeview widget dynamically updates to display data
    - get_children() is used to retrieve all records for updating the UI
      
* To the project: [Job Tracker](https://github.com/TweetTran/Tweet_Projects/tree/main/Job%20Tracker%20Project)
* [Projects Menu](#Project_Menu)

### **Dog_Zommie_Toy**
* **Technical Specifications:**
* **Functional Requirements:**
* **Data Requirements:**
