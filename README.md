# padroes-de-projeto

As informações apresentadas a seguir foram retiradas do site refactoring.guru.

# Singleton

Singleton: O padrão Singleton resolve o problema de garantir que uma classe tenha apenas uma única instância ao longo de toda a aplicação, 
sendo útil para situações em que múltiplas instâncias poderiam causar inconsistências, como no gerenciamento de conexões a um banco de 
dados ou controle de configurações globais. O problema ocorre quando diversas partes do sistema tentam criar instâncias de uma mesma classe, 
gerando um estado compartilhado inconsistente ou consumo desnecessário de recursos. A solução é restringir a criação de objetos da classe por 
meio de um método estático que verifica se uma instância já foi criada e, caso contrário, cria uma nova, armazenando-a para acesso futuro. 
Assim, o Singleton fornece um ponto de acesso global e controlado, garantindo que apenas uma instância exista e que seja compartilhada de forma 
segura entre os diferentes componentes do sistema.


## Explicacao do Codigo: 
O código utiliza a metaclasse SingletonMeta para garantir que a classe SingletonClass siga o padrão Singleton, ou seja, que haja apenas uma única instância dela em todo o programa. O método especial __call__ é sobrescrito para controlar o processo de criação de instâncias. Ele verifica se já existe uma instância da classe no dicionário interno _instances; se não existir, cria uma nova e armazena-a. Caso contrário, retorna a instância previamente criada. Isso garante que todas as chamadas subsequentes para criar objetos da classe retornem a mesma instância, fornecendo um ponto global de acesso à única instância criada.



![singleton](images/singleton.png)


# Strategy

Strategy: O padrão Strategy é útil quando há a necessidade de realizar diferentes variações de um algoritmo com base no contexto ou em condições específicas, mas sem comprometer a estrutura geral do código com instruções condicionais (como if ou switch). O problema ocorre quando diferentes algoritmos são implementados diretamente no cliente, levando à proliferação de código duplicado e à dificuldade de manutenção ou extensão do sistema. A solução oferecida pelo padrão é encapsular cada algoritmo em sua própria classe concreta, implementando uma interface comum que define o contrato para todos os algoritmos. O cliente, então, delega a execução do algoritmo a um objeto de estratégia que pode ser escolhido dinamicamente em tempo de execução. Isso reduz o acoplamento entre o cliente e as implementações dos algoritmos, permitindo a adição, modificação ou substituição de estratégias de forma independente, promovendo flexibilidade e manutenção limpa no sistema.

## Explicacao do Codigo: 
Problema: Calcular descontos em pedidos sem usar estruturas rígidas, como condicionais (if/else) extensivas, que tornam o código difícil de manter e expandir.
Solução: O Strategy encapsula cada lógica de desconto (ou algoritmo) em uma classe separada que implementa a interface DiscountStrategy. Isso permite alterar ou adicionar novos tipos de desconto sem modificar as classes existentes.

Contexto: A classe Order atua como o "contexto" que usa a estratégia de desconto para calcular o total.
Interface comum: A classe abstrata DiscountStrategy define o método calculate_discount que todas as estratégias devem implementar.
Estratégias concretas:
NoDiscount: Implementa uma lógica que não aplica nenhum desconto.
PercentageDiscount: Calcula um desconto percentual.
FixedDiscount: Aplica um desconto fixo, limitado ao valor total do pedido.
Intercambiabilidade: O cliente pode passar qualquer classe que implemente DiscountStrategy para a classe Order, tornando o comportamento dinâmico e flexível.



![strategy](images/strategy.png)

# Bridge

Bridge: O problema abordado pelo padrão de projeto Bridge é a complexidade e rigidez que surgem quando diferentes dimensões de variação (por exemplo, múltiplas funcionalidades ou tipos) precisam ser combinadas de forma extensiva por meio de herança. Isso leva à criação de uma grande quantidade de subclasses, tornando o código difícil de manter e expandir. Quando há muitas combinações possíveis, a árvore de herança se torna grande e complexa, o que dificulta a manutenção e a adição de novos recursos.
Solução: O padrão Bridge resolve esse problema ao separar a abstração da sua implementação. Em vez de criar subclasses para todas as combinações possíveis de variação, o padrão divide o código em duas partes: uma abstração (a interface que os clientes interagem) e uma implementação (a lógica concreta). Isso permite que ambas as partes evoluam independentemente, o que facilita a adição de novos tipos de abstração ou novas implementações sem afetar o sistema como um todo. Assim, o Bridge proporciona flexibilidade, reduz a complexidade e evita o aumento excessivo de subclasses.

## Explicacao do Codigo: 
Abstração: O RemoteControl e AdvancedRemoteControl são responsáveis pela abstração da operação do dispositivo. Eles definem os métodos para interagir com o dispositivo, como ligar/desligar e ajustar o volume, mas não sabem como isso é feito internamente.

Implementação: O Device é a implementação. A classe TV e Radio são implementações específicas de dispositivos que realizam as ações concretas (ligar, desligar, ajustar volume).

Desacoplamento: A abstração (controle remoto) não depende diretamente das classes concretas (TV ou Rádio). Em vez disso, depende da interface Device, permitindo que um RemoteControl controle qualquer tipo de dispositivo que implemente essa interface, sem precisar alterar o controle remoto quando um novo tipo de dispositivo é adicionado. Isso exemplifica a separação de abstração e implementação, característica do padrão Bridge.

Abstração (RemoteControl e AdvancedRemoteControl): Define operações como ligar/desligar e ajustar volume, mas não implementa a lógica.
Implementação (TV, Radio): Fornecem as implementações específicas dos dispositivos.
Desacoplamento: O controle remoto pode interagir com diferentes dispositivos sem conhecer seus detalhes de implementação, permitindo extensibilidade e flexibilidade.



![bridge](images/bridge.png)


Reference: https://refactoring.guru