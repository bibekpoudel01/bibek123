#include<iostream>
using namespace std;

class shop {
    int itemid[100];
    int itemprice[100];
    int counter;
public:
    void initCounter() {
        counter = 0;
    }
    void setprice();
    void displayprice();
};

void shop::setprice() {
    int n;
    cout << "How many items? ";
    cin >> n;
    counter = n;
    for(int i = 0; i < n; ++i) {
        cout << "Enter ID for item " << i+1 << ": ";
        cin >> itemid[i];
        cout << "Enter price for item " << i+1 << ": ";
        cin >> itemprice[i];
    }
}

void shop::displayprice() {
    cout << "\nItem IDs and Prices:\n";
    for(int i = 0; i < counter; ++i) {
        cout << "ID: " << itemid[i] << ", Price: " << itemprice[i] << endl;
    }
}

int main() {
    shop dukaan;
    dukaan.initCounter();
    dukaan.setprice();
    dukaan.displayprice();
    return 0;
}