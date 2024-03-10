/*
 File: CS112_A1_T5_20230101.cpp
 Purpose: Subtract a square
 Author: Peter Hany Rufeat shaker
 ID: 20230101
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

void play(int number_coins) {
    vector<int> list_move;
    for (int i = 1; i <= 20; ++i) {// the list containing the square numbers from 1 to 400
        list_move.push_back(pow(i, 2));
    }

    while (number_coins != 0) {// if number of coins = 0 the game will end and the will be determind
        cout << "The number of coins: " << number_coins << endl;
        bool valid = false;
        while (!valid) {
            int player_move;
            cout << "Player 1, enter your move: ";
            cin >> player_move;

            if (cin.fail()) {// check the number entered by the player 1 is vaild according to the rules of the game 
                cin.clear();
                cin.ignore();
                cout << "Please enter a valid number." << endl;
            } else if (player_move == 1 && number_coins == 1) {
                break;
            } else if (find(list_move.begin(), list_move.end(), player_move) != list_move.end() && player_move < number_coins) {
                valid = true;
            } else {//# if the number entered by the player 1 is invalid, he tries to enter it again 
                cout << "The number is not squared or not less than the number of coins." << endl;
                cout << "Please enter a valid number." << endl;
            }
        }
        int player_move;//check winner
        number_coins -= player_move;
        if (number_coins == 0) {
            cout << "Player 1 is the winner!" << endl;
            break;
        }

        cout << "The number of coins: " << number_coins << endl;
        valid = false;
        while (!valid) {
            int player_move;
            cout << "Player 2, enter your move: ";
            cin >> player_move;

            if (cin.fail()) {// check the number entered by the player 2 is vaild according to the rules of the game
                cin.clear();
                cin.ignore();
                cout << "Please enter a valid number." << endl;
            } else if (player_move == 1 && number_coins == 1) {
                break;
            } else if (find(list_move.begin(), list_move.end(), player_move) != list_move.end() && player_move < number_coins) {
                valid = true;
            } else {//# if the number entered by the player 2 is invalid, he tries to enter it again 
                cout << "The number is not squared or not less than the number of coins." << endl;
                cout << "Please enter a valid number." << endl;
            }
        }

        number_coins -= player_move;//check winner
        if (number_coins == 0) {
            cout << "Player 2 is the winner!" << endl;
            break;
        }
    }
}
//start the game
int main() {
    srand(time(0));

    while (true) {
        char choice;
        cout << "A) Start the game" << endl;
        cout << "B) Quit the game" << endl;
        cin >> choice;

        if (choice == 'A' || choice == 'a') {
            char choice_two;
            cout << "How to determine the number of coins" << endl;
            cout << "A) Choose the number of coins" << endl;
            cout << "B) Play with a random number of coins" << endl;
            cin >> choice_two;
            if (choice_two == 'A' || choice_two == 'a') {
                int number_coins;
                cout << "Enter the number of coins: ";
                while (true){
                    cin >> number_coins;
                    if (number_coins<=10000 && number_coins>=50){
                        break;
                    }else{
                        cout <<"Sorry, minimum number of coins 50 and maximum number of coins 10000 "<< endl;
                        cout <<"please , input number of coins again" << endl;
                        continue;
                    } 
                }
                
                play(number_coins); 
            } else if (choice_two == 'B' || choice_two == 'b') {
                int number_coins = rand() % 401 + 100;
                play(number_coins);
            } else {
                cout << "Please select a valid choice." << endl;
            }
        } else if (choice == 'B' || choice == 'b') {
            cout << "Goodbye!" << endl;
            break;
        } else {
            cout << "Please select a valid choice." << endl;
        }
    }

    return 0;
}
