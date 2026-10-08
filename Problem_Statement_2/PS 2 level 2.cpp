#include <iostream>
#include <unordered_map>
#include <cmath>
#include <random>
#include <algorithm>
using namespace std;

random_device rd;
mt19937 gen(rd());

class Bender {
public:
    string Name, type;
    int att, def, sp, HP;
    string movname[4];
    int points, damage;
    unordered_map<string, int> Move;

    void getinput(){
        cout << "Enter name of the Bender" << endl;
        cin >> Name;

        cout << "Enter element of Bender" << endl;
        cin >> type;

        cout << "Enter the values in this order- HP, Attack, Defence, Speed" << endl;
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
        cout << Name << " (" << type << ") - "
             << "HP:" << HP << "/" << HP
             << ", Attack:" << att
             << ", Defence:" << def
             << ", Speed:" << sp << '\n';

        cout << "Moves:";

        for (int i = 0; i < 4; i++){
            cout << movname[i] << "-" << Move[movname[i]] << " ";
        }

        cout << '\n';
    }

    double typeMultiplier(Bender &target){

        if (type == "Water" && target.type == "Fire")
            return 2.0;

        if (type == "Fire" && target.type == "Air")
            return 2.0;

        if (type == "Air" && target.type == "Earth")
            return 2.0;

        if (type == "Earth" && target.type == "Water")
            return 2.0;


        if (target.type == "Water" && type == "Fire")
            return 0.5;

        if (target.type == "Fire" && type == "Air")
            return 0.5;

        if (target.type == "Air" && type == "Earth")
            return 0.5;

        if (target.type == "Earth" && type == "Water")
            return 0.5;

        return 1.0;
    }

    void attack(Bender &target, string move){

        double type = typeMultiplier(target);

        uniform_real_distribution<double> dis(0.0, 1.0);

        double critical = 1.0;

        if (dis(gen) < 0.10){
            critical = 2.0;
        }

        double baseDamage =
            (double)(att * Move[move]) / target.def;

        damage = max(1, (int)round(baseDamage * type * critical));

        target.HP -= damage;
    }

    void check(){
        if (HP < 0){
            HP = 0;
        }
    }

    bool fainted(){
        return HP == 0;
    }
};


class Duel {
public:

    Bender bender1, bender2;

    void setup(){
        bender1.getinput();

        cout << "Now 2nd Bender" << endl;

        bender2.getinput();
    }

    void battle(){

        cout << "\n";
        cout << bender1.Name << " (" << bender1.type
             << ", HP: " << bender1.HP << "/" << bender1.HP
             << ") VS "
             << bender2.Name << " (" << bender2.type
             << ", HP: " << bender2.HP << "/" << bender2.HP
             << ")" << endl;

        Bender *first;
        Bender *second;

        if (bender1.sp > bender2.sp){
            first = &bender1;
            second = &bender2;
        }
        else if (bender2.sp > bender1.sp){
            first = &bender2;
            second = &bender1;
        }
        else{

            uniform_int_distribution<int> dis(0, 1);

            if (dis(gen) == 0){
                first = &bender1;
                second = &bender2;
            }
            else{
                first = &bender2;
                second = &bender1;
            }
        }

        cout << first->Name << " goes first!" << endl;

        while (!bender1.fainted() && !bender2.fainted()){

            uniform_int_distribution<int> moveDis(0, 3);

            int moveIndex = moveDis(gen);

            string move = first->movname[moveIndex];

            int oldHP = second->HP;

            first->attack(*second, move);

            second->check();

            cout << first->Name << " used " << move
                 << " and dealt " << first->damage
                 << " damage to " << second->Name << "!"
                 << endl;

            cout << second->Name << " HP: "
                 << second->HP << endl;

            if (second->fainted()){
                cout << second->Name << " fainted!" << endl;
                break;
            }


            moveIndex = moveDis(gen);

            move = second->movname[moveIndex];

            second->attack(*first, move);

            first->check();

            cout << second->Name << " used " << move
                 << " and dealt " << second->damage
                 << " damage to " << first->Name << "!"
                 << endl;

            cout << first->Name << " HP: "
                 << first->HP << endl;

            if (first->fainted()){
                cout << first->Name << " fainted!" << endl;
                break;
            }
        }

        if (bender1.fainted()){
            cout << bender2.Name << " wins!" << endl;
        }
        else{
            cout << bender1.Name << " wins!" << endl;
        }
    }
};

int main() {

    Duel duel;
    duel.setup();
    cout << "\n";
    duel.bender1.display();
    cout << "\n";
    duel.bender2.display();
    cout << "\n";
    duel.battle();
    return 0;
}