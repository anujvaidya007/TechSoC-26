#include <iostream>
#include <unordered_map>
#include <cmath>
using namespace std;

class Bender {
public:
    string Name, type;
    int att,def,sp,HP;
    string movname[4];
    int points, damage;
    unordered_map<string, int> Move;
    
void getinput(){
    cout << "Enter name of the Bender"<<endl;
    cin >> Name;
    cout << "Enter element of Bender"<<endl;
    cin >> type;
    cout << "Enter the values in this order- HP, Attack, Defence, Speed"<<endl;
    cin >> HP >> att >> def >> sp;
    for (int i = 0; i < 4; i++){
        cout << "Enter name of move no. " << 1+i << '\n';
        cin >> movname[i];
        cout << "Enter impact value of move no. " << 1+i << '\n';
        cin >> points;
        Move[movname[i]] = points;
    }  
}

void display(){
    cout << Name <<" ("<<type<<") - "<<"HP:"<<HP<<"/"<<HP<<", Attack:"<<att<<", Defence:"<<def<<", Speed:"<<sp<< '\n';
    cout << "Moves:";
    for (int i =0; i <4; i++){
        cout << movname[i] << "-" << Move[movname[i]] <<" ";
    }
}

void attack(Bender &target , string move){
    damage = round((double)(att * Move[move]) / target.def);
    target.HP -= damage;
}

void check(){
    if (HP < 0){
        HP = 0;
    }
}
};

int main() {
    Bender bender1;
    Bender bender2;
    bender1.getinput();
    cout << "Now 2nd Bender"<<endl;
    bender2.getinput();
    bender1.display();
    bender2.display();
    if (bender1.sp >= bender2.sp){
        string m;
        cout<<"What move you want to play, type its name."<<endl;
        cin >> m;
        bender1.attack(bender2, m);
        cout << bender2.Name <<" took "<< bender1.damage <<" damage!"<<endl;
        bender2.check();
        if (bender2.HP == 0){
            cout<<bender2.Name<<" fainted: True";
        }
        else{cout<<bender2.Name<<" fainted: False";}
    }
    else if (bender2.sp > bender1.sp){
        string m;
        cout<<"What move you want to play, type its name."<<endl;
        cin >> m;
        bender2.attack(bender1, m);
        cout << bender1.Name <<" took "<<bender2.damage<<" damage!"<<endl;
        bender1.check();
        if (bender1.HP == 0){
            cout<<bender1.Name<<" fainted: True";
        }
        else{cout<<bender1.Name<<" fainted: False";}
    }
    return 0;
}