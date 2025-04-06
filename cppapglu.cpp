#include <bits/stdc++.h>
using namespace std;



// Function to check if a number is perfect cube
bool isPerfectCube(long long n) {
    if (n < 0) return false;
    long long root = round(cbrt(n));
    return root * root * root == n;
}

// Function to generate unique permutations and count perfect cubes
int countCubePermutations(long long num) {
    string s = to_string(num);
    unordered_set<long long> checked;
    int count = 0;
    
    // Sort to help with unique permutations
    sort(s.begin(), s.end());
    
    do {
        // Skip numbers with leading zeros
        if (s[0] == '0') continue;
        
        long long perm = stoll(s);
        
        // Skip if we've already checked this number
        if (checked.find(perm) != checked.end()) continue;
        
        checked.insert(perm);
        
        // Count if it's a perfect cube and >= original number
        if (perm >= num && isPerfectCube(perm)) {
            count++;
        }
    } while (next_permutation(s.begin(), s.end()));
    
    return count;
}

int main() {
    long long n = 5027;
    while (true) {
       
        long long cube = n * n * n;
        int count = countCubePermutations(cube);
        
        if (count >= 5) {  // Changed to 5 as per your original condition
            cout << "Found: " << cube << " (n = " << n << ")" << endl;
            cout << "Has " << count << " perfect cube permutations" << endl;
            break;
        }
        
        n++;
        
        
        cout << "Checking n = " << n << "..." << endl;
        
    }
    
    return 0;
}