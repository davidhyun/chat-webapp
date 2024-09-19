import socket

HOST = '0.0.0.0'
PORT = 50077

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()
print(f"서버에서 연결 대기중... {HOST}:{PORT}")


while True:
    # 클라이언트 연결 대기
    client_socket, client_addr = server_socket.accept()
    print(f"클라이언트({client_addr})로부터 연결됐습니다.")

    try:
        # 클라이언트로부터 데이터 수신 (최대 1024 bytes)
        data = client_socket.recv(1024).decode("utf-8") # 복호화
        if not data:
            continue # 연결 계속 대기

        contents = data.split(":")
        if len(contents) != 0:
            name = contents[0]
            message = contents[1]
            response = f"안녕! {name}. \n 클라이언트로부터 다음의 메시지를 수신하였습니다. {message}"
        else:
            response = "수신 데이터 없음"
            
        client_socket.send(response.encode("utf-8")) # 암호화
        
    except Exception as e:
        print(e)
        break
    
    finally:
        client_socket.close()
        print("연결 종료")