// Importamos 
const Blockchain = require("./src/blockchain");

// Creamos la Blockchain
const blockchain = new Blockchain();

// Creamos (por ahora) los bloques especificados (son 10 en total)
// ya que todavia no esta automatizado el sistema de votos.
for (let i = 0; i < 10; i++) {
  const block = blockchain.añadirBlock(`Block ${i}`);
  console.log(block.toString());
}