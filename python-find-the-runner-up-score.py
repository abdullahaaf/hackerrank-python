# PROBLEMS
'''
scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

notes:
Fungsi map() berfungsi untuk mengaplikasikan satu fungsi ke semua anggota dari iterable (list, tuple, dan lain – lain) dan mengembalikan hasilnya berupa objek map. Objek map ini bisa dengan mudah diubah menjadi list baru yang anggotanya berupa hasil pemrosesan dari fungsi dengan menggunakan fungsi list(), tuple(), maupun set().
'''

# SOLUTION
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()[:n])
    arr_list = list(arr)
    new_list = []
    for i in arr_list:
        if i not in new_list:
            new_list.append(i)
    new_list.remove(max(new_list))
    print(max(new_list))