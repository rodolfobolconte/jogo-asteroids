# Jogo Star 'Asteroids' Wars

Desenvolvido em Python 3 utilizando as bibliotecas:
  - pygame;
  - random;
  - time.

Realizado durante a cadeira de Programação Orientada a Objetos do Curso Superior de Tecnologia em Telemática.

## Descrição do Jogo

O jogo consiste numa versão básica do famoso Arcade Asteroids, onde temos uma nave com o propósito de destruir o maior número de asteroids e naves inimigas possíveis.

Nesta versão do jogo controlamos a Millenium Falcon, da franquia Star Wars, orbitando a Estrala da Morte, em que devemos destruir e desviar da maior quantidade de Asteroids e Naves Inimigas que puder. O jogador possui 3 vidas que deverão ser usadas para passar das fases apresentadas e aumentar sua pontuação.

## A Millenium Falcon

A Millennium Falcon, a nave que é controlada pelo jogador, é uma espaçonave fictícia da série de filmes Star Wars, que foi pilotada por Han Solo e atualmente por Rey e Chewbacca. A Millennium Falcon foi elemento chave em algumas das maiores vitórias da Aliança Rebelde sobre o Império Galáctico. Na superfície, a Falcon aparenta ser como qualquer outro cargueiro corelliano, com o casco primário em forma de disco e uma cabine cilíndrica montada ao lado da nave. Sua artilharia foi aperfeiçoada para torres blindadas e rotatórias com laser.

No jogo, a Millenium Falcon é capaz de atirar lasers para destruir Asteroids e Naves Inimigas, se movimentando apenas para frente, porém com a possibilidade de ser rotacionada em 45º para a esquerda ou direita. Ela possui 3 vidas (representadas como corações no canto superior direito da tela do jogo), que serão perdidas caso a nave entre em colisão com um Asteroid ou Nave Inimiga ou ainda se for atingida por um disparo de uma Nave Inimiga.

## Os Asteroids

Existem 3 tipos de asteroids de 3 tamanhos diferentes, concedendo pontuações diferentes para o jogador caso o mesmo destrua os Asteroids:
  - Asteroid Tamanho 1 (Menor): este asteróide vale 25 pontos. Ao ser destruído, não gera mais nenhum Asteroid;
  - Asteroid Tamanho 2 (Médio): este asteróide vale 50 pontos. Ao ser destruído, são gerados 2 Asteroids de Tamanho 1;
  - Asteroid Tamanho 3 (Maior): este asteróide vale 75 pontos. Ao ser destruído, são gerados 2 Asteroids de Tamanho 2.
  
Os Asteroids se movimentam sempre na mesma direção, definida aleatoriamente no momento em que são criados.

## As Naves Inimigas

As naves inimigas tem o formato do Caça TIE Avançado x1, sendo um caça de elite usado pelo Império Galáctico em diversas batalhas. Era o caça Imperial que Darth Vader mais utilizava em suas caçadas aos membros da Aliança Rebelde. Diante de um ataque inesperado em sua “indestrutível” Estrela da Morte vinda de naves Rebeldes minúsculas, o Império viu-se incapacitado de destruir tais naves. Darth Vader, escolheu a dedo o esquadrão de pilotos de Caça TIE para acabar com a ameaça Rebelde à Estação. Com seu esquadrão aniquilado, Vader iniciou pessoalmente uma tentativa de enfim destruir os Rebeldes: usar o Caça TIE personalizado, o TIE Advanced x1 Starfighter. Vader conseguiu destruir alguns Rebeldes, porém foi surpreendido por Han Solo, que, a bordo da Millenium Falcon, destruiu parte da asa de sua nave, fazendo com que perdesse controle sobre ela.

No Jogo, as Naves Inimigas começam a aparecer a partir da Segunda Fase, em que a cada nova fase surge uma nova Nave. Ela é capaz de disparar lasers aleatoriamente, com o propósito de destruir a Millenium Falcon ou os Asteroids. Porém, as Naves Inimigas são destruídas ao colidirem com os Asteroids, então use-os ao seu favor. Cada Nave Inimiga quando destruída pela Millenium Falcon, dá ao jogador 100 pontos.

As Naves Inimigas se movimentam sempre na mesma direção, definida aleatoriamente no momento em que são criadas, e seus lasers são disparados de forma aleatória, ou seja, não sabemos em qual direção serão disparados, portanto, fique esperto!

## Controles de Movimentação da Millenium Falcon

| Botão do teclado  | Função no Jogo |
| ------------- | ------------- |
| Tecla `►`  | Gira a Millenium Falcon 45º para a Direita  |
| Tecla `▲`  | Movimenta a Millenium Falcon para a Frente  |
| Tecla `◄`  | Gira a Millenium Falcon 45º para a Esquerda  |
| Tecla `Espaço`  | Dispara um Laser da Millenium Falcon, não funciona mantendo pressionada  |
