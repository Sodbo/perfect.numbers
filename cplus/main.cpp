# include <iostream>
# include <math.h>
# include <omp.h>  

// Runtime HZM ubuntu
// Runtime 10.822s laptop

int main(int argc, char* argv[]){

	int N = 2000000;
	std::cout << "Starting ride!\n\n";

	omp_set_num_threads(2); 
	#pragma omp parallel for
	for (int i=2; i<N+1; i++){
		int a = 1;
		for (int del=2; del<round(sqrt(i))+1;del++){
			if (i%del == 0){
				a = a + del + i/del;
			}
		}

		if (a == i)
			std::cout << "Perfect number " << a << '\n';
	}
	std::cout << '\n';
	return(0);
}