#include <stdio.h>
#include <iostream>
using namespace std;

class Proces{
int priority, pid, leader,status;


public:
    void init(int i, int lead);
    void bully(Proces *prc, int num, int caller);
    void disp();


};

void Proces::init(int i, int lead){
        //cout<<"\n Enter Process "<<i+1<<" Priority: ";
        //cin>>Proces::priority;
        Proces::priority = i;
        Proces::leader = lead;
        cout<<"\n Enter Process ID: ";
        cin>>Proces::pid;
        cout<<"\n Enter Process Status.1 for Active 0 for Inactive: ";
        cin>>Proces::status;

}

void Proces::disp(){
        cout<<"\n Process: "<<Proces::pid;
        cout<<"\n Process Priority: "<<Proces::priority;
        cout<<"\n Process Status: "<<Proces::status;
        cout<<"\n Leader: "<<Proces::leader;

}


void Proces::bully(Proces *prc, int pr_num, int caller){

    for(int i=0;i<pr_num;i++){
                    //caller becomes default leader
                prc[i].leader =caller;

            }

    int next;
    next = caller+1;
    //Send Election message to higher process
        if(caller<pr_num){
                if(prc[next].status == 1){
            //1 is active, 0 is inactive
            cout<<"\n Message Sent to: "<<next;

            prc[0].bully(prc, pr_num,next);



            }else{
                while(next<pr_num){
                    cout<<"\n Inactive Process "<<next<<" Skipped";
                    next = next+1;
                    if (prc[next].status==1){

                        prc[0].bully(prc, pr_num,next);
                        break;
                    }
                    if (next>pr_num){
                        break;
                    }
                }

            }
        }else{
            cout<<"Final Element";

        }



}

int main(){
    int num,call;
    cout<<"\n Enter Number of Process: ";
    cin>>num;
    Proces b[num];

    for(int i=0; i<num;i++){
        b[i].init(i,num);
    }

    cout<<"\n Enter Process That Calls For Election: ";
    cin>>call;
    b[0].bully(b, num,call);

}