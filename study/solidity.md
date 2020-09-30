# 一、 资源

## 1. 官方资源

https://studio.ethereum.org/

https://ethereum.org/en/learn/

https://ethereum.org/en/learn/#smart-contracts

https://solidity.readthedocs.io/en/latest/

https://ethereum.org/en/developers/#frontend-javascript-apis

https://ethereum.org/en/developers/#standards

https://github.com/ethereum/web3.js/   //WEBJS3

https://remix-ethdoc-plugin.readthedocs.io/en/latest/

https://openzeppelin.com/contracts/ // openzeppelin

https://docs.openzeppelin.com/openzeppelin/  // learn on  openzeppelin

## 2. 测试网

### (1) Ropsten

https://faucet.ropsten.be/

https://ropsten.etherscan.io/

### (2) Koven

https://kovan-testnet.github.io/

https://kovan.etherscan.io/

### (2) Rinkeby

获取不了测试币

# 二、 学习记录

## 1. https://studio.ethereum.org/

### (1) Hello World

已学习

### (2) Token

已学习

### (3) CryptoPizza NFT

已学习

## 2. https://cryptozombies.io/en/course/

### (1)  Solidity Path: Beginner to Intermediate Smart Contracts

https://cryptozombies.io/en/lesson/6/chapter/4

## 3. https://solidity.readthedocs.io/en/latest/index.html

https://solidity.readthedocs.io/en/latest/solidity-by-example.html

example草草过了一遍，后续再重读



https://solidity.readthedocs.io/en/latest/structure-of-a-contract.html



Function modifiers can be used to amend the semantics of functions in a declarative way (see

```
        for (uint i = 0; i < proposalNames.length; i++) {
            // `Proposal({...})` creates a temporary
            // Proposal object and `proposals.push(...)`
            // appends it to the end of `proposals`.
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
```

# 三、 语法

```
#指定版本
pragma solidity >=5.0.0 <0.6.0;

#contract
contract HelloWorld {
	uint dnaDigits = 16;
	struct Zombie {
		string name;
        uint dna;
    }

}

```



