# icra-collecter

**icra-collecter** とは、[Python](https://www.python.org/)のpipである[icrawler](https://icrawler.readthedocs.io/en/latest/)を使用して任意の画像を収集するプログラムです。  
機械学習のテストにでも使ってください。

## Windowsの環境でしか試せていません。ごめんなさい


# 説明
* 内容物 (画像収集機 Bing_Ver & Google_Ver)
* 実際に動かすと、下のような画面が出てきます。  
* なんとなく英語にしてみたが、ガバガバです...  

## UIの解説 (上から順番に)

1. 保存先の設定

2. 収集した画像を入れるフォルダの名前の設定

3. 収集したい画像の名前などを入力  
   (検索エンジンみたいに入力しても大丈夫)

4. 欲しい画像の枚数を入力  
   (1000枚ぐらいまで？)

5. 大まかな画像サイズの選択  
   [None,small,medium,large]の４種類


![inter](https://user-images.githubusercontent.com/55323475/88475969-99fc7500-cf6f-11ea-9137-d2ac59d52196.png)

# 環境

使用しているライブラリなど

* Python 2.7~ or 3.5~
* icrawler
* tkinter
* getpass 

# インストール
## 1. install Python  

[Python](https://www.python.org/)のinstallは各自でお願いします

## 2. install icrawler
```bash
pip install icrawler
```

とりあえずこれで**Bing_Ver.py**は動く  
##### 多分...

# 動作方法

先ほどの物を入れた環境でgit などして獲得

```bash
https://github.com/chiseno/icra-collecter.git
```

Python に続けて **Bing_Ver.py** or **Google_Ver.py** をDDして実行！！！

```bash
Python C:\Users\~~~~\Bing_Ver.py  or  Google_Ver.py
```


# 注意！！！
画像枚数が多くなればなるほど、違う画像が出てきてしまいます（超欠陥！！！）  
**Google_Ver.py**はpipのicrawlerをインストールしただけでは使えないはずなので（Googleとの相性問題）、[ここのサイト](https://github.com/hellock/icrawler/issues/65)を参考にしてpipであるicrawler本体のコードを少し書き換えてあげてください。

### 初心者作品ですが、ここまで読んでいただきありがとうございます。
