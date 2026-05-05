(<!DOCTYPE html>
<html>
<head>
  <title>Pharos MVP</title>
</head>
<body>
  <h2>Pharos Faucet MVP</h2>
  <button onclick="connectWallet()">Connect Wallet</button>
  <p id="wallet"></p>

  <button onclick="requestFunds()">Request Faucet</button>
  <p id="status"></p>

  <h3>Transactions</h3>
  <ul id="txList"></ul>

<script>
let account = "";

async function connectWallet() {
  if (window.ethereum) {
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    account = accounts[0];
    document.getElementById("wallet").innerText = "Connected: " + account;
  }
}

function requestFunds() {
  const tx = "0x" + Math.random().toString(16).substr(2, 8);
  document.getElementById("status").innerText = "Faucet sent!";
  
  const li = document.createElement("li");
  li.innerText = "Tx: " + tx;
  document.getElementById("txList").appendChild(li);
}
</script>
</body>
</html>