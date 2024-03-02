# ***Airbnb - Console Project***

<div align="center">
  <a href="https://holbertonschool.uy">
    <img src="https://holberton.anahuac.mx/wp-content/uploads/ddd-1024x1024.png" align="center" height="600" width="600">
  </a>
</div>

# **Description**

This repository is for the Console project of the AirBnB module in Holberton School. The project consists of building an interactive console executed in the linux terminal.

Diagram of the project:

<div align="center">
    <img src="https://peytonbrsmith.netlify.app/projects/web/airbnb/06fccc41df40ab8f9d49.png" align="center" height="250" width="600">
</div>

# **Instalation**

1. Copy the repository link from Github (HTTPS) and `git clone` it in your local machine.
2. Open the terminal, travel to the directory via `cd` and check with `ls` if the `console.py` file is within the root of the repository
3. Change the permissions on that file via `chmod u+x console.py` for you to be able to execute it
4. Run the program with `./console.py`.


# *Commands*

The Console can execute 4 different commands:
- `create` creates an ID for the given class name
- `show` prints a string representation based on the class name and ID
- `update` Updates an instance based on the class name and ID by adding or updating an attribute to it
- `delete` deletes an instance from the system based on the class name and ID
- `all` Prints all string representation of all instances based or not on the class name
- `help` shows available commands to the user


# *Example Usage*

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  create  show  update  destroy  all quit

(hbnb) 
(hbnb) create BaseModel
c11e70de-c4d1-4dd1-b15a-01f119b12997
(hbnb) show BaseModel c11e70de-c4d1-4dd1-b15a-01f119b12997
[BaseModel] (c11e70de-c4d1-4dd1-b15a-01f119b12997) {'id': 'c11e70de-c4d1-4dd1-b15a-01f119b12997', 'created_at': datetime.datetime(2024, 3, 2, 18, 53, 52, 838879), 'updated_at': datetime.datetime(2024, 3, 2, 18, 53, 52, 838934)}
(hbnb) all BaseModel
["[BaseModel] (c11e70de-c4d1-4dd1-b15a-01f119b12997) {'id': 'c11e70de-c4d1-4dd1-b15a-01f119b12997', 'created_at': datetime.datetime(2024, 3, 2, 18, 53, 52, 838879), 'updated_at': datetime.datetime(2024, 3, 2, 18, 53, 52, 838934)}"]
(hbnb) update BaseModel c11e70de-c4d1-4dd1-b15a-01f119b12997 email "mabm2004@gmail.com"
(hbnb) all BaseModel
['[BaseModel] (c11e70de-c4d1-4dd1-b15a-01f119b12997) {\'id\': \'c11e70de-c4d1-4dd1-b15a-01f119b12997\', \'created_at\': datetime.datetime(2024, 3, 2, 18, 53, 52, 838879), \'updated_at\': datetime.datetime(2024, 3, 2, 18, 53, 52, 838934), \'email\': \'"mabm2004@gmail.com"\'}']
(hbnb) destroy BaseModel c11e70de-c4d1-4dd1-b15a-01f119b12997
(hbnb)
(hbnb) quit
$
```
