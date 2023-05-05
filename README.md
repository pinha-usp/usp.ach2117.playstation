# USP - ACH2117 - PlayStation

> Renderização dos botões do PlayStation usando OpenGL 

Para renderizar esses botões, a biblioteca Python [moderngl](https://github.com/moderngl/moderngl) foi utilizada. Ela
facilita muito as operações utilizando OpenGL e GLSL. Os botões foram renderizados utilizando técnicas para calcular
círculos, retângulos e triângulos a partir de vértices 2D, assim como rotações e translações sobre esses mesmos vértices

<div align="center">
  <img width="400" src="https://user-images.githubusercontent.com/86596621/236529852-8e6976f9-0bbc-493e-80a6-7fdbfff97c01.png">
</div>

## Como executar?

Instale as dependências do projeto:

```
python install -r requirements.txt
```

Após, é só rodar o script principal:

```
python window.py
```

> **Warning**
> A versão Python 3.10 foi utilizada

> **Note**
> A tela ficará em fullscreen. Para sair do programa, basta apertar <kbd>ESC</kbd>
