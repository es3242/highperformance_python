from threading import Thread

# 병렬로 실행할 함수
def square(n):
    print(n*n)

# 메인 함수
if __name__ == "__main__":
    # 프로세스 풀 생성
    thread =  Thread(target=square)# 프로세스 개수 설정

    # 입력 데이터
    numbers = [1, 2, 3, 4]
