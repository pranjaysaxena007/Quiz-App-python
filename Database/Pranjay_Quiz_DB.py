import mysql.connector
import random

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='ps',
        password='Harsh@mysql',
        database='Quiz',
        ssl_disabled=True
    )

conn = connect_db()
cursor = conn.cursor()

queries = [
    '''CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    uname VARCHAR(100) UNIQUE NOT NULL,
    pwd VARCHAR(20) NOT NULL
    );''',

    '''CREATE TABLE IF NOT EXISTS pyques(
    ques VARCHAR(300) NOT NULL,
    opt1 VARCHAR(100),
    opt2 VARCHAR(100),
    opt3 VARCHAR(100),
    opt4 VARCHAR(100),
    ans CHAR(1)
    );''',

    '''CREATE TABLE IF NOT EXISTS aiques(
    ques VARCHAR(300) NOT NULL,
    opt1 VARCHAR(100),
    opt2 VARCHAR(100),
    opt3 VARCHAR(100),
    opt4 VARCHAR(100),
    ans CHAR(1)
    );''',

    '''CREATE TABLE IF NOT EXISTS dbques(
    ques VARCHAR(300) NOT NULL,
    opt1 VARCHAR(100),
    opt2 VARCHAR(100),
    opt3 VARCHAR(100),
    opt4 VARCHAR(100),
    ans CHAR(1)
    );''',
    '''
    CREATE TABLE IF NOT EXISTS results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    category VARCHAR(20),
    score INT
    );''',

    '''
    TRUNCATE TABLE pyques;
    ''',
    '''
    TRUNCATE TABLE aiques;
    ''',
    '''
    TRUNCATE TABLE dbques;
    ''',

    '''
    INSERT INTO pyques (ques, opt1, opt2, opt3, opt4, ans)
    VALUES
    ('What is the correct file extension for Python files?', 'A) .pt', 'B) .py', 'C) .pyt', 'D) .python', 'B'),
    ('Which of the following is a valid Python variable name?', 'A) 2myvar', 'B) my-var', 'C) my_var', 'D) my var', 'C'),
    ('Which function is used to output text to the screen in Python?', 'A) display()', 'B) print()', 'C) echo()', 'D) printf()', 'B'),
    ('How do you start a comment in Python?', 'A) //', 'B) #', 'C) <!--', 'D) /*', 'B'),
    ('Which collection type is ordered and changeable?', 'A) Tuple', 'B) Set', 'C) Dictionary', 'D) List', 'D'),
    ('Which operator is used for exponentiation (power) in Python?', 'A) ^', 'B) **', 'C) //', 'D) %', 'B'),
    ('Which keyword is used to create a function in Python?', 'A) define', 'B) function', 'C) def', 'D) fun', 'C'),
    ('What will len([1, 2, 3]) return?', 'A) 1', 'B) 2', 'C) 3', 'D) 4', 'C'),
    ('What data type is the object below? x = {name: John, age: 25}', 'A) Dictionary', 'B) List', 'C) Tuple', 'D) Set', 'A'),
    ('What is the output of 2 + 3 * 4?', 'A) 20', 'B) 14', 'C) 24', 'D) 18', 'B'),
    ('How do you insert an element at the end of a list?', 'A) insert()', 'B) append()', 'C) extend()', 'D) add()', 'B'),
    ('Which of the following is used to define a block of code in Python?', 'A) Parentheses', 'B) Curly braces', 'C) Indentation', 'D) Quotation marks', 'C'),
    ('How do you create a dictionary?', 'A) d = {}', 'B) d = []', 'C) d = ()', 'D) d = set()', 'A'),
    ('What is the result of 10 // 3 in Python?', 'A) 3.33', 'B) 3', 'C) 10', 'D) 1', 'B'),
    ('How do you check the type of a variable in Python?', 'A) checktype()', 'B) type()', 'C) isinstance()', 'D) typeof()', 'B'),
    ('What will be the output of bool([])?', 'A) True', 'B) False', 'C) None', 'D) Error', 'B'),
    ('What is the correct way to import a module in Python?', 'A) import module', 'B) import(module)', 'C) include module', 'D) using module', 'A'),
    ('Which of the following will raise an error?', 'A) x = 1/0', 'B) x = int(10)', 'C) x = 2 + 3', 'D) x = float(10.5)', 'A'),
    ('Which of the following is NOT a keyword in Python?', 'A) lambda', 'B) pass', 'C) eval', 'D) assert', 'C'),
    ('What does list(range(5)) return?', 'A) [1, 2, 3, 4, 5]', 'B) [0, 1, 2, 3, 4, 5]', 'C) [0, 1, 2, 3, 4]', 'D) [1, 2, 3, 4]', 'C');
    ''',

    '''
    INSERT INTO aiques (ques, opt1, opt2, opt3, opt4, ans)
    VALUES
    ('What does AI stand for?', 'A) Artificial Integration', 'B) Automated Intelligence', 'C) Artificial Intelligence', 'D) Advanced Intelligence', 'C'),
    ('Which of the following is NOT a type of machine learning?', 'A) Supervised learning', 'B) Unsupervised learning', 'C) Reinforcement learning', 'D) Integrated learning', 'D'),
    ('Who is considered the father of Artificial Intelligence?', 'A) Alan Turing', 'B) Elon Musk', 'C) John McCarthy', 'D) Marvin Minsky', 'C'),
    ('Which term refers to the ability of an AI to mimic human thought processes?', 'A) Machine learning', 'B) Cognitive computing', 'C) Neural networks', 'D) Natural language processing', 'B'),
    ('What is the main goal of supervised learning?', 'A) To find hidden patterns in data', 'B) To classify labeled data', 'C) To reinforce positive behavior', 'D) To predict future trends based on time series', 'B'),
    ('What is the process of training a model using labeled data called?', 'A) Reinforcement learning', 'B) Clustering', 'C) Supervised learning', 'D) Dimensionality reduction', 'C'),
    ('Which algorithm is widely used in AI to find optimal solutions by simulating natural evolution?', 'A) Genetic Algorithm', 'B) Decision Trees', 'C) Neural Networks', 'D) Bayesian Networks', 'A'),
    ('Which of the following is an example of a classification algorithm?', 'A) K-means', 'B) Linear Regression', 'C) Decision Tree', 'D) Principal Component Analysis', 'C'),
    ('What is the term used for the ability of an AI system to understand and process human language?', 'A) Cognitive Computing', 'B) Neural Networks', 'C) Natural Language Processing', 'D) Machine Learning', 'C'),
    ('Which of the following is a measure of how well a machine learning model generalizes to unseen data?', 'A) Accuracy', 'B) Overfitting', 'C) Precision', 'D) Generalization', 'D'),
    ('Which type of AI is specifically designed to perform one task?', 'A) Narrow AI', 'B) General AI', 'C) Super AI', 'D) Autonomous AI', 'A'),
    ('In Reinforcement Learning, what does the agent try to maximize?', 'A) Error', 'B) Loss', 'C) Reward', 'D) Uncertainty', 'C'),
    ('Which algorithm is used to reduce the dimensionality of large datasets?', 'A) Linear Regression', 'B) K-Nearest Neighbors', 'C) Principal Component Analysis', 'D) Random Forest', 'C'),
    ('What is a neural network composed of?', 'A) Neurons', 'B) Trees', 'C) Graphs', 'D) Layers', 'D'),
    ('What is overfitting in machine learning?', 'A) When the model performs poorly on training data', 'B) When the model generalizes well on unseen data', 'C) When the model memorizes training data', 'D) When the model ignores the training data', 'C'),
    ('Which AI technique allows the model to learn from past actions and decisions?', 'A) Unsupervised Learning', 'B) Supervised Learning', 'C) Reinforcement Learning', 'D) Transfer Learning', 'C'),
    ('What is the full form of NLP in AI?', 'A) Neural Learning Process', 'B) Natural Learning Processing', 'C) Neural Language Programming', 'D) Natural Language Processing', 'D'),
    ('Which of the following is NOT a type of neural network?', 'A) Recurrent Neural Networks', 'B) Convolutional Neural Networks', 'C) Generative Adversarial Networks', 'D) Gradient Boosting Networks', 'D'),
    ('Which of these is commonly used to handle missing data in machine learning models?', 'A) Drop the missing data', 'B) Use default value', 'C) Impute missing values', 'D) All of the above', 'D'),
    ('Which is a common evaluation metric for classification problems?', 'A) Precision', 'B) Mean Squared Error', 'C) Gradient Descent', 'D) Variance', 'A');
    ''',

    '''
    INSERT INTO dbques (ques, opt1, opt2, opt3, opt4, ans)
    VALUES
    ('What does SQL stand for?', 'A) Structured Query Language', 'B) Standard Query Language', 'C) Simple Query Language', 'D) Sequential Query Language', 'A'),
    ('What of the following is NOT a type of database model?', 'A) Hierarchical', 'B) Relational', 'C) Network', 'D) Cloud', 'D'),
    ('What type of key is used to uniquely identify a record in a table?', 'A) Foreign Key', 'B) Candidate Key', 'C) Primary Key', 'D) Composite Key', 'C'),
    ('Which command is used to retrieve data from a database?', 'A) SELECT', 'B) INSERT', 'C) UPDATE', 'D) DELETE', 'A'),
    ('Which SQL keyword is used to sort the result-set?', 'A) SORT BY', 'B) ORDER BY', 'C) GROUP BY', 'D) SORT', 'B'),
    ('Which SQL statement is used to delete data from a database?', 'A) REMOVE', 'B) DELETE', 'C) ERASE', 'D) DROP', 'B'),
    ('What is a foreign key?', 'A) A key that uniquely identifies a record', 'B) A key that links two tables', 'C) A key that enforces referential integrity', 'D) Both B and C', 'D'),
    ('Which of the following is a NoSQL database?', 'A) MySQL', 'B) PostgreSQL', 'C) MongoDB', 'D) Oracle', 'C'),
    ('Which command is used to add new rows to a table?', 'A) INSERT INTO', 'B) ADD ROW', 'C) ADD TO', 'D) INSERT ROW', 'A'),
    ('What is normalization in databases?', 'A) Increasing data redundancy', 'B) Minimizing data redundancy', 'C) Increasing database size', 'D) Optimizing query performance', 'B'),
    ('Which of the following is a DDL (Data Definition Language) command?', 'A) INSERT', 'B) UPDATE', 'C) ALTER', 'D) SELECT', 'C'),
    ('Which of the following is an aggregate function in SQL?', 'A) COUNT()', 'B) LENGTH()', 'C) LEFT()', 'D) CONVERT()', 'A'),
    ('What is a view in SQL?', 'A) A stored procedure', 'B) A virtual table based on the result of a SELECT query', 'C) A real table storing data', 'D) A key in a database', 'B'),
    ('Which of the following constraints ensures that a column cannot have a NULL value?', 'A) PRIMARY KEY', 'B) UNIQUE', 'C) NOT NULL', 'D) FOREIGN KEY', 'C'),
    ('Which command is used to change the structure of an existing table?', 'A) MODIFY', 'B) CHANGE', 'C) ALTER', 'D) UPDATE', 'C'),
    ('Which SQL clause is used to group rows with the same values into summary rows?', 'A) GROUP BY', 'B) ORDER BY', 'C) HAVING', 'D) SUM', 'A'),
    ('In which normal form is a table when it has no transitive dependencies?', 'A) First Normal Form (1NF)', 'B) Second Normal Form (2NF)', 'C) Third Normal Form (3NF)', 'D) Boyce-Codd Normal Form (BCNF)', 'C'),
    ('Which of the following SQL statements is used to update existing data in a table?', 'A) UPDATE', 'B) INSERT', 'C) MODIFY', 'D) CHANGE', 'A'),
    ('Which of the following refers to a column in one table that points to the primary key in another table?', 'A) Foreign Key', 'B) Primary Key', 'C) Unique Key', 'D) Composite Key', 'A'),
    ('Which SQL function is used to return the smallest value from a set of values?', 'A) MAX()', 'B) MIN()', 'C) LEAST()', 'D) LOW()', 'B');
    '''
]
for query in queries:
    cursor.execute(query)

