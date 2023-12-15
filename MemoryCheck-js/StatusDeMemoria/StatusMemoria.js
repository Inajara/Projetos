const os = require('os')
const log = require('./Arquivando')

//loop de dados
setInterval(() => {
    //const memoriaLivre = os.freemem | const memoriaTotal = os.totalmem
    const { freemem, totalmem } = os
    //converter byte para MB
    const memoriaLivre = parseInt(freemem()/1024/1024)
    const memoriaTotal = parseInt(totalmem()/1024/1024)
    const percentualMemoria = parseInt((memoriaLivre/memoriaTotal)*100)
    const statusMemoria = {
        memoriaLivre: `${memoriaLivre} MB`,
        memoriaTotal: `${memoriaTotal} MB`,
        memoriaUsada: `${percentualMemoria}%`
    }
    console.clear()
    console.log("<===== Status de memória do computador: =====>")
    console.table(statusMemoria)
    log(`${JSON.stringify(statusMemoria)}\n`)
}, 1000)