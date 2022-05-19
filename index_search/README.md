# Scripts para experimentos do projeto

Aqui disponibilizamos os scripts para reprodução dos experimentos detalhados no relatório do segundo projeto da disciplina de processamento de cadeias de caracteres, de forma que aqui estarão as isntruções para executar os experimentos, os detalhes de como eles funcionam estarão no relatório mencionado.

No seguinte [link](http://pizzachili.dcc.uchile.cl/texts/nlang/) é possível encontrar os arquivos usados nos quais realizamos as buscas dos padrões.

---

## Aviso

Os scripts foram feitos para rodar com uma determinada estrutura no arquivo de padrões, mas para repordução desse experimento é possível alterá-lo para que execute os
scripts com padrões diferentes dos quais usamos ou aumentar sua quantidade.

---

## Ajustes no texto

Os textos possuem alguns caracteres fora do limite ASCII, de modo que foi necessário o uso de um script que eliminará cada linha que possui esses caracteres. Não processar esse texto, levará a respostas distintas em relação à corretude, visto que ferramentas cocmo grep não irão contabilizar matchs do padrão em linhas que possuem caracteres fora do ASCII.

Dessa forma, para os ajustes no texto, siga os seguintes passos:

1. Baixe o texto que você deseja analizar e coloque-o nesse repositório.
2. Em seguida, execute o seguinte comando para descompactar o arquivo: 
```bash 
  gzip -d <nome_do_arquivo> 
  ```
3. Para ajustar o texto conforme discutido, execute o seguinte script:
```bash
  python3 clean_text.py <nome_do_arquivo>
  ```
---

## Experimentos de corretude

Para executar os testes de corretude para indexação e busca:
```bash
  python3 corretude_index_search.py dataset/patterns_exato_completo.txt <nome_do_arquivo>
  ```
 
Ao final de cada execução, haverá uma sinalização para cada erro de corretude encontrado na nossa ferramenta. Bem como um aviso, caso nenhum erro tenha sido encontrado.

---

## Experimentos de desempenho

Para executar o experimento de desempenho para a indexação:
```bash
  python3 benchmark_index.py <nome_do_arquivo>
  ```
Ao final da execução haverá um output informando o tempo necessário para indexar o arquivo

Para o experimento de desempenho para busca:
```bash
  python3 benchmark_search.py dataset/patterns_exato_completo.txt <nome_do_arquivo>
  ```
Ao final da execução será dado como output um arquivo .csv com os tempos de execução para o grep, pmt e a nossa ferramenta.