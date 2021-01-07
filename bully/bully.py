def process_list(id, message_to_send_case=0):
    nodes_list = [1, 2, 3, 4, 5]  
    if message_to_send_case == 1:  # sending the election request
        higher_order_nodes=[]
        for x in nodes_list:
            if id < x: 
                higher_order_nodes.append(x)  # list of nodes with an id higher than the current node 
        if id==len(nodes_list): # last node in the list
             return None # theres no higher priority node

        return higher_order_nodes # return list of higher priority nodes
    if message_to_send_case==2 and id != 1: #respond to an ok message to the election
        return [nodes_list[int(id)-2] ]  # return id of predecessor node in priority hierachy
        
    if message_to_send_case==3:  #sending an victory message to other nodes
        del nodes_list[len(nodes_list)-1]  # pop the highest id 
        return nodes_list # updated list with recepients being everyone minus the winner



def sending_data(node_id,recepients,message):
    if recepients != None:
        for node in recepients:
            print("NODE "+str(node_id) + " to NODE "+str(node)+":  " +message)


def node(myId):
    sending_list=process_list(myId,1)
    if  sending_list is None: # no node is higher and thus, this node has won
        sending_data(myId,process_list(myId,3),"I AM THE COORDINATOR") # when the highest node wins
    else :
        sending_data(myId, sending_list,"Election initiated") # forward an election message to higher node in the priority list
    sending_data(myId, process_list(myId,2),"OK") #send data to lower nodes in the priority list


node(1)
node(2)
node(3)
node(4)
node(5)
