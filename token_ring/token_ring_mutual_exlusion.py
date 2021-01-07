

array = [0,0,0,0]
class Site:
    def __init__(self, pid, arr, exe, req, has_token):
        self.pid = pid
        self.arr  = arr
        self.exe = exe
        self.req = req
        self.has_token = has_token
        self.check_requesting_processes(sites)

    def request(self):
        msg = " "
        print("PROCESS "+str(self.pid) + " REQUESTING...")
        if self.check_requesting_processes(sites) is True:
            msg = "ANOTHER PROCESS REQUESTING, DENIED"
            queue.append(self.pid)
            self.req =0
        else:
            
            self.req =1 
            self.execute_CS()
        for i in range(len(array)):
            if i == self.pid:
                array[self.pid] = 1
        print(msg)

    def execute_CS(self):
        if self.req == 0:                
            print("PROCESS "+str(self.pid)+ " EXECUTING....")
            msg = "TOKEN HOLDER IS PROCESS "+str(self.pid)
            self.has_token = 1
            self.release_token()


    def check_requesting_processes(self, sites):
        requests = []
        for site in sites:
            if site.req == 1:
                requests.append(site.pid)        
        if len(requests) > 1:
            return True
        return False    

    def grant_permission(self):
        if self.req == 1:
            self.req =0
    
    def release_token(self):
        self.has_token = 0
        print("PROCESS " +str(self.pid) +"  RELEASED TOKEN")       
        


if __name__ == '__main__':
    queue = []
    sites = []
    #init processes
    process_0 = Site(0, array, exe=0, req=1, has_token=1)
    process_1 = Site(1, array, exe=0, req=0, has_token=0)
    process_2 = Site(2, array, exe=0, req=0, has_token=0)
    process_3 = Site(3, array, exe=0, req=0, has_token=0)
    sites= [process_0, process_1, process_2, process_3]

    process_1.request()
    process_1.execute_CS()
    process_1.release_token()
    process_3.request()    
    process_2.request()
    process_3.execute_CS()
   
  
    
    
    

    
    
    
    

    

