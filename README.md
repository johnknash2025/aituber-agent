# テスト

このプロジェクトでは、pytestとpytest-asyncioを使用してテストを実行します。

開発用依存関係をインストールした後、以下のコマンドでテストを実行できます:

```bash
pip install -e .[dev]
make test
```

## Google Cloud Credentials

`google_tts_util.py` uses Google Cloud Text-to-Speech. Set the environment
variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of your service account
JSON key before running the utility. You can store this value in a `.env` file
and it will be loaded automatically.
