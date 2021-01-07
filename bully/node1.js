const express = require('express')
const app = express()


app.listen(4000, function () {
    console.log('Now listening');    
})


app.get('/nodeDetails', function(req, res){    
    let node1 =new  Node(4000, "Node1", false, 4000);
    console.log(node1.name);
    res.json({name: node1.name, id: node1.id, cordinator: node1.cordinator, port: node1.port});
});

class Node{
    constructor(id, name, cordinator=false, port){
        this.id = id;
        this.name = name;
        this.cordinator = cordinator;
        this.port = port
    }
}


