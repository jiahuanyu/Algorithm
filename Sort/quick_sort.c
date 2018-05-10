#include <stdio.h>

int int_array_[] = {45, 50, 60, 10, 20, 55, 20, 9, 1, 2};

const int ARRAY_COUNT = 10;

void swap(int i, int j) {
	int temp = int_array_[i];
	int_array_[i] = int_array_[j];
	int_array_[j] = temp;
}

void quick_sort(int p_start_index, int p_end_index) {
	if(p_start_index >= p_end_index) {
		return;
	}

	int base_num = int_array_[p_start_index];
	int point_i = p_start_index;
	int point_j = p_end_index;

	while(point_i != point_j) {
		while(point_i < point_j && int_array_[point_j] >= base_num) {
			point_j --;
		}
		while(point_i < point_j && int_array_[point_i] <= base_num) {
			point_i ++;
		}
		// 如果是已经排序好的就直接退出
		// 交换
		if(point_i < point_j) {
			swap(point_i, point_j);
		}
	}
	//	
	swap(p_start_index, point_i);
	//
	quick_sort(p_start_index, point_i - 1);
	quick_sort(point_i + 1, p_end_index);
}

int main(void) {

	for (int i = 0; i < ARRAY_COUNT; i++) {
		printf("%d, ", int_array_[i]);
	}

	quick_sort(0, ARRAY_COUNT - 1);

	printf("\n");

	for (int i = 0; i < ARRAY_COUNT; i++) {
		printf("%d, ", int_array_[i]);
	}

	return 0;	
}
