#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<Windows.h>
#define MAXN 2020
#define M_MAXN 50
#define Hyperparameter 20
using namespace std;

// The bmp FileHeader length is 14
#define BITMAPFILEHEADERLENGTH 14
// The ASCII code for BM
#define BM 19778

//Coordinate system
double Cs[210];

// OffSet from Header part to Data Part
unsigned int* OffSet;

long long* width;
long long* height;

unsigned char r[MAXN][MAXN], output_r[MAXN][MAXN];
unsigned char g[MAXN][MAXN], output_g[MAXN][MAXN];
unsigned char b[MAXN][MAXN], output_b[MAXN][MAXN];

unsigned char R_resized[MAXN][MAXN];
unsigned char G_resized[MAXN][MAXN];
unsigned char B_resized[MAXN][MAXN];

//Quick sort
struct value {
	//value
	int key;
	//Sequence
	int num;
};
typedef value value;

int partition(vector<value> &arr, int p, int r) {
	int x = arr[r].key;
	int i = p - 1;
	for (int j = p; j <= r - 1; j++) {
		if (arr[j].key <= x) {
			i += 1;
			swap(arr[i], arr[j]);
		}
	}
	swap(arr[i + 1], arr[r]);
	return i + 1;
}
//recursion
void QuickSort(vector<value> &arr, int p, int r) {
	if (p < r) {
		int q = partition(arr, p, r);
		QuickSort(arr, p, q - 1);
		QuickSort(arr, q + 1, r);
	}
}

//Test the file is bmp file or not
void bmpFileTest(FILE* fpbmp) {
	unsigned short* bfType;
	bfType = (unsigned short*)malloc(sizeof(unsigned short));
	fseek(fpbmp, 0L, SEEK_SET);
	fread(bfType, sizeof(char), 2, fpbmp);
	if (BM != (*bfType)) {
		printf("This file is not bmp file.\n");
		//system("pause");
		exit(1);
	}
}

//To get the OffSet of header to data part
void bmpHeaderPartLength(FILE* fpbmp) {
	fseek(fpbmp, 10L, SEEK_SET);
	fread(OffSet, sizeof(char), 4, fpbmp);
	printf("The Header Part is of length %d.\n", (*OffSet));
}

//To get the width and height of the bmp file
void BmpWidthHeight(FILE* fpbmp) {
	fseek(fpbmp, 18L, SEEK_SET);
	fread(width, sizeof(char), 4, fpbmp);
	fseek(fpbmp, 22L, SEEK_SET);
	fread(height, sizeof(char), 4, fpbmp);
	printf("The Width of the bmp file is %ld.\n", (*width));
	printf("The Height of the bmp file is %ld.\n", (*height));
}

//Get R,G,B data
void bmpDataPart(FILE* fpbmp) {
	int i, j = 0;
	int stride;
	unsigned char* pix = NULL;

	FILE* fpr;
	FILE* fpg;
	FILE* fpb;

	if ((fpr = fopen("bmpr.txt", "w+")) == NULL) {
		printf("Failed to construct file bmpr.txt.");
		//system("pause");
		exit(1);
	}

	if ((fpg = fopen("bmpg.txt", "w+")) == NULL) {
		printf("Failed to construct file bmpg.txt.");
		//system("pause");
		exit(1);
	}

	if ((fpb = fopen("bmpb.txt", "w+")) == NULL) {
		printf("Failed to construct file bmpb.txt.");
		//system("pause");
		exit(1);
	}

	fseek(fpbmp, (*OffSet), SEEK_SET);
	stride = (24 * (*width) + 31) / 8;
	stride = stride / 4 * 4;
	pix = (unsigned char *)malloc(stride);

	for (j = 0; j < (*height); j++) {
		fread(pix, 1, stride, fpbmp);
		for (i = 0; i < (*width); i++) {
			r[(*height) - 1 - j][i] = pix[i * 3 + 2];
			g[(*height) - 1 - j][i] = pix[i * 3 + 1];
			b[(*height) - 1 - j][i] = pix[i * 3];

			output_r[(*height) - 1 - j][i] = pix[i * 3 + 2];
			output_g[(*height) - 1 - j][i] = pix[i * 3 + 1];
			output_b[(*height) - 1 - j][i] = pix[i * 3];
		}
	}

	for (i = 0; i < (*height); i++) {
		for (j = 0; j < (*width) - 1; j++) {
			fprintf(fpb, "%4d", b[i][j]);
			fprintf(fpg, "%4d", g[i][j]);
			fprintf(fpr, "%4d", r[i][j]);
		}
		fprintf(fpb, "%4d\n", b[i][j]);
		fprintf(fpg, "%4d\n", g[i][j]);
		fprintf(fpr, "%4d\n", r[i][j]);
	}

	fclose(fpr);
	fclose(fpg);
	fclose(fpb);
}

