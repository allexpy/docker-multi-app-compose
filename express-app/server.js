const express = require("express")
const app = express()
const port = process.env.PORT || 3000


app.get("/javascript/", (request, response) => {
    response.send("express js index")
})

app.listen(port, () => {
    console.log(`Listening on http://localhost:${port}`)
})
