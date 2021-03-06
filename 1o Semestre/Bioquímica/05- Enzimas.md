# Enzimas

12/08/20

---

Algumas enzimas precisam de um **cofator** para desempenhar seu papel no organismo, que pode ser íons, ou uma molécula orgânica, chamada de **coenzima**, geralmente derivadas de vitaminas. Se a coenzima ou o cofator se ligam muito firmemente à enzima são chamados **grupo prostético**.

Há um codigo que classifica as enzimas, no formato A.B.C.D. A é a classe da enzima, que pode ser:

1. Oxirdoredutases
2. Transferases
3. Hidrolases
4. Liases
5. Isomerases
6. Ligases

As enzimas atuam reduzindo a energia de ativação necessária para transformar os reagentes nos produtos, não sendo alterada ao fim do processo.

A velocidade de qualquer reação é dada por $V = k[A][B]$ ... Inerente ao k é a velocidade de ativação da reação. Assim, a relação do k da reação catalizada e o k da reação normal temos uma razão de quão mais eficientes são as reações catalizadas (em torno de $10^{10}$). A constante de equilíbrio, entretanto, não se relaciona com enzimas.

O modelo mais aceitado atualmente diz que no estado de transição enzima e substratos estão em seus estados de maior complementariedade. 

## Análise qualitativa das enzimas

As enzimas só podem atuar enquanto estão em quantidade o suficiente concentração. Uma vez que todas estão preenchidas, não ocorre mais aumento na velocidade.

A reação catalizada ocorre em pelo menos duas etapas. A mais demorada é aquela com maior energia de ativação e sua constante de reação é *kcat*.

A reação catalizada entra num **estado estacionário** quando a concentração de um de seus intermediários não se altera, uma vez que a formação de novos intermediários ocorre no mesmo ritmo do consumo dessas substâncias. Nesse momento, as enzimas estão "saturadas", então aumentar a quantidade de substrato não aumenta a velocidade da reação.

Podemos descobrir a velocidade da reação total ao considerar que esta é a mesma da velocidade no estado estacionário. Considerando um equação do tipo
$$
\ce{E + S <=> ES <=> EP <=> E + P}
$$
na qual a passagem de ES para EP é a mais demorada, temos que ES será o intermediário cuja concentração não se alterará no estado estacionário. 

![image-20200813084840994](05- Enzimas.assets/image-20200813084840994.png)

Vf = Vq. Simplificando, temos que

![image-20200813110656835](05- Enzimas.assets/image-20200813110656835.png)

Definindo as constantes da equação como **constante de Michaelis (Km)**

$$
sendo\ K_m = (K_{-1} + K_2)/K_1\\
e\\
V_0 = k_2[ES],\\
temos\ que\\
V_0 = \frac{k_2[E_t][S]}{K_m + [S]}\\
$$

A velocidade máxima da reação ocorre quando toda a enzima está "saturada", sendo representada como k2[Et]. **Finalmente,**

$$
V_0 = \frac{V_{max}[S]}{K_m+[S]}
$$

Pela equação, quando a velocidade inicial é metade da velocidade máxima, a constante de Michaelis é igual a [S]. 

K2 é também chamado de Kcat, ou, quando as enzimas estão saturadas, **número de renovação**, uma vez que mede a frequência em que a enzima pode ser reutilizada. Para comparar a eficiencia de duas enzimas usa-se a relação entre Kcat e Km.

## Afirmativas:

**Verdadeira:** As enzimas alteram a constante da reação química, alterando assim as velocidades dela.

Analisando  a constante da reação química, vemos que ela depende da energia de ativação da reação. Como as enzimas alteram a energia de ativação, alterarão também a constante.

**Falsa:** Enzimas atuam aumentando a constante de equilíbrio no sentido direto, o que gera o aumento na produção do produto

Enzimas não alteram a constante de equilíbrio, sim a energia de ativação da reação.

**Verdadeira:** A Kcat dá o número de vezes que a enzima pode ser utlizada em um período de tempo

Sim, a Kcat é chamada de número de renovação devido a sua capacidade de medir a frequência de reutilzação enzimática

**Falsa:** Pode-se dizer que a equação está em seu estado estacionário quando a concentração de produtos e de reagentes não varia.

Nessa condição, a reação está em estado de equiíbrio, não em estado estacionário. Ela está em estado estacionário quando as velocidades de formação e consumo de seu intermediário anterior à etapa lenta são iguais.

{% include mathjax.html %}