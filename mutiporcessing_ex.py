import multiprocessing

# 병렬로 실행할 함수
def square(n):
    return n * n

# 메인 함수
if __name__ == "__main__":
    # 프로세스 풀 생성
    pool = multiprocessing.Pool(processes=4)  # 프로세스 개수 설정

    # 입력 데이터
    numbers = [1, 2, 3, 4]

    # square 함수를 병렬로 실행하고 결과를 출력
    results = pool.map(square, numbers)
    pool.close()  # 작업이 끝나면 풀을 닫음
    pool.join()  # 모든 프로세스가 끝날 때까지 기다림

    print(results)
