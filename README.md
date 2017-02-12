# 本リポジトリについて
Elastic Beanstalk(以下eb)を使いこなせると、運用がとてもラクになる。
相当な大規模システムでもないかぎり、システム構築はebから入ると、サービスがかなりスケールするまで、安定した運用が期待できる。
インターネット上には、Web環境のナレッジが多いが、同じようにしてワーカー環境も作ることができる。
Webシステムの裏には、そこそこ大きなバッチ処理が走っていることが多く、Webほど注目されないために、長時間運用すると問題含みになる。
このリポジトリは、ebのワーカー環境導入(Python+Django)のためのチュートリアルになっている。
このチュートリアルで導入イメージを持って、今後タスク処理機構を設計するときの有力な選択肢にしてほしい。

## Elastic Beanstalkとは
AWSが提供している、Webシステム用のインフラフレームワーク。
PaaSの一種と説明されることもあったが、中身はAWSのIaaSとPaaSを組み合わせた、インフラ構築・デプロイ・各種運用をスムーズにするためのフレームワーク。
なので、ひとつひとつのインスタンスを個別にチューニングすることも可能で、かつそれらと連携したデプロイフローが用意されている。
ebの設定内容はソースコードの中で管理できるため、インフラの構成手順や必要パッケージなども、必然的にソース管理される。
ebのバージョンも年々上がっており、便利な機能が追加されたり機能強化も進んでいる。

### Elastic Beanstalkのワーカー環境とは
ebはWebシステムのための構成だが、裏側で稼働するタスク処理にも対応させた環境。
サイトを公開しないワーカー環境も、Webアプリの考え方で開発でき、あるいはWebサイトとタスク処理を同居させるシステムをホストできる。
既存のWebフレームワークのナレッジをそのまま、タスク処理のための仕組みに活かすことができるし、タスク処理の環境もWebのように複数台で冗長化して、分散処理構成が取れる。

### Elastic Beanstalkで使える言語環境
Python / .NET / Ruby / Node.js / PHP / Java / Go / Tomcat が利用可能。
各言語のバージョン/フレームワークは、サポートしている選択肢の中でしか選べないが、メジャーなバージョンならかなり広く選択できる。
ebならではの制約はほとんどなく、ミドルウェアをチューニングしていなければ、各種ebの設定をすればインフラを載せ替えることができる。
