## BCT3 Practical: Bank Account Smart Contract

### Step 1: Open Remix IDE
1. Open [Remix IDE](https://remix.ethereum.org/?utm_source=chatgpt.com).
2. Click **File Explorer**.
3. Create a new file named `BankAccount.sol`.

### Step 2: Write the code

Paste this code into `BankAccount.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {
    mapping(address => uint256) private balances;

    // Deposit money
    function deposit() public payable {
        require(msg.value > 0, "Amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    // Withdraw money
    function withdraw(uint256 amount) public {
        require(amount > 0, "Enter valid amount");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    // Show balance
    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
```

### Step 3: Compile
1. Click **Solidity Compiler**.
2. Select compiler version `0.8.20` or a compatible newer `0.8.x` version.
3. Click **Compile BankAccount.sol**.
4. Confirm the green **Compiled** status.

### Step 4: Deploy
1. Click **Deploy & Run Transactions**.
2. Select `Remix VM` as the environment.
3. Select `BankAccount` in the contract dropdown.
4. Set **Value** to `0`.
5. Click **Deploy**.
6. Expand `BankAccount` under **Deployed Contracts**.

### Step 5: Deposit 2 ETH
1. Set **Value** to `2`.
2. Select `ether` from the unit dropdown.
3. Click **Transact** beside `deposit`.
4. Wait for the transaction to succeed.

### Step 6: Show balance
1. Click **Call** beside `showBalance`.
2. Expected output:

```text
2000000000000000000
```

### Step 7: Withdraw 1 ETH
1. Set **Value** to `0 ether`.
2. Enter `1000000000000000000` in the `withdraw` amount field.
3. Click **Transact** beside `withdraw`.
4. Wait for the transaction to succeed.

### Step 8: Check updated balance
1. Click **Call** beside `showBalance`.
2. Expected output:

```text
1000000000000000000
```

### Step 9: Verify insufficient balance
1. Keep **Value** at `0 ether`.
2. Enter `2000000000000000000` in the `withdraw` amount field.
3. Click **Transact**.
4. The transaction should fail with `Insufficient balance`.

### Step 10: Record the result

| Operation | Amount | Expected balance |
|---|---:|---:|
| Initial balance | 0 ETH | 0 ETH |
| Deposit | 2 ETH | 2 ETH |
| Show balance | — | 2 ETH |
| Withdraw | 1 ETH | 1 ETH |
| Show balance | — | 1 ETH |

**Result:** Successfully implemented, deployed, and tested the Bank Account smart contract using Solidity and Remix VM.