conn.commit()
conn.close()

def register():
    conn = connect_db()
    cursor = conn.cursor()
    username = input("Enter a username: ")

    cursor.execute("SELECT * FROM users WHERE uname = %s", (username,))
    if cursor.fetchone():
        print("Username already exists. Try another.")
        return

    while True:
        pwd = input("Enter a password: ")
        if 8 <= len(pwd) <= 20 and any(c.islower() for c in pwd) and \
                any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and \
                any(c in '@#%_!.' for c in pwd):
            cursor.execute("INSERT INTO users (uname, pwd) VALUES (%s, %s)", (username, pwd))
            conn.commit()
            print("Registration successful!")
            break
        else:
            print("Password must contain one uppercase, one lowercase, one number, and one special character.")

    conn.close()


def login():
    conn = connect_db()
    cursor = conn.cursor()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM users WHERE uname = %s AND pwd = %s", (username, password))
    if cursor.fetchone():
        print("Login successful!")
        conn.close()
        return username
    else:
        print("Invalid username or password.")
        conn.close()
        return None


def get_questions(category):
    conn = connect_db()
    cursor = conn.cursor()

    table_map = {'Python': 'pyques', 'AI': 'aiques', 'Database': 'dbques'}
    table_name = table_map.get(category)

    cursor.execute(f"SELECT ques, opt1, opt2, opt3, opt4, ans FROM {table_name}")
    questions = []
    for ques, opt1, opt2, opt3, opt4, ans in cursor.fetchall():
        questions.append({
            'question': ques,
            'choices': [f"A) {opt1}", f"B) {opt2}", f"C) {opt3}", f"D) {opt4}"],
            'answer': ans
        })

    conn.close()
    return questions


