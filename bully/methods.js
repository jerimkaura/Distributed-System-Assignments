const express = require("express");
const app = express();

app.listen(4000, function () {
  console.log("Now listening");
});

app.get("/nodeDetails", function (req, res) {
    for(i of nodes_array){
        if(i.id > node_id){
            send_message(i, node_id);
        }
    }
});

nodes_array=[
	{ id: 100, name: "Node 0", cordinator: false, port: 5001 },
	{ id: 200, name: "Node 1", cordinator: false, port: 5002 },
	{ id: 300, name: "Node 2", cordinator: false, port: 5003 },
	{ id: 400, name: "Node 3", cordinator: false, port: 5004 },
];


function get_higher_nodes(nodes_array, node_id) {
    var i;
    var higher_nodes_array = [];
    for(i of nodes_array){
        if(i.id > node_id){
            higher_nodes_array.push(i)
        }
    }
    return higher_nodes_array;
}

function election(nodes_array, node_id){
	for(i of nodes_array){
		app
	}
}

election(nodes_array, 23);


