# I Coding Dojo
Realizado em 18/11/2019

Mestre: Guilherme Paiva

## O Problema

Na primeira edição do Dojo de Programação realizado pelo capítulo, foi proposto o problema **Escrevendo no Celular**.

Queremos enviar uma SMS a partir de um celular que não possui um teclado QWERTY, portanto, para escrever um texto precisamos digitar uma combinação numérica que corresponde ao texto, de tal forma:

<img src="http://sergiolopes.org/img/palestra/mobile-web/ios-input-tel.png" width="150" height="150">

Ao enviar mensagens SMS usando rede GSM temos um limite máximo de 255 caracteres, e para este problema, podemos apenas enviar apenas texto. Logo, caracteres especiais e números não podem entrar na mensagem.

Devemos desenvolver um programa em **Python** que dado uma entrada em texto, produza a uma sequência de números necessária para escrever a mensagem em um teclado numérico. Letras referenciadas pelo mesmo número devem ser separadas utilizando o caractere _.

## Recursos

Todos os códigos foram escritos no editor texto [Sublime Text 3](https://www.sublimetext.com/) na linguagem [Python 3.7.5](https://www.python.org/).

Nesta pasta se encontra a [solução](Solution) proposta pelo mestre, e os [códigos](Dojo) desenvolvidos na seção.


### Testes
Para realizar os testes, utilizamos a framework [pytest](https://docs.pytest.org/en/latest/).

#### Instalação
```bash
pip3 install pytest
```
#### Utilização

```bash
pytest
```

## Execução
```bash
python3 dojo.py
```
