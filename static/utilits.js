const log = console.log.bind(console)
const qs = function (domName) {
    return document.querySelector(domName)
}
// 封装成 promise
const ajax = (request) => {
    let p = new Promise(function (resolve, reject) {
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                resolve(this.response)
            }
        }
        xhttp.open("GET", request.url, true);
        xhttp.responseType = request.type
        xhttp.send();
    })

    return p
}

const fun_test = () => {
    let bytes = window.bytes
    let canvas = document.getElementById("id-canvas");
    let ctx = canvas.getContext("2d");
    for (let i = 0; i < 8; i++) {
        let line = bytes[8 * index + i]
        let byteLine = parseTo16Binary(line)
        newLine = mergeBinary(byteLine)
        log('newLine', newLine)
        // 计算 y
        let y = 10 * i
        for (let j = 0; j < 8; j++) {
            let c = color[newLine[j]]
            let x = 10 * j

            ctx.fillStyle = c
            ctx.fillRect(x, y, x + 10, y + 10);
        }
    }
}