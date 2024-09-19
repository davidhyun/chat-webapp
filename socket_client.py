import socket


# 모듈 전달 인자값 저장
name = input("이름을 입력하시오: ")
message = input("메시지르 입력하시오: ")

# 서버 주소 설정
server_address = 'localhost'
server_port = 50077

# 서버 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

# 데이터 전송
data = f"{name}:{message}"
client_socket.send(data.encode("utf-8"))

# 서버로부터 응답 받기
response = client_socket.recv(1024).decode("utf-8")
print(f"Response from server: {response}")

# 클라이언트 소켓 연결 종료
client_socket.close()