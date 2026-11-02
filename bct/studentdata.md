## 1. Solidity Code

Create a file named `StudentData.sol`.

```

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure
    struct Student {
        uint rollNo;
        string name;
        uint age;
        string course;
    }

    // Array
    Student[] public students;

    // Fallback function
    fallback() external payable {
    }

    // Add student
    function addStudent(
        uint _rollNo,
        string memory _name,
        uint _age,
        string memory _course
    ) public {
        students.push(Student(_rollNo, _name, _age, _course));
    }

    // Get student details
    function getStudent(uint _index)
        public
        view
        returns (uint, string memory, uint, string memory)
    {
        Student memory s = students[_index];

        return (s.rollNo, s.name, s.age, s.course);
    }

    // Get total students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }
}

```

## 2. Steps to Perform Practical

Step 1: Open Remix IDE

Go to [https://remix.ethereum.org/](https://remix.ethereum.org/?utm_source=chatgpt.com)

Step 2: Create Solidity File

1. Open File Explorer.
2. Click New File.
3. Name it `StudentData.sol`.
4. Paste the above code.

Step 3: Compile

1. Open Solidity Compiler.
2. Select compiler version `0.8.20`.
3. Click Compile StudentData.sol.
4. Check for compilation errors.

Step 4: Deploy

1. Open Deploy & Run Transactions.
2. Select Environment: `Remix VM (Cancun)` or another available Remix VM.
3. Select contract: `StudentData`.
4. Click Deploy.
5. Check the deployed contract section.

Step 5: Add Student Details

Use `addStudent`:

First student:

- Roll No: `1`
- Name: `"Rahul"`
- Age: `20`
- Course: `"Computer Engineering"`

Click Transact.

Second student:

- Roll No: `2`
- Name: `"Priya"`
- Age: `21`
- Course: `"Information Technology"`

Click Transact.

Step 6: Display Student Details

- Click `getStudentCount` → Output: `2`
- Enter `0` in `getStudent` → Displays Rahul's details.
- Enter `1` in `getStudent` → Displays Priya's details.

Step 7: Execute Fallback Function

1. Open Deploy & Run Transactions.
2. Find Low level interactions.
3. Enter the deployed contract address.
4. Enter calldata:

```
0x12345678
```

5. Set Value to `0`.
6. Click Transact.

The fallback function executes because the input does not match any existing function selector.

## 3. Observe Gas and Transaction Fee

1. Open Remix Terminal.
2. Expand the transaction details.
3. Observe Gas Used, Transaction Cost, Execution Cost and Gas Price.

Formula:

\\[ \text{Transaction Fee}=\text{Gas Used}\times\text{Gas Price} \\]

Record the actual values:

| Operation     | Gas Used | Transaction Fee |
| ------------- | -------- | --------------- |
| Deployment    |          |                 |
| Add Student 1 |          |                 |
| Add Student 2 |          |                 |
| Fallback      |          |                 |

## 4. Result

The Student Data smart contract was successfully created and deployed using Solidity. Structures, arrays and fallback functions were implemented. Student records were added and retrieved successfully, and gas consumption and transaction fees were observed.

Note: Remix VM is a local test blockchain, not Ethereum mainnet. No real ETH is spent.