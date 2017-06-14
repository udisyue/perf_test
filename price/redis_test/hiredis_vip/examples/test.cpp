#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main() {
    srand((unsigned)time(NULL));
    int index = rand()%12;
    switch(index) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            cout << index << endl;
            break;
        default:
            cout << "not 1" << endl;
    }
    return 0;
}
