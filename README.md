 <sup></sup><sub>----------------------------------------------- Print("Hello The Internet!") ------------------------------------------------------------------</sub>

### <ins>***Table of Content***</ins>
   ###### [- Intro - About Me](#Intro_AboutMe)
   ###### [- Projects Menu](#Project_Menu)


### <ins>***Intro_AboutMe***</ins>
  Hello! I’m Tweet, a Computer Science graduate from 2024 with a deep passion for software development. This portfolio showcases the projects and practices that have helped me grow as a developer, reflecting my continuous journey in exploring and learning new technologies. I’m always eager to tackle new challenges and refine my skills through hands-on experience. The projects you’ll find here are a testament to my commitment to growth and innovation, and my dedication to staying current with industry best practices. I’m excited to continue evolving as a developer, and I look forward to further expanding my knowledge and expertise.

  
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### <ins>***Project_Menu***</ins>
###### [- Job Tracker](#Job_Tracker)
###### [- Dog Zommie Toy](#Dog_Zommie_Toy)


**Job_Tracker**
* **Functional Requirements**
  - This program provides a user-friendly Graphical User Interface (GUI) for managing job applications efficiently. It features a Treeview widget to display a table of job applications, along with input fields for adding new entries. Users can perform CRUD (Create, Read, Update, Delete) operations using buttons to add, update, delete, and search for applications based on job name or company name. The program interacts with a database to store job application details, including job name, company name, applied date, resume used, and additional notes. To enhance usability, it arranges widgets using .pack() and .grid(), includes a scrollbar for easy navigation, supports multiline text for job details, and can be converted into an executable file using PyInstaller for wider accessibility.
      
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

 <sup></sup><sub>[To the project -](https://github.com/TweetTran/Tweet_Projects/tree/main/Job%20Tracker%20Project)</sub>
 <sup></sup><sub>[Back to Menu -](#Project_Menu)</sub>
 <sup></sup><sub>[Reference: Codemy.com](https://www.youtube.com/@Codemycom)</sub>

### **Zommie_Dog_Toy**
This project is called Zoomie_Dog_Toy. The robot operates using an Arduino Uno and a single motor to pull a string that is stretched between five checkpoints placed on the ground.
The first checkpoint, known as the Base, houses the Arduino board, motor controller, motor, and battery.
The remaining checkpoints serve as anchor points to guide the string.
The last checkpoint loops back to the Base, forming a continuous string loop.
The motor is attached to the string and rotates clockwise to unwind the string and counterclockwise to recoil it. It operates at random speeds and directions, creating unpredictable movement.
The machine is activated by pressing a button and continues running until the button is pressed again to stop it.

* **Functional Requirements**
The robot must activate when the button is pressed.
The motor must pull the string in a loop between five checkpoints.
The string must unwind (clockwise) and recoil (counterclockwise) based on motor direction.
The motor must operate at random speeds and directions.
The system must stop when the button is pressed again.
The string must remain taut as it loops through the checkpoints.

* **Non-Functional Requirements**
The robot must be portable and lightweight.
The system must operate reliably for at least 2 hours on battery power.
The motor’s operation should generate minimal noise (≤ 50 dB).
The activation and deactivation button must have a response time of less than 1 second.
The structure must withstand repeated operations without significant wear for at least 1 year.

* **Technical Requirements**
The Arduino Uno must support motor control and button input functionality.
A motor controller capable of bi-directional rotation must be used.
The system must ensure the string loop remains secure and tensioned.
Randomized motor speed and direction must be controlled programmatically.
The checkpoints must be spaced precisely to allow smooth string movement.

* **Hardware Requirements**
Arduino Uno: To control the system logic.
Motor: A DC motor with sufficient torque to pull the string through all checkpoints.
Motor Controller: To manage motor direction and speed.
Button: For system activation and deactivation.
Battery: A rechargeable battery pack capable of powering the system.
String: Durable and flexible material to create a loop between checkpoints.
Checkpoints: Anchors or pulleys to guide the string loop.

* **Software Requirements**
Arduino IDE: To program and upload the control logic.
Randomization Algorithm: To determine motor speed and direction.
Motor Control Code: To manage the clockwise and counterclockwise motion.
Button Control Logic: To handle start/stop functionality.

* **User Requirements**
The user must be able to start and stop the robot using a single button.
The system should be intuitive and require minimal setup or technical knowledge.
The checkpoints should be easy to assemble and securely anchor the string.
Users should receive clear instructions for replacing or recharging the battery.

 <sup></sup><sub>[To the project -](https://github.com/TweetTran/Tweet_Projects/tree/main/Job%20Tracker%20Project)</sub>
 <sup></sup><sub>[Back to Menu -](#Project_Menu)</sub>
 <sup></sup><sub>[Reference: POPRHINO , ](https://www.wayfair.com/pet/pdp/poprhino-remote-control-pet-chase-toy-for-outdoor-exercise-training-suitable-for-dogs-pprh1035.html)</sub> 
 <sup></sup><sub>[Generic , ](https://www.amazon.com/Generic-Treadmill-Continuous-Backyard-Electric/dp/B0D9DJ76HB/ref=asc_df_B0D9DJ76HB?mcid=4ac98acad49133a795ebdc98ec5c1b75&tag=hyprod-20&linkCode=df0&hvadid=697654782231&hvpos=&hvnetw=g&hvrand=2403657064496655038&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9016168&hvtargid=pla-2336352648465&psc=1)</sub>
 <sup></sup><sub>[SwiftPaws](https://www.amazon.com/SwiftPaws-Original-Controlled-Interactive-Enrichment/dp/B08L82BYPX/ref=pd_ci_mcx_pspc_dp_2_t_3?pd_rd_w=ayaMW&content-id=amzn1.sym.cd152278-debd-42b9-91b9-6f271389fda7&pf_rd_p=cd152278-debd-42b9-91b9-6f271389fda7&pf_rd_r=1VW3FMEGQ5YH15JT7AK4&pd_rd_wg=Xnnth&pd_rd_r=503c8d0e-f486-404d-90a1-5583d4a48209&pd_rd_i=B08L82BYPX)</sub>
 
