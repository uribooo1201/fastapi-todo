# FastAPI ToDo Application

[![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions)
[![CI-E2E](https://github.com/<OWNER>/<REPO>/actions/workflows/ci-e2e.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions)

---

## 📌 Overview (English)

This repository provides a **ToDo application built with FastAPI** as a practical example for learning and demonstration.  
It shows how to combine **FastAPI, SQLAlchemy, Alembic, Docker, and GitHub Actions** to build a modern backend service.

### ✨ Features
- RESTful API built with **FastAPI**
- Database layer with **SQLAlchemy** (Postgres / SQLite)
- Schema management with **Alembic**
- Containerized setup using **Docker & docker-compose**
- Automated testing with **pytest**
- **Continuous Integration (CI)** via GitHub Actions:
  - Unit tests with SQLite (fast)
  - End-to-End tests with PostgreSQL
  - Code quality checks (Ruff, Mypy)
  - (Optional) Code coverage reporting via Codecov

### 📚 API Endpoints (examples)
- `GET /healthz` – health check
- `GET /todos` – list todos
- `POST /todos` – create a todo
- `GET /todos/{id}` – get a specific todo
- `PUT /todos/{id}` – update a todo
- `DELETE /todos/{id}` – delete a todo

### 🚀 Getting Started
```bash
# 1. Clone this repository
git clone https://github.com/<OWNER>/<REPO>.git
cd <REPO>

# 2. Start services with Docker
docker compose up --build

# 3. Access API
curl http://localhost:8000/healthz
```

---

## 📌 概要 (日本語)

このリポジトリは、**FastAPI を用いて構築した ToDo アプリケーション**のサンプルです。  
**FastAPI, SQLAlchemy, Alembic, Docker, GitHub Actions** を組み合わせて、モダンなバックエンドサービスを構築する方法を示しています。

### ✨ 特徴
- **FastAPI** による RESTful API
- **SQLAlchemy** を利用したデータベース層（Postgres / SQLite）
- **Alembic** によるスキーマ管理
- **Docker & docker-compose** によるコンテナ化
- **pytest** を使った自動テスト
- **GitHub Actions** による CI:
  - SQLite を用いたユニットテスト（高速）
  - PostgreSQL を用いたエンドツーエンドテスト
  - 静的解析（Ruff, Mypy）
  - （オプション）Codecov によるカバレッジ可視化

### 📚 API エンドポイント（例）
- `GET /healthz` – 動作確認
- `GET /todos` – ToDo 一覧取得
- `POST /todos` – ToDo 登録
- `GET /todos/{id}` – ToDo 詳細取得
- `PUT /todos/{id}` – ToDo 更新
- `DELETE /todos/{id}` – ToDo 削除

### 🚀 セットアップ方法
```bash
# 1. リポジトリを clone
git clone https://github.com/<OWNER>/<REPO>.git
cd <REPO>

# 2. Docker でサービス起動
docker compose up --build

# 3. API へアクセス
curl http://localhost:8000/healthz
```
