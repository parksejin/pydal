import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from matrix import Matrix

# parse txt file to list of matrices
def parse_Matrix(testset):
    print "Parsing text file "+ testset + " into Matrix instance"

    f=open(testset, "r")
    mat_list = [] # this will be returned 
    res = [] # contains list of list that will be changed to a matrix
    res_len = -1
    for line in f.readlines():
	if line.startswith("test"):
	    res.append([])
	    res_len += 1
	else:
	    res[res_len].append(line.rstrip(" \r\n").split(" "))
    
    for elem in res: 
	if(type(elem) == int):
	    mat = Matrix(1,1)
	    mat.matrix = elem
	    mat_list.append(mat)
	else:
            print elem
	    mat = Matrix(len(elem), len(elem[0])) # Matrix(2,10)
	    for r in range(mat.row): # 2
		for c in range(mat.col): # 10
                    mat.matrix[r][c] = int(elem[r][c])
	    mat_list.append(mat)

    return mat_list
	
# wrtie list of matrices into txt file in desired directory
def write_Matrix(mat_list, txt_dir, txt_name): 
    print "Writing list of matrix to text file " + txt_name

    f = open(os.path.join(txt_dir, txt_name+".txt"), "w")

    for idx, mat in enumerate(mat_list):
	f.write("test case " + str(idx+1) + "\n")
	f.write(str(mat))
	f.write("\n")
    f.close()

# compare two matrix
def compare_Matrix(solset, resset, func_dir, test_func):
    grade = open(os.path.join(func_dir, test_func + "_grade.txt"), "w+")
    grade_sum = open(os.path.join(os.path.dirname(__file__), "../../grade_total.txt"), "a+")
    grade_total = 0
    for idx in range(len(solset)):
	if solset[idx].matrix == resset[idx].matrix:
	    grade.write("correct case : " + str(idx) + "\n")
	    grade_total += 1
	else:
	    grade.write("incorrect case : " + str(idx) +" \n")
	    grade.write("Solution \n")
	    grade.write(str(solset[idx]) + "\n")
	    grade.write("Result \n")
	    grade.write(str(resset[idx]) + "\n")
    print test_func + " test summary : " + str(grade_total) + "/" + str(len(solset))
    grade.write(test_func + " test summary : " + str(grade_total) + "\n")
    grade_sum.write(test_func + " test summary : " + str(grade_total) + "/" + str(len(solset)) + "\n")
    grade.close()
    grade_sum.close()
