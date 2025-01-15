# send.jpgをサーバーに送信するクライアント
import socket
import cv2
import numpy

# サーバーのIPアドレスとポート
HOST = 'localhost'
PORT = 50007

def main():
    # ソケットの作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバーに接続
        s.connect((HOST, PORT))
        # 画像の読み込み
        img = cv2.imread('send.jpg')
        # 画像をバイト列に変換
        data = cv2.imencode('.jpg', img)[1].tobytes()
        # 画像を送信
        s.sendall(data)
        print('send.jpg sent')

if __name__ == '__main__':
    main()
