const express = require("express");
const app = express();

app.listen(4001, function () {
  console.log("Now listening");
});

class Node {
  constructor(id, name, cordinator = false, port) {
    this.id = id;
    this.name = name;
    this.cordinator = cordinator;
    this.port = port;
  }
}
