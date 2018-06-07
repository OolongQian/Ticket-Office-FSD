#include <iostream>

using namespace std;
int main() {
	char tmp[500]; 
	while(true) {
		cin.getline(tmp, 500, '\n');
	 	if(strcmp(tmp, "exit") == 0)
	 		break;
	 	strcat(tmp, "c++");
		printf("%s\n", tmp);
		printf("second line\n"); 
	}
	return 0; 
} 
