<h1>Sistema Bancário V3</h1>
<h2>Objetivo Geral:</h2>
<p>Modelar um sistema bancário baseado no anterior (V2), porém, orientado a objetos. Adicionar classes para cliente e conta e atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código segue o modelo de classes UML a seguir:</p>
<img src="diagramas-uml\sistema_bancario_uml.png" alt="Modelo de classes do sistema bancário" width=800/>
<p>Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu para funcionarem com as classes modeladas (união das funções criadas na segunda versão do Sistema bancário com as classes criadas na terceira versão).</p>
<h3>Nota pessoal:</h3>
<p>O modelo proposto para o projeto foi o seguinte:</p>
<img src="diagramas-uml\modelo_proposto.png" alt="Modelo de classes proposto" width=800/>
<p>Tomei a liberdade de fazer algumas alterações no modelo proposto de forma que ficasse mais intuitivo e, consequentemente, facilitando o aprendizado.</p>
<p>Abaixo vão algumas razões para as alterações:</p>
<ul>
    <li>Não consegui entender o motivo de uma classe exclusiva para Transação e mais duas subclasses para       depósito e saque. Julguei que fosse mais simples delegar as funções de depositar e sacar unicamente para a classe Conta;</li>
    <li>Para não deixar de trabalhar o conceito de classe abstrata, pus a classe Conta como interface, visto que um cliente simplesmente não tem uma conta, mas sim uma conta-corrente;</li>
    <li>Ao invés de um método de classe para criar uma nova conta, mantive da segunda versão do Sistema Bancário a função "criar_cc", a qual já adiciona na lista de contas do programa uma instância da classe ContaCorrente. O inicializador dessa classe chama automaticamente o método "adicionar_conta" da classe Cliente.</li>
</ul>