//Output data to corresponding txt file
void bmpoutput(FILE* fpout) {
	int i, j = 0;
	int stride;
	unsigned char* pixout = NULL;

	stride = (24 * (*width) + 31) / 8;
	stride = stride / 4 * 4;
	pixout = (unsigned char*)malloc(stride);

	fseek(fpout, (*OffSet), SEEK_SET);

	for (j = 0; j < (*height); j++) {
		for (i = 0; i < (*width); i++) {
			pixout[i * 3 + 2] = output_r[(*height) - 1 - j][i];
			pixout[i * 3 + 1] = output_g[(*height) - 1 - j][i];
			pixout[i * 3] = output_b[(*height) - 1 - j][i];
		}
		fwrite(pixout, 1, stride, fpout);
	}
}

//initialization
void init() {
	OffSet = (unsigned int*)malloc(sizeof(unsigned int));
	width = (long long*)malloc(sizeof(long long));
	height = (long long*)malloc(sizeof(long long));

	*OffSet = 0;
	*width = 0;
	*height = 0;
}

//If open
void ifopen(FILE* temp) {
	if (temp == NULL) {
		printf("Open bmp failed.\n");
		//system("pause");
		exit(1);
	}
}

void saveHEADERFILE(FILE* in, FILE* out) {
	fseek(in, 0L, SEEK_SET);
	fseek(out, 0L, SEEK_SET);

	unsigned char* fp_temp;
	fp_temp = (unsigned char *)malloc((*OffSet));
	fread(fp_temp, 1, (*OffSet), in);
	fwrite(fp_temp, 1, (*OffSet), out);
}

//A better denoise
//Storage
int** IMG;
int RB[200][200];
int idx[200][200];

//DFS
//If use DFS will stack overflow
//Should add 
//"#pragma comment(linker, "/STACK:10456000000,10456000000")"
//But not really worked
//So, use BFS
/*
void DFS(int r, int c, int FindWhat, int id) {
	if (r < 0 || r >= 200 || c < 0 || c >= 200) { return; }
	if (idx[r][c] > 0 || RB[r][c] != FindWhat) { return; }

	idx[r][c] = id;
	for (int dr = -1; dr <= 1; dr++) {
		for (int dc = -1; dc <= 1; dc++) {
			if (dr != 0 || dc != 0)
				DFS(r + dr, c + dc, FindWhat, id);
		}
	}
}
*/
//BFS
//Storage
struct Node {
	int x;
	int y;
};
typedef Node Node;
int dir[8][2] = { { 1,0 },{ -1,0 },{ 0,1 },{ 0,-1 },{ 1,1 },{ -1,1 },{ 1,-1 },{ -1,-1 } };

