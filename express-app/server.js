const express = require("express")
const app = express()
const port = process.env.PORT || 3000

// function handleIndex (request, response) {
//     response.send("hello world")
// }

app.get("/", (request, response) => {
    response.send("hello world")
})

app.get("/world/", (request, response) => {
    response.send("the world")
})

app.listen(port, () => {
    console.log(`Listening on http://localhost:${port}`)
})
