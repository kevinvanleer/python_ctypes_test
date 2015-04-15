#include <stdlib.h>

struct test_struct {
    int a;
    int b;
    int c;
    int d;
} typedef test_struct;

test_struct* get_test_struct(const int valid) {
    test_struct* newStruct = 0;
    if (valid > 0) {
	newStruct = malloc(sizeof *newStruct);
	newStruct->a = 1;
	newStruct->b = 2;
	newStruct->c = 3;
	newStruct->d = 4;
    }
    return newStruct;
}

void get_two_floats(const int valid, float* float1, float* float2) {
    if (valid > 0) {
	*float1 = 1.1f;
	*float2 = 2.2f;
    } else {
	float1 = 0;
	float2 = 0;
    }
}