void BFS(int r, int c, int FindWhat, int id) {
	//int dir[8][2];
	//int cnt = 0;
	queue<Node> Q;
	/*for (int i = -1; i <= 1; i++) {
		for (int j = -1; j <= 1; j++) {
			if (i != 0 && j != 0) {
				dir[cnt][0] = i;
				dir[cnt++][1] = j;
			}
		}
	}*/
	/*for (int i = 0; i < 8; i++) {
		cout << dir[i][0] << " ";
		cout << dir[i][1] << endl;
	}*/

	Node node;
	node.x = r;
	node.y = c;
	Q.push(node);
	//cout << "Done" << endl;
	while (!Q.empty()) {
		Node cur = Q.front();
		Node next;
		Q.pop();
		for (int i = 0; i < 8; i++) {
			next.x = cur.x + dir[i][0];
			next.y = cur.y + dir[i][1];
			if (next.x >= 0 && next.x < 200 && next.y >= 0 && next.y < 200) {
				if (RB[next.x][next.y] == FindWhat && idx[next.x][next.y] == 0) {
					idx[next.x][next.y] = id;
					Q.push(next);
				}
			}
		}
	}
}


void BetterDenoise() {
	//4*4 Kernel
	for (int i = 0; i < 200 - 4 + 1; i++) {
		for (int j = 0; j < 200 - 4 + 1; j++) {
			int sum = 0;
			for (int x = 0; x < 4; x++) {
				for (int y = 0; y < 4; y++) {
					sum += IMG[i + x][j + y];
				}
			}
			if (sum >= 12) {
				for (int m = 0; m < 4; m++) {
					for (int n = 0; n < 4; n++) {
						RB[i + m][j + n] = 1;
					}
				}
			}
		}
	}

	//DFS over there
	/*
	//Graph-connected
	memset(idx, 0, sizeof(idx));
	vector<int> Aera;

	int cnt = 0;
	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 200; j++) {
			if (idx[i][j] == 0 && RB[i][j] == 1) {
				DFS(i, j, 1, ++cnt);
			}
		}
	}

	Aera.resize(cnt);
	for (int k = 0; k < cnt; k++) { Aera[k] = 0; }
	for (int x = 0; x < 200; x++) {
		for (int y = 0; y < 200; y++) {
			if (idx[x][y] > 0) { Aera[idx[x][y] - 1]++; }
		}
	}
	//for (int y = 0; y < cnt; y++) {
	//	cout << Aera[y] << endl;
	//}
	//Get max
	int Max = 0, key;
	for (int i = 0; i < cnt; i++) {
		if (Aera[i] > Max) {
			Max = Aera[i];
			key = i + 1;
		}
	}
	for (int a = 0; a < 200; a++) {
		for (int b = 0; b < 200; b++) {
			if (idx[a][b] != key) {
				RB[a][b] = 0;
			}
		}
	}
	*/

	//BFS over there
	//Graph-connected

	//For 1
	memset(idx, 0, sizeof(idx));
	vector<int> Aera_1;

	int cnt = 0;
	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 200; j++) {
			if (idx[i][j] == 0 && RB[i][j] == 1) {
				BFS(i, j, 1, ++cnt);
				//cout << "Done" << endl;
			}
		}
	}
	//cout << "Done" << endl;

	Aera_1.resize(cnt);
	for (int k = 0; k < cnt; k++) { Aera_1[k] = 0; }
	for (int x = 0; x < 200; x++) {
		for (int y = 0; y < 200; y++) {
			if (idx[x][y] > 0) { Aera_1[idx[x][y] - 1]++; }
		}
	}

	//Get max
	int Max = 0, key;
	for (int i = 0; i < cnt; i++) {
		if (Aera_1[i] > Max) {
			Max = Aera_1[i];
			key = i + 1;
		}
	}
	for (int a = 0; a < 200; a++) {
		for (int b = 0; b < 200; b++) {
			if (idx[a][b] != key) {
				RB[a][b] = 0;
			}
		}
	}

	//For 0
	memset(idx, 0, sizeof(idx));
	vector<int> Aera_2;

	int Cnt = 0;
	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 200; j++) {
			if (idx[i][j] == 0 && RB[i][j] == 0) {
				BFS(i, j, 0, ++Cnt);
				//cout << "Done" << endl;
			}
		}
	}
	//cout << "Done" << endl;

	Aera_2.resize(Cnt);
	for (int k = 0; k < Cnt; k++) { Aera_2[k] = 0; }
	for (int x = 0; x < 200; x++) {
		for (int y = 0; y < 200; y++) {
			if (idx[x][y] > 0) { Aera_2[idx[x][y] - 1]++; }
		}
	}

	//Get two bigger
	vector<int> Key;
	for (int i = 0; i < Cnt; i++) {
		if (Aera_2[i] < 100) {
			Key.push_back(i + 1);
		}
	}
	for (int a = 0; a < 200; a++) {
		for (int b = 0; b < 200; b++) {
			for (int c = 0; c < Key.size(); c++) {
				if (idx[a][b] == Key[c])
					RB[a][b] = 1;
			}
		}
	}

	FILE* Temp;
	Temp = fopen("BetterDenoise.txt", "wb+");
	fclose(Temp);
	ofstream location_out;
	location_out.open("BetterDenoise.txt", std::ios::out | std::ios::app);
	int i = 0, j = 0;
	for (i = 0; i < 200; i++) {
		for (j = 0; j < 200; j++) {
			if (RB[i][j] == 1) { location_out << ". "; }
			else
				location_out << " ";
		}
		location_out << endl;
	}
}

