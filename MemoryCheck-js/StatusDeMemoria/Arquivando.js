const emissordeEvento = require('events')
const fs = require('fs')
const path = require('path')
const emissario = new emissordeEvento()

emissario.on('log', (message) => {
    fs.appendFile(path.join(__dirname, 'log.txt'), message, err => {
        if (err) throw err
    })
})

function log(message){
    emissario.emit('log', message)
}

module.exports = log