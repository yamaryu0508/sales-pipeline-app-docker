from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    アプリケーション構成クラス
    管理画面での表示名を指定する
    """
    name = 'users'
    verbose_name = 'User settings'