//Image process
int** processImage(FILE* out, int width, int height) {
	//Storage
	static int** Pic;
	Pic = (int**)malloc(height * sizeof(int *));
	int i = 0;
	for (i = 0; i < height; i++)
		Pic[i] = (int*)malloc(width * sizeof(int));

	int x = 0, y = 0;
	for (x = 0; x < height; x++) {
		for (y = 0; y < width; y++) {
			double R = R_resized[x][y];
			double G = G_resized[x][y];
			double B = B_resized[x][y];
			double ave = (R + G + B) / 3.0;
			double D_R = ((R - ave) > 0) ? (R - ave) : (ave - R);
			double D_G = ((G - ave) > 0) ? (G - ave) : (ave - G);
			double D_B = ((B - ave) > 0) ? (B - ave) : (ave - B);
			double deviation = (D_R + D_G + D_B) / 3.0;

			if (deviation > Hyperparameter)
				Pic[x][y] = 1;
			else
				Pic[x][y] = 0;
		}
	}

	//For IMG
	IMG = Pic;

	//Noise reduction
	double increment = 110.0 / 200.0;
	//cout << increment << endl;
	for (int kase = 0; kase < 200; kase++) {
		double tempKase = kase;
		double cnt_b = 14.0 + increment * tempKase;
		int cnt = cnt_b;
		//cout << cnt << endl;

		vector<value> arr_value;
		arr_value.clear();
		for (int i = 0; i < 200 - cnt - 1; i++) {
			int sum = 0;
			for (int j = 0; j <= cnt; j++) {
				sum += Pic[kase][i + j];
			}
			value temp;
			//cout << sum << endl;
			temp.key = sum;
			temp.num = i;
			arr_value.push_back(temp);
		}
		QuickSort(arr_value, 0, arr_value.size() - 1);

		double mid;
		int start = arr_value[arr_value.size() - 1].num;
		//cout << start << endl;
		mid = (start + start + cnt) / 2.0;
		Cs[kase] = mid;
	}

	return Pic;
}

