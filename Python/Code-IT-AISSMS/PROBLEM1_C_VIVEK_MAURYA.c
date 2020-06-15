#include<stdio.h>

int main(int argc, char *argv[])
{
	int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};		
//	int arr[] = {3,2,5};
//  int arr[] = {9, 8, 10, 7, 11, 2, 5};		
//	int arr[] = {1,2};							
//	int arr[] = {2,1,3,4,2,3,1,2,4};		

	int kElemntcount = 0;
	int arrayCount = (sizeof(arr)/sizeof(int));

	if( ( sizeof(arr)/sizeof(int) ) >= 3)
	{	

			for( int i=1;i < (arrayCount-1);i++ )
			{	
				if (arr[(i-1)] > arr[i] && arr[i] < arr[(i+1)] )
				{
					kElemntcount++;
				}
			}
	
			printf("%d",kElemntcount);
	}
	else 
	{	
		printf("Wrong Input");
	}

	return 0;
}