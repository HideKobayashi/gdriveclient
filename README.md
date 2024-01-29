# gdriveclient

gdrive_desktop_client

## 構築手順

python 3.12 のインストール

```sh
conda create --name py312 python=3.12
conda info -e
```

仮想環境の構築

```sh
conda activate py312
python -m venv ~/work/venvs/py312google
conda deactivate
```

仮想環境の有効化

```sh
source ~/work/venvs/py312google/bin/activate
```

仮想環境の無効化

```sh
deactivate
```

VSCode に仮想環境を登録

1. command + shift + p でコマンド入力欄を表示
2. Python: インタプリタを選択
3. ~/work/venvs/py312google/bin/python を設定

Python の外部ライブラリ：Google API クライアントをインストール

```sh
source ~/work/venvs/py312google/bin/activate
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

pip をアップグレード

```sh
python -m pip install --upgrade pip
```

## OpenCV をインストール

```sh
pip install opencv-python
```