void resizePic(FILE* in, FILE* out, FILE* sample, int reWidth, int reHeight) {
	int i = 0, j = 0;
	int x = 0, y = 0;
	int stride;
	unsigned char* pix = NULL;

	fseek(in, (*OffSet), SEEK_SET);
	stride = (24 * (*width) + 31) / 8;
	stride = stride / 4 * 4;
	pix = (unsigned char *)malloc(stride);

	for (j = 0; j < (*height); j++) {
		fread(pix, 1, stride, in);
		for (i = 0; i < (*width); i++) {
			r[(*height) - 1 - j][i] = pix[i * 3 + 2];
			g[(*height) - 1 - j][i] = pix[i * 3 + 1];
			b[(*height) - 1 - j][i] = pix[i * 3];
		}
	}
	//INTER_LINEAR
	double tempRW = reWidth;
	double tempRH = reHeight;
	double tempW = (*width);
	double tempH = (*height);
	double proportion_W = tempRW / tempW;
	double proportion_H = tempRH / tempH;

	for (x = 0; x < reHeight; x++) {
		for (y = 0; y < reWidth; y++) {
			int xx = (int)(x / proportion_H);
			int yy = (int)(y / proportion_W);
			int xx_1, yy_1;
			xx_1 = (xx + 1 < (*height)) ? (xx + 1) : xx;
			yy_1 = (yy + 1 < (*width)) ? (yy + 1) : yy;

			if (xx == xx_1 || yy == yy_1) {
				R_resized[x][y] = r[xx][yy];
				G_resized[x][y] = g[xx][yy];
				B_resized[x][y] = b[xx][yy];
			}
			else {
				double deviation_X = x - xx;
				double deviation_Y = y - yy;

				double first = (1.0 - deviation_X)*(1.0 - deviation_Y);
				double second = (1.0 - deviation_X)*deviation_Y;
				double third = deviation_X * (1.0 - deviation_Y);
				double fourth = deviation_X * deviation_Y;

				double temp_0_0_R = r[xx][yy];
				double temp_0_0_G = g[xx][yy];
				double temp_0_0_B = b[xx][yy];

				double temp_0_1_R = r[xx][yy_1];
				double temp_0_1_G = g[xx][yy_1];
				double temp_0_1_B = b[xx][yy_1];

				double temp_1_0_R = r[xx_1][yy];
				double temp_1_0_G = g[xx_1][yy];
				double temp_1_0_B = b[xx_1][yy];

				double temp_1_1_R = r[xx_1][yy_1];
				double temp_1_1_G = g[xx_1][yy_1];
				double temp_1_1_B = b[xx_1][yy_1];

				double temp_R_1 = first * temp_0_0_R + second * temp_0_1_R;
				double temp_R_2 = third * temp_1_0_R + fourth * temp_1_1_R;
				R_resized[x][y] = (int)(temp_R_1 + temp_R_2);
				double temp_G_1 = first * temp_0_0_G + second * temp_0_1_G;
				double temp_G_2 = third * temp_1_0_G + fourth * temp_1_1_G;
				G_resized[x][y] = (int)(temp_G_1 + temp_G_2);
				double temp_B_1 = first * temp_0_0_B + second * temp_0_1_B;
				double temp_B_2 = third * temp_1_0_B + fourth * temp_1_1_B;
				B_resized[x][y] = (int)(temp_B_1 + temp_B_2);
			}
		}
	}

	int Stride;
	unsigned char* pix_out = NULL;

	Stride = (24 * (reWidth)+31) / 8;
	Stride = Stride / 4 * 4;
	pix_out = (unsigned char*)malloc(Stride);

	int offset = 54;
	fseek(out, 0L, SEEK_SET);
	fseek(sample, 0L, SEEK_SET);
	//fseek(in, 0L, SEEK_SET);

	unsigned char* fp_temp;
	fp_temp = (unsigned char *)malloc((offset));
	fread(fp_temp, 1, offset, sample);
	//fread(fp_temp, 1, offset, in);
	fwrite(fp_temp, 1, offset, out);

	for (j = 0; j < (reHeight); j++) {
		for (i = 0; i < (reWidth); i++) {
			pix_out[i * 3 + 2] = R_resized[(reHeight)-1 - j][i];
			pix_out[i * 3 + 1] = G_resized[(reHeight)-1 - j][i];
			pix_out[i * 3] = B_resized[(reHeight)-1 - j][i];
		}
		fwrite(pix_out, 1, stride, out);
	}
}


