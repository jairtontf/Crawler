# Crawler para o Vagalume

Um pequeno projeto para exibir os nomes das músicas de uma banda que você deseja procurar.

## Informações de uso

Basta você executar o script passando como argumento o nome da banda.
Também é possível usar o argumento -top5 para trazer as cinco músicas mais populares da banda.
Além disso você pode digitar o nome da banda que tenha acento nas letras.
Bandas que tem caracteres especias como apóstrofo ( ' ), cifrão ( $ ), 'e comercial'
  ( & ) e outros, você deve escrever o nome da banda sem o carácter especial.


```- Ex0.: Titãs se tornará titas;
```
```- Ex1.: para Gun's n Roses utilize Guns n Roses;
```
```- Ex2.: para Eddy B & Tim Gunter utilize Eddy B Tim Gunter
```
```- Ex2.: para Ca$h Out utilize Cah Out
```

### Requisitos

Recomendo utilizar Python 3.7, virtualenv e os seguintes módulos: bs4 na versão 4.7.1 e requests na versão 2.21.0


### Instalando

Com o Python 3.7 instalado na máquina instale o virtualenv ou qualquer outro de sua preferência

```pip install virutalenv```

Crie o seu ambiente virtual e ative ele

```virtualenv nomedoambiente```
```source caminho/do/ambiente/bin/activate```

Agora instales as os módulos

```pip install -r requirements.txt```

Agora faça o clone do repositório

```git clone https://github.com/jairtontf/Crawler.git```

### Exemplo de uso

```python crawler.py Zé do Caroço -top5```
