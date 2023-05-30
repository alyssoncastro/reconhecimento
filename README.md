<h1>"Processamento de imagens e detecção de objetos"</h1>
<h6>Instituto de Tecnologia e Liderança</h6>

---
**Autor:** Alysson Carlos de Castro Cordeiro.


**OBJETIVO:**

Desenvolver um script em Python capaz de identificar rachaduras em paredes de concreto. Utilize o dataset desenvolvido pela Roboflow. Para o desenvolvimento dessa atividade, recomenda-se o uso de um modelo de detecção de objetos pré-treinado, como o YoLo.

**TECNOLOGIAS:**

1. Yolo V8
2. OpenCV
3. Colab
4. Python3

**DESENVOLVIMENTO:**

Para alcançarmos nosso objetivo de detecção de rachaduras utilizando inteligência artificial, é necessário começar com a utilização de um conjunto de dados (dataset) como referência para treinar a rede neural. No exercício em questão, recomenda-se o uso do site Roboflow, uma plataforma que disponibiliza diversos conjuntos de dados prontos para download. O Roboflow é uma ferramenta útil para obter acesso a conjuntos de dados adequados para treinamento e validação de modelos de detecção de rachaduras. Após compreendermos o processo de exportação do conjunto de dados para o Colab, uma vez que o código abaixo solicitará uma 'Api Key', podemos utilizar essas informações para treinar nosso modelo de inteligência artificial. Com as informações necessárias em mãos, estamos prontos para iniciar o treinamento da nossa IA.

[clique aqui para ver imagem das instalação no Colab](img/carbon-install.png)

Após o treinamento, o modelo de inteligência artificial irá gerar um arquivo chamado 'best.pt', conforme indicado na imagem, e esse arquivo estará disponível para download. O caminho do arquivo para download será fornecido, permitindo que você faça o download do arquivo 'best.pt'.

[clique aqui para ver imagem do arquivo "best"](img/best.png)

Agora, com o arquivo 'best.pt' treinado, agora vamos prosseguir para o nosso ambiente Python local no Visual Code. Vale lembrar que o arquivo deve estar no mesmo diretório, vamos colocar o arquivo 'best.pt' e o código Python com o seguinte conteúdo:

[clique aqui para ver imagem do código no VsCode](img/carbon.png)

Rode o código.

Este é o resultado:
[clique aqui para ver o resultado](img/rachadura.png)

**CONCLUSÃO**

Chegamos à conclusão de que, por meio dessa atividade, podemos evidenciar o potencial das ferramentas de inteligência artificial em conjunto com o processamento de imagens para trazer benefícios significativos à sociedade. No caso da solução proposta, essa combinação específica pode ser aplicada para identificar rachaduras em tubulações, permitindo a detecção de vazamentos ou possíveis danos na estrutura interna de forma antecipada, sem a necessidade de uma intervenção humana no local. Isso resulta em maior segurança e preservação da integridade dos colaboradores envolvidos, além de proporcionar uma abordagem mais eficiente e ágil para a manutenção e inspeção de infraestruturas.