//Matrix operation
//Define a mat
struct Matrix {
	vector<vector<double> > matrix;
	int height;
	int width;
};
typedef Matrix Matrix;

//Get matrix
Matrix getMatrix(double** mat_in, int height, int width) {
	static Matrix out;
	out.height = height;
	out.width = width;

	out.matrix.resize(height);
	for (int i = 0; i < out.height; i++) {
		out.matrix[i].resize(out.width);
	}

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			out.matrix[i][j] = mat_in[i][j];
		}
	}

	return out;
}

//Print matrix
void printMat(Matrix in) {
	for (int i = 0; i < in.height; i++) {
		for (int j = 0; j < in.width; j++) {
			cout << in.matrix[i][j];
			cout << " ";
		}
		cout << endl;
	}
	cout << endl;
}

//Add
Matrix add(Matrix one, Matrix two) {
	static Matrix out;
	out.height = one.height;
	out.width = one.width;

	out.matrix.resize(one.height);
	for (int i = 0; i < one.height; i++) {
		out.matrix[i].resize(one.width);
	}

	if (one.height == two.height && one.width == two.width) {
		for (int i = 0; i < one.height; i++) {
			for (int j = 0; j < one.width; j++) {
				out.matrix[i][j] = one.matrix[i][j] + two.matrix[i][j];
			}
		}
	}
	else {
		cout << "ERROR" << endl;
		system("pause");
		exit(1);
	}

	return out;
}

//Multiply
Matrix multiply(Matrix one, Matrix two) {
	static Matrix out;
	out.height = one.height;
	out.width = two.width;

	out.matrix.resize(one.height);
	for (int i = 0; i < one.height; i++) {
		out.matrix[i].resize(two.width);
	}

	if (one.width == two.height) {
		for (int i = 0; i < one.height; i++) {
			for (int j = 0; j < two.width; j++) {
				int sum = 0;
				for (int k = 0; k < one.width; k++) {
					sum += one.matrix[i][k] * two.matrix[k][j];
				}
				out.matrix[i][j] = sum;
			}
		}
		return out;
	}
	else {
		cout << "ERROR" << endl;
		system("pause");
		exit(1);
	}
}

//Transpose matrix
Matrix TransposedMat(Matrix in) {
	static Matrix out;
	out.height = in.width;
	out.width = in.height;

	out.matrix.resize(in.width);
	for (int i = 0; i < in.width; i++) {
		out.matrix[i].resize(in.height);
	}

	for (int i = 0; i < in.width; i++) {
		for (int j = 0; j < in.height; j++) {
			out.matrix[i][j] = in.matrix[j][i];
		}
	}
	return out;
}

//Determinant
double determinant(double a[][M_MAXN], int dimension);
void spread(double a[][M_MAXN], int row, int dimension);
void copy_m(double src[][M_MAXN], double dst[][M_MAXN], int dimension);

double Determinant(Matrix in) {
	double A[M_MAXN][M_MAXN];
	for (int i = 0; i < in.height; i++) {
		for (int j = 0; j < in.width; j++) {
			A[i][j] = in.matrix[i][j];
		}
	}

	double sum = determinant(A, in.height);
	return sum;
}
double determinant(double a[][M_MAXN], int dimension) {
	double sum = 0;
	double m_copy[M_MAXN][M_MAXN];
	memset(m_copy, 0, sizeof(m_copy));
	copy_m(a, m_copy, dimension);
	if (dimension == 2) {
		double result = a[0][0] * a[1][1] - a[0][1] * a[1][0];
		return result;
	}
	for (int i = 0; i < dimension; i++) {
		if (a[i][dimension - 1] - 0 < 0.000001)
			continue;
		spread(a, i, dimension);
		double tmp = a[i][dimension - 1] * determinant(a, dimension - 1);
		int sign = (i + 1 + dimension) % 2 == 0 ? 1 : (-1);
		sum += (double)sign * tmp;
		copy_m(m_copy, a, dimension);
	}
	return sum;
}
void spread(double a[][M_MAXN], int row, int dimension) {
	if (row == dimension - 1)
		return;
	for (int i = row; i < dimension - 1; i++)
		for (int j = 0; j < dimension - 1; j++)
			a[i][j] = a[i + 1][j];
}

