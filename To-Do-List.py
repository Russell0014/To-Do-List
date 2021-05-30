from datetime import date
from typing import overload
import pandas as pd
from pandas.core.algorithms import mode
from pandas.core.frame import DataFrame
import os

folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(folder, "task.csv")


t_date = date.today().strftime("%d/%m/%y")
t_date_con = t_date.split("/")
t_date_one = int(t_date_con[0])
columns = ["Tasks", "Due Date", "Due status"]
todo = pd.DataFrame(columns=columns)

todo = pd.read_csv(my_file, index_col=0)
print("-----------------------------TO DO App-----------------------------")

sel = ""
over_due = "overdue"
due_today = "due today"
due_after_today = "due after today"
no_due = "-"

while sel != "Q":

    sel = str(
        input("'A' for add, 'D' for delete, 'P' for print all tasks, 'Q' for quit: ")
    )
    print("")
    if sel == "A":
        due = input("Enter due date in DD/MM/YY: ")
        due_con = due.split("/")
        due_con_one = int(due_con[0])
        task = input("Enter your task: ")
        print("")

        if (
            due_con[0] < t_date_con[0]
            and due_con[1] <= t_date_con[1]
            and due_con[2] == t_date_con[2]
        ):
            todo = todo.append(
                {"Tasks": task, "Due Date": due, "Due status": over_due},
                ignore_index=True,
            )
        elif (
            due_con[0] == t_date_con[0]
            and due_con[1] == t_date_con[1]
            and due_con[2] == t_date_con[2]
        ):
            todo = todo.append(
                {"Tasks": task, "Due Date": due, "Due status": due_today},
                ignore_index=True,
            )
        elif (
            due_con_one == t_date_one + 1
            and due_con[1] == t_date_con[1]
            and due_con[2] == t_date_con[2]
        ):
            todo = todo.append(
                {"Tasks": task, "Due Date": due, "Due status": due_after_today},
                ignore_index=True,
            )
        else:
            todo = todo.append(
                {"Tasks": task, "Due Date": due, "Due status": no_due},
                ignore_index=True,
            )

    elif sel == "D":
        print("-------------Tasks-------------")
        print(todo)
        del_num = input("Enter row number to delete: ")
        del_num = int(del_num)
        todo.drop([del_num], inplace=True)
        print("")

    elif sel == "P":
        print("-------------Tasks-------------")
        print(todo)
        print("")

todo.to_csv(my_file)
