# ***Airbnb - Console Project***

<div align="center">
  <a href="https://holbertonschool.uy">
    <img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240302%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240302T174629Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2028e3527c040a64ad9d44a592eac093aad22d8c7f084d44b150724e7a93fa34" align="center" height="250" width="600" />
  </a>
</div>

# **Description**

This repository is for the Console project of the AirBnB module in Holberton School. The project consists of building an interactive console executed in the linux terminal.

Diagram of the project:

<div align="center">
    <img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240302%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240302T174629Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=737c4d3e95ae73f61e656cc0e613e115d854c22ec59912996495c5c7c86d5441" align="center" height="250" width="600">
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