void copy_m(double src[][M_MAXN], double dst[][M_MAXN], int dimension) {
	for (int i = 0; i < dimension; i++)
		for (int j = 0; j < dimension; j++)
			dst[i][j] = src[i][j];
}

//Adjugate matrix
double AlgebraMinor(Matrix in, int i, int j);

Matrix AdjugateMatrix(Matrix in) {
	Matrix temp;
	temp.height = in.height;
	temp.width = in.width;

	temp.matrix.resize(in.height);
	for (int i = 0; i < in.height; i++) {
		temp.matrix[i].resize(in.width);
	}

	for (int i = 0; i < temp.height; i++) {
		for (int j = 0; j < temp.width; j++) {
			temp.matrix[i][j] = AlgebraMinor(in, i, j);
		}
	}

	static Matrix out = TransposedMat(temp);
	return out;
}

double AlgebraMinor(Matrix in, int i, int j) {
	Matrix temp;
	temp.height = in.height - 1;
	temp.width = in.width - 1;

	temp.matrix.resize(in.height - 1);
	for (int i = 0; i < in.height - 1; i++) {
		temp.matrix[i].resize(in.width - 1);
	}

	int kase_1 = 0, kase_2 = 0;
	for (int x = 0; x < in.height; x++) {
		kase_2 = 0;
		if (x != i) {
			for (int y = 0; y < in.width; y++) {
				if (y != j) {
					temp.matrix[kase_1][kase_2] = in.matrix[x][y];
					kase_2++;
				}
			}
			kase_1++;
		}
	}

	double out = Determinant(temp);
	return out;
}


//Multi factor line regression method
//Factor
struct factor {
	double A_2;
	double A_1;
	double A_0;
};
typedef factor factor;

//The factor of multi factor line regression
factor arr_factor[10];

void MFLRM_operation(int cnt);

void MFLRM() {
	//Operation to Cs
	FILE *temp;
	temp = fopen("factor.txt", "wb");
	fclose(temp);

	//Devide array into ten
	for (int cnt = 1; cnt <= 10; cnt++) {
		MFLRM_operation(cnt);
	}

	ofstream location_out;
	location_out.open("factor.txt", std::ios::out | std::ios::app);
	int i = 0, j = 0;
	for (i = 0; i < 10; i++) {
		location_out << arr_factor[i].A_2 << " ";
		cout << arr_factor[i].A_2 << " ";
		location_out << arr_factor[i].A_1 << " ";
		cout << arr_factor[i].A_1 << " ";
		location_out << arr_factor[i].A_0 << endl;
		cout << arr_factor[i].A_0 << endl;
	}
	location_out.close();
}