def save_result(username, category, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (username, category, score) VALUES (%s, %s, %s)", (username, category, score))
    conn.commit()
    conn.close()


def show_result_history(username):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT category, score FROM results WHERE username = %s", (username,))
    results = cursor.fetchall()

    if results:
        print(f"\nQuiz History for {username}:")
        for category, score in results:
            print(f"Quiz: {category} - Score: {score}")
    else:
        print("No history found.")

    conn.close()


def quiz(username):
    while True:
        print("\nWhich quiz would you like to attempt?")
        print("A) Python\nB) AI\nC) Database\nD) Exit")
        ch = input("Enter a choice: ").upper()
        category_map = {'A': 'Python', 'B': 'AI', 'C': 'Database'}

        if ch in category_map:
            category = category_map[ch]
            questions = get_questions(category)

            random.shuffle(questions)
            score = 0

            for idx, question in enumerate(questions[:5], start=1):
                print(f"\nQ{idx}: {question['question']}")
                for choice in question['choices']:
                    print(choice)
                user_answer = input("Enter your answer: ").upper()

                if user_answer == question['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {question['answer']}.")

            print(f"\nResult: {score} out of 5.")
            save_result(username, category, score)
            show_result_history(username)
        elif ch == 'D':
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    response = input("Are you already registered? (yes/no): ").strip().lower()

    if response == 'no':
        register()

    while True:
        username = login()
        if username:
            quiz(username)
            break
        else:
            print("Retry login or register.")


main()