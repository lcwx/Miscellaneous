#include"head.h"

int main() {
	//Main

	//Display
	system("title Gobang");
	system("mode con cols=30 lines=16");
	system("color E0");

	//Introduce operation
	string FirstSen = "Hi, I'm Levi. ";
	string SecondSen = "I'm happy to see you come here. ";
	string ThirdSen = "Let me introduce the operation of the game. ";
	string FourthSen = "W is for up; A is for left; D is for right. S is for down. ";
	string FifthSen = "Space is for chess moving. ";
	display(FirstSen);
	display(SecondSen);
	display(ThirdSen);
	display(FourthSen);
	display(FifthSen);
	delay(10000);
	system("pause");

	//Clear screen operation   
	system("cls");

	//Let player choose either PVP or fight with AI
	string Sen_1 = "What would you like to play with ?";
	display(Sen_1);
	string Sen_2 = "If you want to play with me, please enter 1. ";
	display(Sen_2);
	string Sen_3 = "If you like PVP, please enter 2. ";
	display(Sen_3);
	delay(10000);
	cout << "enter : ";
	int choose_2;
	scanf("%d", &choose_2);
	if (choose_2 != 1 && choose_2 != 2) {
		printf("ERROR\n");
		system("pause");
		return 0;
	}

	//Clear screen operation   
	system("cls");

	//Let player choose first or latter
	if (choose_2 == 1) {
		cout << "Choose first or later. 1 is for first, 2 is for latter : ";
		getchar();
		int choose_1;
		scanf("%d", &choose_1);
		if (choose_1 == 1) {
			human = 1;
			AI = 2;
		}
		else if (choose_1 == 2) {
			human = 2;
			AI = 1;
		}
		else {
			printf("ERROR!\n");
			system("pause");
			return 0;
		}

		//Clear screen operation   
		system("cls");
	}

	//Initialization
	initialization();

	//Input control
	while (true) {
		//Console gets a character from the keyboard 
		if (human == player) {
			while (true) {
				char key = getch();
				if (!(PlayerOperation(key))) {
					//Clear screen operation   
					system("cls");
					//Print
					print();
					break;
				}
				else {
					//Clear screen operation   
					system("cls");
					//Print
					print();
				}
			}
		}
		else {
			while (true) {
				if (choose_2 == 2) {
					char key = getch();
					if (!(PlayerOperation(key))) {
						//Clear screen operation   
						system("cls");
						//Print
						print();
						break;
					}
					else {
						//Clear screen operation   
						system("cls");
						//Print
						print();
					}
				}
				else {
					Levi(AI);
					//Clear screen operation   
					system("cls");
					//Print
					print();
					break;
				}
			}
		}

		//Law of game
		if (judge(choose_2))
			break;
	}

	return 0;
}
