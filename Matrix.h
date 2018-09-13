#pragma once
#include <iostream>
#include <vector>
#include <cmath>
#include <Windows.h>
#define M_MAXN 50
using namespace std;

vector<vector<double> > init_v;

//Define Matrix class
class Matrix
{
	//Matrix
public:
	explicit Matrix(int h = 1, int w = 1, vector<vector<double>> mat = init_v)
		: height(h), width(w)
	{
		if (mat.empty() == true) {
			mat.resize(1);
			mat[0].resize(1);
			mat[0][0] = 0;
			//cout << "Done" << endl;
		}
		//cout << "Done" << endl;
		matrix.resize(height);
		//cout << "Done" << endl;
		for (int i = 0; i < height; i++)
		{
			matrix[i].resize(width);
		}

		if (mat.size() != h || mat[0].size() != w)
		{
			std::cout << "INPUT ERROR!";
			std::cout << std::endl;
			system("pause");
			exit(1);
		}
		else
		{
			for (int i = 0; i < h; i++)
			{
				for (int j = 0; j < w; j++)
				{
					matrix[i][j] = mat[i][j];
				}
			}
		}
	}

	//Initialization
	void init(int h, int w, vector<vector<double>> mat) {
		height = h;
		width = w;

		matrix.resize(height);
		for (int i = 0; i < height; i++)
		{
			matrix[i].resize(width);
		}

		if (mat.size() != h || mat[0].size() != w)
		{
			std::cout << "INPUT ERROR!";
			std::cout << std::endl;
			system("pause");
			exit(1);
		}
		else
		{
			for (int i = 0; i < h; i++)
			{
				for (int j = 0; j < w; j++)
				{
					matrix[i][j] = mat[i][j];
				}
			}
		}
	}

	//Get height
	int getHeight() { return height; }

	//Get width
	int getWidth() { return width; }

	//Get element
	double getElement(int i, int j) { return matrix[i][j]; }

	//Print matirx
	void printMat()
	{
		for (int i = 0; i < height; i++)
		{
			for (int j = 0; j < width; j++)
			{
				cout << matrix[i][j];
				cout << " ";
			}
			cout << endl;
		}
		cout << endl;
	}

	//Add
	Matrix add(Matrix two)
	{
		//cout << "Done" << endl;
		vector<vector<double>> temp;
		temp.resize(height);
		for (int i = 0; i < height; i++)
		{
			temp[i].resize(width);
		}
		//temp.clear();
		static Matrix out(height, width, temp);
		//cout << "Done" << endl;

		if (height == two.height && width == two.width)
		{
			for (int i = 0; i < height; i++)
			{
				for (int j = 0; j < width; j++)
				{
					out.matrix[i][j] = matrix[i][j] + two.matrix[i][j];
				}
			}
		}
		else
		{
			cout << "ERROR" << endl;
			system("pause");
			exit(1);
		}

		return out;
	}

	//Multiply
	Matrix multiply(Matrix two)
	{
		vector<vector<double>> temp;
		temp.resize(height);
		for (int i = 0; i < height; i++)
		{
			temp[i].resize(two.getWidth());
		}
		//temp.clear();
		static Matrix out(height, two.getWidth(), temp);

		if (width == two.height)
		{
			for (int i = 0; i < height; i++)
			{
				for (int j = 0; j < two.width; j++)
				{
					int sum = 0;
					for (int k = 0; k < width; k++)
					{
						sum += matrix[i][k] * two.matrix[k][j];
					}
					out.matrix[i][j] = sum;
				}
			}
			return out;
		}
		else
		{
			cout << "ERROR" << endl;
			system("pause");
			exit(1);
		}
	}

	//Transpose matrix
	Matrix TransposedMat()
	{
		vector<vector<double>> temp;
		temp.resize(width);
		for (int i = 0; i < width; i++)
		{
			temp[i].resize(height);
		}
		//temp.clear();
		static Matrix out(width, height, temp);

		for (int i = 0; i < width; i++)
		{
			for (int j = 0; j < height; j++)
			{
				out.matrix[i][j] = matrix[j][i];
			}
		}
		return out;
	}

	//Determinant
	double Determinant()
	{
		if (height == 1 && width == 1)
		{
			return matrix[0][0];
		}

		double A[M_MAXN][M_MAXN];
		for (int i = 0; i < height; i++)
		{
			for (int j = 0; j < width; j++)
			{
				A[i][j] = matrix[i][j];
			}
		}

		double sum = determinant(A, height);
		return sum;
	}

	//Adjugate matrix
	Matrix AdjugateMatrix()
	{
		vector<vector<double>> Temp;
		Temp.resize(height);
		for (int i = 0; i < height; i++)
		{
			Temp[i].resize(width);
		}
		//Temp.clear();
		Matrix temp(height, width, Temp);

		for (int i = 0; i < temp.height; i++)
		{
			for (int j = 0; j < temp.width; j++)
			{
				temp.matrix[i][j] = AlgebraMinor(i, j);
				//cout << AlgebraMinor(i, j) << endl;
			}
		}

		static Matrix out = temp.TransposedMat();
		return out;
	}

private:
	int height;
	int width;
	vector<vector<double>> matrix;

