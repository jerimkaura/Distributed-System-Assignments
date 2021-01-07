

array = [0,0,0,0]
class Site:
    def __init__(self, pid, arr, exe, req, has_token):
        self.pid = pid
        self.arr  = arr
        self.exe = exe
        self.req = req
        self.has_token = has_token
        self.check_requesting_processes(sites)

    def request(self,process):
        queue.append(process.pid)
        process.req =1
        for i in range(len(array)):
            if i == process.pid:
                array[process.pid]=1

        if(self.check_requesting_processes is False):
            process.has_token = 1
        else:
            print("Another process requesting")
            queue.append(process.pid)
        print("TOKEN_HOLDER: PROCESS " +str(process.pid))
        print(array)
        print(queue)

    def check_requesting_processes(self, sites):
        for site in sites:
            if site.req == 0:
                return site.pid
        return True

    


if __name__ == '__main__':
    queue = []
    sites = []
    process_0 = Site(0, array, exe=0, req=0, has_token=0)
    process_1 = Site(1, array, exe=0, req=1, has_token=0)
    process_2 = Site(2, array, exe=0, req=0, has_token=0)
    sites.append(process_0)
    sites.append(process_1)
    sites.append(process_2)
    process_0.check_requesting_processes(sites)
    
   
    process_0.request(process_0)
    process_2.request(process_1)

    

