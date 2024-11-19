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
file1 = open("pyques.txt", "w")
for i in python_quiz_questions:
    q = i["question"]
    c = "\n".join(i["choices"])  # Join choices into a single string
    a = i["answer"]
    file1.write(f"{q}\n{c}\nAnswer: {a}\n\n")
print("Done")
file1.close()
with open ('ai_ques.txt', 'w') as file2:
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
    for i in ai_quiz_questions:
        q = i["question"]
        c = "\n".join(i["choices"])  # Join choices into a single string
        a = i["answer"]
        file2.write(f"{q}\n{c}\nAnswer: {a}\n\n")
    print("Done")
    file2.close()
with open ('dbques.txt', 'w') as file3:
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
    for i in db_quiz_questions:
        q = i["question"]
        c = "\n".join(i["choices"])  # Join choices into a single string
        a = i["answer"]
        file3.write(f"{q}\n{c}\nAnswer: {a}\n\n")
    print("Done")
    file3.close()
import random

# Read questions from file
def read_file(file_r):
    quiz_questions = []
    with open(file_r, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            question_line = lines[i].strip()
            if not question_line:
                i += 1
                continue
            question = question_line
            choices = [lines[i + j].strip() for j in range(1, 5)]
            if i + 5 < len(lines) and "Answer:" in lines[i + 5]:
                answer = lines[i + 5].strip().split(": ")[1]
            quiz_questions.append({
                'question': question,
                'choices': choices,
                'answer': answer
            })
            i += 7
    return quiz_questions

# Registration function
def register():
    while True:
        with open('user.txt', 'r') as user_file:
            lines = user_file.readlines()

        username = input("Enter a username: ")
        if any(username in line for line in lines):
            print("Username already exists. Try another.")
        else:
            with open('user.txt', 'a') as user_file:
                while True:
                    pwd = input("Enter a password: ")
                    if 8 <= len(pwd) <= 20 and any(c.islower() for c in pwd) and \
                            any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and \
                            any(c in '@#%_!.' for c in pwd):
                        user_file.write(f"{username}\t\t{pwd}\n")
                        print("Registration successful!")
                        return True
                    else:
                        print(
                            "Retry! Password must contain:\nOne capital letter\nOne small letter\nOne number\nOne special character")

# Login function
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("user.txt", "r") as file:
        users = {}
        for line in file:
            uname, pwd = line.strip().split("\t\t")
            users[uname] = pwd

    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Quiz function
def quiz(username):
    while True:
        print("Which quiz would you like to attempt?")
        print("A) Python\nB) AI\nC) Database\nD) Exit")
        ch = input("Enter a choice: ").upper()
        count = 0

        if ch == 'A':
            questions = read_file('pyques.txt')
        elif ch == 'B':
            questions = read_file('aiques.txt')
        elif ch == 'C':
            questions = read_file('dbques.txt')
        elif ch == 'D':
            break
        else:
            print("Invalid Choice")
            continue

        random.shuffle(questions)
        for idx, question in enumerate(questions[:5], start=1):
            print(f"Q{idx}: {question['question']}")
            for choice in question["choices"]:
                print(choice)
            user_answer = input("Enter your answer: ").upper()
            if user_answer and user_answer[0] == question["answer"]:
                print("Correct!")
                count += 1
            else:
                print(f"Wrong! The correct option is {question['answer']}.")

        print(f"\nResult: {count} out of 5.")
        
        # Save result to file
        with open("results.txt", "a") as result_file:
            result_file.write(f"{username}\t{ch}\t{count}/5\n")
        print("Your result has been saved.\n")

# Show result history function
def show_result_history(username):
    print(f"\nResult History for {username}:")
    with open("results.txt", "r") as result_file:
        lines = result_file.readlines()
        user_results = [line.strip() for line in lines if line.startswith(username)]
        if not user_results:
            print("No result history found.")
        else:
            for result in user_results:
                _, quiz_type, score = result.split("\t")
                print(f"Quiz: {quiz_type} | Score: {score}")

# Main function
def main():
    response = input("Are you already registered? (yes/no): ").strip().lower()

    if response == 'no':
        print("Please register first.")
        register()

    username = login()
    if username:
        while True:
            print("\nMenu:")
            print("1. Take Quiz")
            print("2. Show Result History")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                quiz(username)
            elif choice == '2':
                show_result_history(username)
            elif choice == '3':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()