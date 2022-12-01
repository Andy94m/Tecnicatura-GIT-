// Importamos desde la clase Block
const Block = require("./block");


// Crea el nuevo bloque y lo añade al array inicializado
class Blockchain {
  constructor() {
    this.chain = [Block.genesis];
  }

  añadirBlock(data) {
    const blockAnterior = this.chain[this.chain.length - 1];
    const block = Block.minar(blockAnterior, data);
    this.chain.push(block);
    return block;
  }
}

// Exportamos para otras clases
module.exports = Blockchain;