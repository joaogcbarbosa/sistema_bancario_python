<h1>Sistema Bancário V2</h1>
<h2>Objetivo Geral:</h2>
<p>Deixar o código da primeira versão mais modularizado. Para isso, criar funções para as
operações “sacar”, “depositar” e “visualizar extrato” já existentes. Além disso, para a 
versão 2 do sistema, precisa-se criar duas novas funções: criar usuário (cliente do banco) 
e criar conta conta corrente (vincular com usuário).</p>
<h3>Separação em funções:</h3>
<p>Criar funções para todas as operações do sistema. Cada função vai ter uma regra na
passagem de argumentos. O retorno e a forma como serão chamadas pode ser definida de 
forma livre.</p>
<ol>
    <li>Função Saque: Esta função deve receber os argumentos apenas por nome. Sugestão de
     argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de 
     retorno: saldo e extrato;
    </li>
    <li>Função Depósito: Esta função deve receber os argumentos apenas por posição. 
     Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato;
    </li>
    <li>Função Extrato: Esta função deve receber os argumentos por posição e nome.
     Argumentos posicionais: saldo; argumentos nomeados: extrato.
    </li>
</ol>
<h3>Novas funções:</h3>
<ol>
    <li>Função Criar Usuário: O programa deve armazenar os usuários em uma lista. Um 
     usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma 
     string com o formato: logradouro, número, bairro, cidade, sigla do estado. Deve ser 
     armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo 
     CPF;
    </li>
    <li>Função Criar Conta Corrente: O programa deve armazenar contas em uma lista. Uma 
     conta é composta por: agência, número da conta e usuário. O número da conta é 
     sequencial, iniciando em 1. O número da agência é fixo: “0001”. O usuário pode ter 
     mais de uma conta, mas uma conta pertence somente a um usuário;
    </li>
    <li>Função Listar Contas (opcional): Dica: para vincular um usuário a uma conta, 
     filtre a lista de usuários buscando o número do CPF informado para cada usuário da 
     lista.
    </li>
</ol>
<h3>Notas pessoais:</h3>
<ol>
    <li>Para garantir que dois CPF's iguais não serão inseridos, foi criada a função
    "verifica_cpf";
    </li>
    <li>Foi criada a função "verifica_usuario" para que seja forçada a criação de um
     usuário antes da criação de uma conta.
</ol>
