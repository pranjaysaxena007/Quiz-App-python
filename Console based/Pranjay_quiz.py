'''
questions,registered,login,result -> store in separate files
create function -> show result history
'''

python_quiz_questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "choices": ["A) .pt", "B) .py", "C) .pyt", "D) .python"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a valid Python variable name?",
        "choices": ["A) 2myvar", "B) my-var", "C) my_var", "D) my var"],
        "answer": "C"
    },
    {
        "question": "Which function is used to output text to the screen in Python?",
        "choices": ["A) display()", "B) print()", "C) echo()", "D) printf()"],
        "answer": "B"
    },
    {
        "question": "How do you start a comment in Python?",
        "choices": ["A) //", "B) #", "C) <!--", "D) /*"],
        "answer": "B"
    },
    {
        "question": "Which collection type is ordered and changeable?",
        "choices": ["A) Tuple", "B) Set", "C) Dictionary", "D) List"],
        "answer": "D"
    },
    {
        "question": "Which operator is used for exponentiation (power) in Python?",
        "choices": ["A) ^", "B) **", "C) //", "D) %"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "choices": ["A) define", "B) function", "C) def", "D) fun"],
        "answer": "C"
    },
    {
        "question": "What will `len([1, 2, 3])` return?",
        "choices": ["A) 1", "B) 2", "C) 3", "D) 4"],
        "answer": "C"
    },
    {
        "question": "What data type is the object below?\n`x = {'name': 'John', 'age': 25}`",
        "choices": ["A) Dictionary", "B) List", "C) Tuple", "D) Set"],
        "answer": "A"
    },
    {
        "question": "What is the output of `2 + 3 * 4`?",
        "choices": ["A) 20", "B) 14", "C) 24", "D) 18"],
        "answer": "B"
    },
    {
        "question": "How do you insert an element at the end of a list?",
        "choices": ["A) insert()", "B) append()", "C) extend()", "D) add()"],
        "answer": "B"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "choices": ["A) Parentheses", "B) Curly braces", "C) Indentation", "D) Quotation marks"],
        "answer": "C"
    },
    {
        "question": "How do you create a dictionary?",
        "choices": ["A) d = {}", "B) d = []", "C) d = ()", "D) d = set()"],
        "answer": "A"
    },
    {
        "question": "What is the result of `10 // 3` in Python?",
        "choices": ["A) 3.33", "B) 3", "C) 10", "D) 1"],
        "answer": "B"
    },
    {
        "question": "How do you check the type of a variable in Python?",
        "choices": ["A) checktype()", "B) type()", "C) isinstance()", "D) typeof()"],
        "answer": "B"
    },
    {
        "question": "What will be the output of `bool([])`?",
        "choices": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "B"
    },
    {
        "question": "What is the correct way to import a module in Python?",
        "choices": ["A) import module", "B) import(module)", "C) include module", "D) using module"],
        "answer": "A"
    },
    {
        "question": "Which of the following will raise an error?",
        "choices": ["A) x = 1/0", "B) x = int('10')", "C) x = '2' + '3'", "D) x = float('10.5')"],
        "answer": "A"
    },
    {
        "question": "Which of the following is NOT a keyword in Python?",
        "choices": ["A) lambda", "B) pass", "C) eval", "D) assert"],
        "answer": "C"
    },
    {
        "question": "What does `list(range(5))` return?",
        "choices": ["A) [1, 2, 3, 4, 5]", "B) [0, 1, 2, 3, 4, 5]", "C) [0, 1, 2, 3, 4]", "D) [1, 2, 3, 4]"],
        "answer": "C"
    }
]
ai_quiz_questions = [
    {
        "question": "What does AI stand for?",
        "choices": ["A) Artificial Integration", "B) Automated Intelligence", "C) Artificial Intelligence", "D) Advanced Intelligence"],
        "answer": "C"
    },
    {
        "question": "Which of the following is NOT a type of machine learning?",
        "choices": ["A) Supervised learning", "B) Unsupervised learning", "C) Reinforcement learning", "D) Integrated learning"],
        "answer": "D"
    },
    {
        "question": "Who is considered the father of Artificial Intelligence?",
        "choices": ["A) Alan Turing", "B) Elon Musk", "C) John McCarthy", "D) Marvin Minsky"],
        "answer": "C"
    },
    {
        "question": "Which term refers to the ability of an AI to mimic human thought processes?",
        "choices": ["A) Machine learning", "B) Cognitive computing", "C) Neural networks", "D) Natural language processing"],
        "answer": "B"
    },
    {
        "question": "What is the main goal of supervised learning?",
        "choices": ["A) To find hidden patterns in data", "B) To classify labeled data", "C) To reinforce positive behavior", "D) To predict future trends based on time series"],
        "answer": "B"
    },
    {
        "question": "What is the process of training a model using labeled data called?",
        "choices": ["A) Reinforcement learning", "B) Clustering", "C) Supervised learning", "D) Dimensionality reduction"],
        "answer": "C"
    },
    {
        "question": "Which algorithm is widely used in AI to find optimal solutions by simulating natural evolution?",
        "choices": ["A) Genetic Algorithm", "B) Decision Trees", "C) Neural Networks", "D) Bayesian Networks"],
        "answer": "A"
    },
    {
        "question": "Which of the following is an example of a classification algorithm?",
        "choices": ["A) K-means", "B) Linear Regression", "C) Decision Tree", "D) Principal Component Analysis"],
        "answer": "C"
    },
    {
        "question": "What is the term used for the ability of an AI system to understand and process human language?",
        "choices": ["A) Cognitive Computing", "B) Neural Networks", "C) Natural Language Processing", "D) Machine Learning"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a measure of how well a machine learning model generalizes to unseen data?",
        "choices": ["A) Accuracy", "B) Overfitting", "C) Precision", "D) Generalization"],
        "answer": "D"
    },
    {
        "question": "Which type of AI is specifically designed to perform one task?",
        "choices": ["A) Narrow AI", "B) General AI", "C) Super AI", "D) Autonomous AI"],
        "answer": "A"
    },
    {
        "question": "In Reinforcement Learning, what does the agent try to maximize?",
        "choices": ["A) Error", "B) Loss", "C) Reward", "D) Uncertainty"],
        "answer": "C"
    },
    {
        "question": "Which algorithm is used to reduce the dimensionality of large datasets?",
        "choices": ["A) Linear Regression", "B) K-Nearest Neighbors", "C) Principal Component Analysis", "D) Random Forest"],
        "answer": "C"
    },
    {
        "question": "What is a neural network composed of?",
        "choices": ["A) Neurons", "B) Trees", "C) Graphs", "D) Layers"],
        "answer": "D"
    },
    {
        "question": "What is overfitting in machine learning?",
        "choices": ["A) When the model performs poorly on training data", "B) When the model generalizes well on unseen data", "C) When the model memorizes training data", "D) When the model ignores the training data"],
        "answer": "C"
    },
    {
        "question": "Which AI technique allows the model to learn from past actions and decisions?",
        "choices": ["A) Unsupervised Learning", "B) Supervised Learning", "C) Reinforcement Learning", "D) Transfer Learning"],
        "answer": "C"
    },
    {
        "question": "What is the full form of NLP in AI?",
        "choices": ["A) Neural Learning Process", "B) Natural Learning Processing", "C) Neural Language Programming", "D) Natural Language Processing"],
        "answer": "D"
    },
    {
        "question": "Which of the following is NOT a type of neural network?",
        "choices": ["A) Recurrent Neural Networks", "B) Convolutional Neural Networks", "C) Generative Adversarial Networks", "D) Gradient Boosting Networks"],
        "answer": "D"
    },
    {
        "question": "Which of these is commonly used to handle missing data in machine learning models?",
        "choices": ["A) Drop the missing data", "B) Use default value", "C) Impute missing values", "D) All of the above"],
        "answer": "D"
    },
    {
        "question": "Which is a common evaluation metric for classification problems?",
        "choices": ["A) Precision", "B) Mean Squared Error", "C) Gradient Descent", "D) Variance"],
        "answer": "A"
    }
]
db_quiz_questions = [
    {
        "question": "What does SQL stand for?",
        "choices": ["A) Structured Query Language", "B) Standard Query Language", "C) Simple Query Language", "D) Sequential Query Language"],
        "answer": "A"
    },
    {
        "question": "Which of the following is NOT a type of database model?",
        "choices": ["A) Hierarchical", "B) Relational", "C) Network", "D) Cloud"],
        "answer": "D"
    },
    {
        "question": "What type of key is used to uniquely identify a record in a table?",
        "choices": ["A) Foreign Key", "B) Candidate Key", "C) Primary Key", "D) Composite Key"],
        "answer": "C"
    },
    {
        "question": "Which command is used to retrieve data from a database?",
        "choices": ["A) SELECT", "B) INSERT", "C) UPDATE", "D) DELETE"],
        "answer": "A"
    },
    {
        "question": "Which SQL keyword is used to sort the result-set?",
        "choices": ["A) SORT BY", "B) ORDER BY", "C) GROUP BY", "D) SORT"],
        "answer": "B"
    },
    {
        "question": "Which SQL statement is used to delete data from a database?",
        "choices": ["A) REMOVE", "B) DELETE", "C) ERASE", "D) DROP"],
        "answer": "B"
    },
    {
        "question": "What is a foreign key?",
        "choices": ["A) A key that uniquely identifies a record", "B) A key that links two tables", "C) A key that enforces referential integrity", "D) Both B and C"],
        "answer": "D"
    },
    {
        "question": "Which of the following is a NoSQL database?",
        "choices": ["A) MySQL", "B) PostgreSQL", "C) MongoDB", "D) Oracle"],
        "answer": "C"
    },
    {
        "question": "Which command is used to add new rows to a table?",
        "choices": ["A) INSERT INTO", "B) ADD ROW", "C) ADD TO", "D) INSERT ROW"],
        "answer": "A"
    },
    {
        "question": "What is normalization in databases?",
        "choices": ["A) Increasing data redundancy", "B) Minimizing data redundancy", "C) Increasing database size", "D) Optimizing query performance"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a DDL (Data Definition Language) command?",
        "choices": ["A) INSERT", "B) UPDATE", "C) ALTER", "D) SELECT"],
        "answer": "C"
    },
    {
        "question": "Which of the following is an aggregate function in SQL?",
        "choices": ["A) COUNT()", "B) LENGTH()", "C) LEFT()", "D) CONVERT()"],
        "answer": "A"
    },
    {
        "question": "What is a view in SQL?",
        "choices": ["A) A stored procedure", "B) A virtual table based on the result of a SELECT query", "C) A real table storing data", "D) A key in a database"],
        "answer": "B"
    },
    {
        "question": "Which of the following constraints ensures that a column cannot have a NULL value?",
        "choices": ["A) PRIMARY KEY", "B) UNIQUE", "C) NOT NULL", "D) FOREIGN KEY"],
        "answer": "C"
    },
    {
        "question": "Which command is used to change the structure of an existing table?",
        "choices": ["A) MODIFY", "B) CHANGE", "C) ALTER", "D) UPDATE"],
        "answer": "C"
    },
    {
        "question": "Which SQL clause is used to group rows with the same values into summary rows?",
        "choices": ["A) GROUP BY", "B) ORDER BY", "C) HAVING", "D) SUM"],
        "answer": "A"
    },
    {
        "question": "In which normal form is a table when it has no transitive dependencies?",
        "choices": ["A) First Normal Form (1NF)", "B) Second Normal Form (2NF)", "C) Third Normal Form (3NF)", "D) Boyce-Codd Normal Form (BCNF)"],
        "answer": "C"
    },
    {
        "question": "Which of the following SQL statements is used to update existing data in a table?",
        "choices": ["A) UPDATE", "B) INSERT", "C) MODIFY", "D) CHANGE"],
        "answer": "A"
    },
    {
        "question": "Which of the following refers to a column in one table that points to the primary key in another table?",
        "choices": ["A) Foreign Key", "B) Primary Key", "C) Unique Key", "D) Composite Key"],
        "answer": "A"
    },
    {
        "question": "Which SQL function is used to return the smallest value from a set of values?",
        "choices": ["A) MAX()", "B) MIN()", "C) LEAST()", "D) LOW()"],
        "answer": "B"
    }
]

import random

users = {}
# Registration function
def register():
    while True:
        username = input("Enter a username:")
        if username in users:
            print("Username already exists. Try another.")
        else:
            # Checking for correct syntax password entry
            while (True):
                length = False
                lower = False
                upper = False
                digit = False
                special = False
                pwd = input("Enter a password:")
                if (len(pwd) > 8 or len(pwd) < 20):
                    length = True
                for i in pwd:
                    if (i.islower()):
                        lower = True
                    elif (i.isupper()):
                        upper = True
                    elif (i.isdigit()):
                        digit = True
                    elif (i in '@#%_!.'):
                        special = True
                if length and lower and upper and digit and special:
                    break
                else:
                    print("Retry! Password must contain: \nOne Capital letter\nOne small letter \nOne number\nOne special character")
                    continue
            users[username] = pwd
            print("Registration successful!")
            break
    return True

# Login function
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def quiz():
    #Choice for user
    print("Which quiz you wanna attempt:")
    print("A) Python\nB) AI\nC) DataBase")
    ch = input("Enter a choice:").upper()
    while(True):
        flag = 0
        count = 0
        if(ch == 'A'):
            random.shuffle(python_quiz_questions)
            for question in python_quiz_questions:
                print(question["question"])
                flag += 1
                for choice in question["choices"]:
                    print(choice)
                user_answer = input("Enter your answer: ").upper()
                if user_answer[0] == question["answer"]:
                    print("Correct!")
                    count += 1
                else:
                    print(f"Wrong! The correct option is {question['answer']}.")
                if(flag == 5):
                    break
            break
        elif(ch == 'B'):
            random.shuffle(ai_quiz_questions)
            for question in ai_quiz_questions:
                print(question["question"])
                flag += 1
                for choice in question["choices"]:
                    print(choice)
                user_answer = input("Enter your answer: ").upper()
                if user_answer[0] == question["answer"]:
                    print("Correct!")
                    count += 1
                else:
                    print(f"Wrong! The correct option is {question['answer']}.")
                if (flag == 5):
                    break
            break
        elif(ch == 'C'):
            random.shuffle(db_quiz_questions)
            for question in db_quiz_questions:
                print(question["question"])
                flag += 1
                for choice in question["choices"]:
                    print(choice)
                user_answer = input("Enter your answer: ").upper()
                if user_answer[0] == question["answer"]:
                    print("Correct!")
                    count += 1
                else:
                    print(f"Wrong! The correct answer is {question['answer']}.")
                if (flag == 5):
                    break
            break
        else:
            print("Invalid Choice")
    print(f"\nResult: {count} out of 5.")
    return True

#Calling Different functins
r = register()
while (True):
    if r == True:
        l = login()
        if l != None:
            quiz()
            break
        else:
            print('Retry!')
            continue