//Operation
void MFLRM_operation(int cnt) {
	Matrix X;
	Matrix Y;

	X.height = 20;
	X.width = 3;
	X.matrix.resize(20);
	for (int i = 0; i < 20; i++) {
		X.matrix[i].resize(3);
	}

	Y.height = 20;
	Y.width = 1;
	Y.matrix.resize(20);
	for (int i = 0; i < 20; i++) {
		Y.matrix[i].resize(1);
	}

	for (int i = 0; i < X.height; i++) {
		for (int j = 0; j < X.width; j++) {
			X.matrix[i][j] = pow(((cnt - 1) * 20 + 1 + i), j);
		}
	}

	for (int i = 0; i < Y.height; i++) {
		Y.matrix[i][0] = Cs[(cnt - 1) * 20 + i];
	}

	printMat(X);
	Matrix XT = TransposedMat(X);
	//cout << XT.height << " " << XT.width << endl;
	Matrix XTX = multiply(XT, X);
	//cout << "Done one" << endl;

	double IXTXI = Determinant(XTX);
	Matrix XTXX = AdjugateMatrix(XTX);
	//cout << XTXX.height << " " << XTXX.width << endl;
	//cout << "Done two" << endl;

	Matrix tempOne = multiply(XTXX, XT);
	//cout << tempOne.height << " " << tempOne.width << endl;
	Matrix tempTwo = multiply(tempOne, Y);
	//cout << "Done three" << endl;

	double result_2 = (1.0 / IXTXI)*tempTwo.matrix[2][0];
	arr_factor[cnt - 1].A_2 = result_2;
	double result_1 = (1.0 / IXTXI)*tempTwo.matrix[1][0];
	arr_factor[cnt - 1].A_1 = result_1;
	double result_0 = (1.0 / IXTXI)*tempTwo.matrix[0][0];
	arr_factor[cnt - 1].A_0 = result_0;
}

//Not important
void NotImportant(int** temp) {
	//Not important
	FILE *tempFile;
	tempFile = fopen("pic.txt", "wb");
	fclose(tempFile);

	ofstream location_out;
	location_out.open("pic.txt", std::ios::out | std::ios::app);
	int i = 0, j = 0;
	for (i = 0; i < 200; i++) {
		for (j = 0; j < 200; j++) {
			if (temp[i][j] == 1) { location_out << "."; }
			else
				location_out << " ";
		}
		location_out << endl;
	}

	////Print coordinate system
	//for (int m = 0; m < 200; m++)
	//	cout << Cs[m] << endl;

	location_out.close();
}

//Return angle
void returnAngle() {
	FILE *Temp;
	Temp = fopen("angle.txt", "wb");
	fclose(Temp);

	ofstream location_out;
	location_out.open("angle.txt", std::ios::out | std::ios::app);
	int i = 0;
	for (i = 0; i < 200; i++) {
		int NorP;
		double angle;
		double dif = (100 - Cs[i] >= 0) ? (100 - Cs[i]) : (Cs[i] - 100);
		if (100 - Cs[i] < 0) { NorP = 1; }
		else { NorP = -1; }
		//The value of angle should be expanded
		angle = 90.0 + NorP * atan(dif / 200);

		location_out << angle << endl;
	}

	location_out.close();
}

int main() {
	init();
	FILE *fpbmp;
	FILE *fpout;
	FILE *fpout_resized_sample;
	FILE *fpout_resized;
	FILE *Angle;

	fpbmp = fopen("in.bmp", "rb");
	fpout = fopen("out.bmp", "wb+");
	fpout_resized_sample = fopen("sample.bmp", "rb");
	fpout_resized = fopen("resized.bmp", "wb+");
	Angle = fopen("angle.txt", "wb+");
	ifopen(Angle);
	ifopen(fpout_resized_sample);
	ifopen(fpout_resized);
	ifopen(fpbmp);
	ifopen(fpout);

	bmpFileTest(fpbmp);
	bmpHeaderPartLength(fpbmp);
	BmpWidthHeight(fpbmp);
	bmpDataPart(fpbmp);
	saveHEADERFILE(fpbmp, fpout);
	bmpoutput(fpout);

	//Process picture
	resizePic(fpbmp, fpout_resized, fpout_resized_sample, 200, 200);
	int** temp = processImage(Angle, 200, 200);

	NotImportant(temp);
	returnAngle();

	////Multi factor line regression method
	//MFLRM();

	//Better denoise
	BetterDenoise();

	//location_out.close();
	fclose(Angle);
	fclose(fpout_resized);
	fclose(fpout_resized_sample);
	fclose(fpbmp);
	fclose(fpout);
	system("pause");
	return 0;
}