	//Determinant
	double determinant(double a[][M_MAXN], int dimension)
	{
		double sum = 0;
		double m_copy[M_MAXN][M_MAXN];
		memset(m_copy, 0, sizeof(m_copy));
		copy_m(a, m_copy, dimension);
		if (dimension == 2)
		{
			double result = a[0][0] * a[1][1] - a[0][1] * a[1][0];
			return result;
		}
		for (int i = 0; i < dimension; i++)
		{
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

	void spread(double a[][M_MAXN], int row, int dimension)
	{
		if (row == dimension - 1)
			return;
		for (int i = row; i < dimension - 1; i++)
			for (int j = 0; j < dimension - 1; j++)
				a[i][j] = a[i + 1][j];
	}

	void copy_m(double src[][M_MAXN], double dst[][M_MAXN], int dimension)
	{
		for (int i = 0; i < dimension; i++)
			for (int j = 0; j < dimension; j++)
				dst[i][j] = src[i][j];
	}

	//Adjugate matrix
	double AlgebraMinor(int i, int j)
	{
		vector<vector<double>> Temp;
		Temp.resize(height - 1);
		for (int i = 0; i < height - 1; i++)
		{
			Temp[i].resize(width - 1);
		}
		//Temp.clear();
		Matrix temp(height - 1, width - 1, Temp);

		int kase_1 = 0, kase_2 = 0;
		for (int x = 0; x < height; x++)
		{
			kase_2 = 0;
			if (x != i)
			{
				for (int y = 0; y < width; y++)
				{
					if (y != j)
					{
						temp.matrix[kase_1][kase_2] = matrix[x][y];
						//cout << matrix[x][y] << endl;
						kase_2++;
					}
				}
				kase_1++;
			}
		}

		//cout << temp.Determinant() << endl;
		double out = temp.Determinant() * pow(-1.0, i + j);
		return out;
	}
};

////Matrix operation
////Define a mat
//struct Matrix {
//	vector<vector<double> > matrix;
//	int height;
//	int width;
//};
//typedef Matrix Matrix;
//
////Get matrix
//Matrix getMatrix(double** mat_in, int height, int width) {
//	static Matrix out;
//	out.height = height;
//	out.width = width;
//
//	out.matrix.resize(height);
//	for (int i = 0; i < out.height; i++) {
//		out.matrix[i].resize(out.width);
//	}
//
//	for (int i = 0; i < height; i++) {
//		for (int j = 0; j < width; j++) {
//			out.matrix[i][j] = mat_in[i][j];
//		}
//	}
//
//	return out;
//}
//
////Print matrix
//void printMat(Matrix in) {
//	for (int i = 0; i < in.height; i++) {
//		for (int j = 0; j < in.width; j++) {
//			cout << in.matrix[i][j];
//			cout << " ";
//		}
//		cout << endl;
//	}
//	cout << endl;
//}
//
////Add
//Matrix add(Matrix one, Matrix two) {
//	static Matrix out;
//	out.height = one.height;
//	out.width = one.width;
//
//	out.matrix.resize(one.height);
//	for (int i = 0; i < one.height; i++) {
//		out.matrix[i].resize(one.width);
//	}
//
//	if (one.height == two.height && one.width == two.width) {
//		for (int i = 0; i < one.height; i++) {
//			for (int j = 0; j < one.width; j++) {
//				out.matrix[i][j] = one.matrix[i][j] + two.matrix[i][j];
//			}
//		}
//	}
//	else {
//		cout << "ERROR" << endl;
//		system("pause");
//		exit(1);
//	}
//
//	return out;
//}
//
////Multiply
//Matrix multiply(Matrix one, Matrix two) {
//	static Matrix out;
//	out.height = one.height;
//	out.width = two.width;
//
//	out.matrix.resize(one.height);
//	for (int i = 0; i < one.height; i++) {
//		out.matrix[i].resize(two.width);
//	}
//
//	if (one.width == two.height) {
//		for (int i = 0; i < one.height; i++) {
//			for (int j = 0; j < two.width; j++) {
//				int sum = 0;
//				for (int k = 0; k < one.width; k++) {
//					sum += one.matrix[i][k] * two.matrix[k][j];
//				}
//				out.matrix[i][j] = sum;
//			}
//		}
//		return out;
//	}
//	else {
//		cout << "ERROR" << endl;
//		system("pause");
//		exit(1);
//	}
//}
//
////Transpose matrix
//Matrix TransposedMat(Matrix in) {
//	static Matrix out;
//	out.height = in.width;
//	out.width = in.height;
//
//	out.matrix.resize(in.width);
//	for (int i = 0; i < in.width; i++) {
//		out.matrix[i].resize(in.height);
//	}
//
//	for (int i = 0; i < in.width; i++) {
//		for (int j = 0; j < in.height; j++) {
//			out.matrix[i][j] = in.matrix[j][i];
//		}
//	}
//	return out;
//}
//
////Determinant
//double determinant(double a[][M_MAXN], int dimension);
//void spread(double a[][M_MAXN], int row, int dimension);
//void copy_m(double src[][M_MAXN], double dst[][M_MAXN], int dimension);
//
//double Determinant(Matrix in) {
//	double A[M_MAXN][M_MAXN];
//	for (int i = 0; i < in.height; i++) {
//		for (int j = 0; j < in.width; j++) {
//			A[i][j] = in.matrix[i][j];
//		}
//	}
//
//	double sum = determinant(A, in.height);
//	return sum;
//}
//double determinant(double a[][M_MAXN], int dimension) {
//	double sum = 0;
//	double m_copy[M_MAXN][M_MAXN];
//	memset(m_copy, 0, sizeof(m_copy));
//	copy_m(a, m_copy, dimension);
//	if (dimension == 2) {
//		double result = a[0][0] * a[1][1] - a[0][1] * a[1][0];
//		return result;
//	}
//	for (int i = 0; i < dimension; i++) {
//		if (a[i][dimension - 1] - 0 < 0.000001)
//			continue;
//		spread(a, i, dimension);
//		double tmp = a[i][dimension - 1] * determinant(a, dimension - 1);
//		int sign = (i + 1 + dimension) % 2 == 0 ? 1 : (-1);
//		sum += (double)sign * tmp;
//		copy_m(m_copy, a, dimension);
//	}
//	return sum;
//}
//void spread(double a[][M_MAXN], int row, int dimension) {
//	if (row == dimension - 1)
//		return;
//	for (int i = row; i < dimension - 1; i++)
//		for (int j = 0; j < dimension - 1; j++)
//			a[i][j] = a[i + 1][j];
//}
//
//void copy_m(double src[][M_MAXN], double dst[][M_MAXN], int dimension) {
//	for (int i = 0; i < dimension; i++)
//		for (int j = 0; j < dimension; j++)
//			dst[i][j] = src[i][j];
//}
//
////Adjugate matrix
//double AlgebraMinor(Matrix in, int i, int j);
//
//Matrix AdjugateMatrix(Matrix in) {
//	Matrix temp;
//	temp.height = in.height;
//	temp.width = in.width;
//
//	temp.matrix.resize(in.height);
//	for (int i = 0; i < in.height; i++) {
//		temp.matrix[i].resize(in.width);
//	}
//
//	for (int i = 0; i < temp.height; i++) {
//		for (int j = 0; j < temp.width; j++) {
//			temp.matrix[i][j] = AlgebraMinor(in, i, j);
//		}
//	}
//
//	static Matrix out = TransposedMat(temp);
//	return out;
//}
//
//double AlgebraMinor(Matrix in, int i, int j) {
//	Matrix temp;
//	temp.height = in.height - 1;
//	temp.width = in.width - 1;
//
//	temp.matrix.resize(in.height - 1);
//	for (int i = 0; i < in.height - 1; i++) {
//		temp.matrix[i].resize(in.width - 1);
//	}
//
//	int kase_1 = 0, kase_2 = 0;
//	for (int x = 0; x < in.height; x++) {
//		kase_2 = 0;
//		if (x != i) {
//			for (int y = 0; y < in.width; y++) {
//				if (y != j) {
//					temp.matrix[kase_1][kase_2] = in.matrix[x][y];
//					kase_2++;
//				}
//			}
//			kase_1++;
//		}
//	}
//
//	double out = Determinant(temp);
//	return out;
//}
//
//
//int main() {
//	int h, w;
//	cin >> h >> w;
//	double** mat;
//	mat = (double**)malloc(h * sizeof(double*));
//	for (int i = 0; i < h; i++)
//		mat[i] = (double*)malloc(w * sizeof(int));
//
//	for (int i = 0; i < h; i++) {
//		for (int j = 0; j < w; j++) {
//			cin >> mat[i][j];
//		}
//	}
//
//	/*int h_1, w_1;
//	cin >> h_1 >> w_1;
//	double** mat_1;
//	mat_1 = (double**)malloc(h_1 * sizeof(double*));
//	for (int i = 0; i < h_1; i++)
//	mat_1[i] = (double*)malloc(w_1 * sizeof(int));
//
//	for (int i = 0; i < h_1; i++) {
//	for (int j = 0; j < w_1; j++) {
//	cin >> mat_1[i][j];
//	}
//	}*/
//
//	Matrix mat_one = getMatrix(mat, h, w);
//	//Matrix mat_two = getMatrix(mat_1, h_1, w_1);
//
//	Matrix  temp_1 = TransposedMat(mat_one);
//	printMat(temp_1);
//
//	double i = Determinant(mat_one);
//	cout << i << endl;
//
//	Matrix temp_2 = AdjugateMatrix(mat_one);
//	printMat(temp_2);
//
//	/*Matrix temp_2 = multiply(mat_one, mat_two);
//	printMat(temp_2);*/
//
//	system("pause");
//	return 0;
//}