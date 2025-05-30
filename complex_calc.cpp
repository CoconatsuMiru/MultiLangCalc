#include <iostream>
#include <cmath>
#include <cstring>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "ERROR: No input provided\n";
        return 1;
    }

    std::string input = argv[1];
    
    if (input.find("sqrt") == 0) {
        double num;
        sscanf(input.c_str(), "sqrt %lf", &num);
        if (num < 0) {
            std::cout << "SQRT_NEGATIVE_ERROR\n";
        } else {
            std::cout << sqrt(num) << "\n";
        }
    } else {
        double base, exp;
        sscanf(input.c_str(), "%lf ^ %lf", &base, &exp);
        std::cout << pow(base, exp) << "\n";
    }

    return 0;
}
