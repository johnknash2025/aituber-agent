# AI VTuber Agent

これは、YouTube LiveのコメントにAIが自動で応答し、OBSにコメントを表示し、音声を生成して配信に乗せるためのツールです。

## 機能

- **YouTube Live コメント取得**: 指定したYouTube Liveのチャットコメントをリアルタイムで取得します。
- **AIによる応答生成**: [Ollama](https://ollama.com/) を利用して、コメントに対する返答をAIが生成します。
- **OBSへのコメント表示**: 生成されたAIの応答をOBSのテキストソースに表示します。
- **音声合成**:
  - Google Cloud Text-to-Speech
  - VOICEVOX
  を使用して、AIの応答を音声に変換し再生します。

## 必要なもの

### ソフトウェア
- **[Ollama](https://ollama.com/)**: ローカルで大規模言語モデルを動かすためのツールです。
- **[OBS Studio](https://obsproject.com/)**: 配信・録画ソフトウェアです。
  - **[obs-websocket](https://github.com/obsproject/obs-websocket/releases)** プラグインが必要です。
- **[VOICEVOX](https://voicevox.hiroshiba.jp/)**: テキスト読み上げソフトウェアです（任意）。

### APIキーなど
- **YouTube Data API key**: YouTube Liveのコメントを取得するために必要です。
- **Google Cloud Service Account Key**: Google Cloud Text-to-Speechを使用する場合に必要です。

## セットアップ

1. **リポジトリをクローンします**
   ```bash
   git clone https://github.com/your-username/aituber-agent.git
   cd aituber-agent
   ```

2. **必要なライブラリをインストールします**
   このプロジェクトでは `uv` を使用したパッケージ管理を推奨しています。
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

3. **環境変数を設定します**
   `.env.example` をコピーして `.env` ファイルを作成します。
   ```bash
   cp .env.example .env
   ```
   作成した `.env` ファイルをエディタで開き、YouTubeのAPIキーや動画IDなどを設定してください。

### Google Cloud Credentials

`google_tts_util.py` uses Google Cloud Text-to-Speech. Set the environment
variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of your service account
JSON key before running the utility. You can store this value in a `.env` file
and it will be loaded automatically.

## 使い方

以下のコマンドで、コメント取得とAIの応答を開始します。

```bash
python get-comment.py
```

## テスト

このプロジェクトでは、pytestとpytest-asyncioを使用してテストを実行します。

開発用依存関係をインストールした後、以下のコマンドでテストを実行できます:

```bash
pip install -e .[dev]
make test
```

## モジュール説明

- `main.py`: プロジェクトのエントリーポイント（現在開発中）。
- `get-comment.py`: メインの処理を行うスクリプト。YouTubeコメントを取得し、AI応答を生成、OBS表示、音声合成を実行します。
- `youtube_util.py`: YouTube Data APIを扱うユーティリティ関数群。
- `ollama_util.py`: Ollamaとの連携用ユーティリティ関数。
- `obs_util.py`: OBS WebSocketとの連携用ユーティリティ関数。
- `google_tts_util.py`: Google Cloud Text-to-Speech用のユーティリティ関数。
- `voicevox_util.py`: VOICEVOX API用のユーティリティ関数。
