# tcpで画像を受信するサーバー
# 画像を受信するとrecieve.jpgを保存する
import socket
import cv2
import numpy

# 待ち受けtcpポート
PORT = 50007

def main():
    # ソケットの作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # ソケットの設定
        s.bind(('', PORT))
        s.listen(1)
        print('Waiting for connection...')
        # クライアントからの接続を待つ
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # データを受信
                data = conn.recv(1024)
                if not data:
                    break
                # 受信したデータを画像に変換
                img = cv2.imdecode(numpy.frombuffer(data, dtype='uint8'), cv2.IMREAD_COLOR)
                # 画像を保存
                cv2.imwrite('recieve.jpg', img)
                print('recieve.jpg saved')
                break

if __name__ == '__main__':
    main()
