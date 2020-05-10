import requests


def buscar_avatar(usuario):
    """
    Função para buscar avatar do usuário no GitHub
    :param usuario: Nome do usuário
    :return: Avatar do usuário no GitHub
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
if __name__ == '__main__':
    print(buscar_avatar('JoaoCesarSeS'))

