
def arr_sum_avg(N):
    sum_arr = 0
    
    if len(N) <= 100 and 1 <= len(N):
        for numbers in range(len(N)):
            sum_arr += N[numbers]
    sum_result = sum_arr
    N_cnt = len(N)+1
    avg_result = sum_result / N_cnt
    
    print(f'合計：{round(sum_result,2)}　平均：{round(avg_result,2)}')


arr_sum_avg([1,3,2,3,6,2,10])