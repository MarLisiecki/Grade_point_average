# Grade point average
##  Created by:
[![N|Solid](https://i.imgur.com/zk7PUsqm.jpg)](https://nodesource.com/products/nsolid)


Grade point calculator which automatically calculate your semester/year average (college: Wrocław University of Science and Technology)

## Preparations

- Download XLS from JSOS
- Open the file using Excel or other software
- Save it as CSV file
- In initial_values.py set self.name_of_file = "NAME OF YOUR FILE"
- In initial_values.py set self.choice = [LIST OF STRINGS WITH NAME OF SEMESTER] 
for example:  self.choice = ["Zimowy(2019/2020)", "Letni(2019/2020)"]
- Run your script, in console you will see your average 

## Requirements
- Python 3.7+
- Numpy library

## Test coverage

|Name                | Stmts         |Miss   | Cover   |
| ------------------ |:-------------:| -----:|--------:|
|helpers_func.py     | 28            |0      | 100%    |
|initial_values.py   | 10            |0      | 100%    |
|main.py             | 13            |5      | 62%     |

