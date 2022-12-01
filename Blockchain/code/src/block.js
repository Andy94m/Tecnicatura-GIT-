// Importamos el algoritmo SHA256 para encriptar
const SHA256 = require("crypto-js/sha256");


// Añadimos algunas constantes para ayudarnos a ejecutar
const DIFICULTAD = 3;
const RATE_MINADO = 3000;


// Creamos el objeto bloque
class Block {
  constructor(tiempo, hashPrevio, hash, data, nope, DIFICULTAD) {
    this.tiempo = tiempo;
    this.hashPrevio = hashPrevio;
    this.hash = hash;
    this.data = data;
    this.nope = nope;
    this.DIFICULTAD = DIFICULTAD;
  }

  
// Creamos el metodo genesis para el primer bloque y obetener los datos
  static get genesis() {
    const tiempo = new Date("2009-03-01").getTime();
    return new this(
      tiempo,
      undefined,
      "genesis_hash",
      "Genesis Block",
      0,
      DIFICULTAD
    );
  }


// Creamos el metodo de minado para los bloques: Encriptamos, validamos el
// bloque anterior y retornamos los datos para el siguiente bloque
  static minar(previousBlock, data) {
    const { hash: hashPrevio } = previousBlock;
    let { DIFICULTAD } = previousBlock;
    let hash;
    let tiempo;
    let nope = 0;

    do {
      tiempo = Date.now();
      nope += 1;
      DIFICULTAD =
        previousBlock.tiempo + RATE_MINADO > tiempo ? DIFICULTAD + 1 : DIFICULTAD - 1;
      hash = SHA256(hashPrevio + tiempo + data + nope + DIFICULTAD).toString();
    } while (hash.substring(0, DIFICULTAD) !== "0".repeat(DIFICULTAD));

    return new this(tiempo, hashPrevio, hash, data, nope, DIFICULTAD);
  }


// Imprimimos la información
  toString() {
    const { tiempo, hashPrevio, hash, data, nope, DIFICULTAD } = this;
    return `🧱 Block - 
            Tiempo: ${tiempo}
            Previous Hash: ${hashPrevio}
            Hash: ${hash}
            Data: ${data}
            nope: ${nope}
            DIFICULTAD: ${DIFICULTAD}
            -------------------------------------`;
  }
}


// Exportamos para las otras clases 
module.exports = Block;