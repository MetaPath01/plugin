# metaPathPlugin
## MetaPath Plugin User Guide

Welcome to the MetaPath Plugin User Guide! This guide will walk you through the functionalities of the MetaPath plugin and how to use them effectively.

### Overview

MetaPath is a powerful tool that allows you to query information related to cryptocurrencies, NFTs, tokens, coins, DeFi, and Web3. With MetaPath, you can retrieve details about supported chains, recently listed NFTs, top NFT collections, NFT assets owned by a user, specific transaction details, and even swap tokens on a specific DEX.

### Table of Contents

1. [Supported Chains](#supported-chains)
2. [NFTs](#nfts)
3. [Token Swaps](#token-swaps)
4. [Transaction Details](#transaction-details)

---

### 1. Supported Chains <a name="supported-chains"></a>

To get a list of supported chains:

```javascript
MetaPath.get_coin_lists();
```

---

### 2. NFTs <a name="nfts"></a>

#### 2.1 Recently Listed NFTs

To get a list of recently listed NFTs:

```javascript
MetaPath.get_recent_nfts();
```
![image](https://github.com/MetaPath01/plugin/assets/95208869/2feb3440-1ad6-4be6-80d5-9ade332a01c7)

#### 2.2 Top NFT Collections

To get a list of top NFT collections:

```javascript
MetaPath.get_top_nfts();
```
![image](https://github.com/MetaPath01/plugin/assets/95208869/85350374-a72e-4bc5-979c-67ea0cc1096d)

#### 2.3 NFT Assets Owned by a User

To get a list of NFT assets owned by a specific user:

```javascript
MetaPath.get_nfts_by_user({
  owner: "user_address_here"
});
```

Replace `user_address_here` with the desired user's address.

---

### 3. Token Swaps <a name="token-swaps"></a>

To get a quote for swapping tokens on a specific DEX:

```javascript
MetaPath.get_quote_between_two_tokens({
  fromTokenName: "token_name_here",
  toTokenName: "token_name_here",
  fromTokenAmount: "amount_here",
  wallet_address: "receiver_address_here",
  fromTokenChain: "chain_name_here",
  toTokenChain: "chain_name_here"
});
```

Replace the placeholders with the appropriate values:
- `token_name_here`: Name of the token.
- `amount_here`: Amount of the token to swap.
- `receiver_address_here`: Address of the receiver.
- `chain_name_here`: Name of the chain.

---
![image](https://github.com/MetaPath01/plugin/assets/95208869/4112c708-4db7-4b74-8b14-1f23db391515)


### 4. Transaction Details <a name="transaction-details"></a>

To get details for a specific transaction:

```javascript
MetaPath.get_trans_detail({
  hash: "transaction_hash_here"
});
```

Replace `transaction_hash_here` with the desired transaction hash.

---
![image](https://github.com/MetaPath01/plugin/assets/95208869/38526588-6ae3-4553-8152-67b77a0313bd)


### Conclusion

MetaPath offers a comprehensive suite of tools for querying various aspects of the crypto and NFT world. Whether you're looking to explore the latest NFT listings, check transaction details, or swap tokens, MetaPath has you covered. Use this guide as a reference to navigate and make the most of the plugin's functionalities.
