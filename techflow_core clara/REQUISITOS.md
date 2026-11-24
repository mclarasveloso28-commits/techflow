# REQUISITOS DO SISTEMA TECHFLOW CORE
## 1. Descrição do sistema

O TechFlow Core é um sistema de gerenciamento de demandas e chamados técnicos, desenvolvido em Python e executado por meio de uma interface de linha de comando (CLI).

O objetivo do sistema é facilitar o controle das solicitações realizadas pelos usuários, permitindo cadastrar, listar, buscar, atualizar e excluir demandas.

O sistema também contará com funcionalidades de consulta de CEP para obter informações de endereço e consulta de cotação de moedas por meio de serviços externos disponíveis na internet.

A aplicação deverá oferecer uma utilização simples, organizada e segura, evitando erros causados por informações incorretas, campos obrigatórios vazios e registros duplicados.

---

## 2. Requisitos Funcionais (RF)

### RF01 — Cadastrar Demandas

O sistema deverá permitir o cadastro de novas demandas, solicitando as seguintes informações:

- Identificador (ID);
- Título da demanda;
- Nome do solicitante;
- Prioridade;
- CEP;
- Cidade;
- Status.

Cada demanda deverá receber um identificador único. O sistema deverá impedir o cadastro quando existirem campos obrigatórios vazios ou quando o identificador informado já estiver cadastrado.

### RF02 — Listar Demandas

O sistema deverá permitir a visualização de todas as demandas cadastradas.

As informações deverão ser apresentadas de maneira organizada, permitindo que o usuário visualize os dados de cada chamado, incluindo identificador, título, solicitante, prioridade, localização e status.

Caso não existam demandas cadastradas, o sistema deverá apresentar uma mensagem informando que a lista está vazia.

### RF03 — Buscar Demandas

O sistema deverá permitir a busca de uma demanda específica por meio do seu identificador (ID).

Após informar o identificador, o sistema deverá procurar o registro correspondente e apresentar suas informações.

Caso o identificador não seja encontrado, deverá apresentar uma mensagem informando que a demanda não existe.

### RF04 — Atualizar Status das Demandas

O sistema deverá permitir a alteração do status de uma demanda já cadastrada.

O usuário deverá informar o identificador da demanda e selecionar o novo status desejado.

O sistema deverá localizar o registro, realizar a atualização e apresentar uma mensagem confirmando a operação.

Não deverá ser possível atualizar uma demanda inexistente.

### RF05 — Excluir Demandas

O sistema deverá permitir a exclusão de demandas cadastradas por meio de seus identificadores.

Antes de realizar a exclusão, o sistema deverá verificar se a demanda informada existe.

Caso o registro seja encontrado, deverá ser removido da lista de demandas.

Caso não seja encontrado, o sistema deverá apresentar uma mensagem informando que não foi possível localizar a demanda.

### RF06 — Consultar CEP e Cotação de Moedas

O sistema deverá disponibilizar consultas a serviços externos por meio da internet.

Na consulta de CEP, deverá utilizar o serviço ViaCEP para obter informações de endereço relacionadas ao CEP informado.

Na consulta de cotação de moedas, deverá utilizar um serviço externo para obter informações atualizadas sobre a cotação de moedas, incluindo o dólar.

As informações recebidas deverão ser apresentadas de maneira organizada ao usuário.

Caso ocorra uma falha de conexão ou indisponibilidade do serviço, o sistema deverá apresentar uma mensagem informativa, sem encerrar inesperadamente a aplicação.

---

## 3. Requisitos Não Funcionais (RNF)

### RNF01 — Segurança

O sistema deverá validar as informações fornecidas pelos usuários, impedindo entradas inválidas que possam comprometer o funcionamento da aplicação.

Também deverá tratar erros durante as consultas aos serviços externos, evitando encerramentos inesperados.

### RNF02 — Integridade dos Dados

O sistema deverá garantir a integridade das informações cadastradas, impedindo registros com identificadores duplicados e campos obrigatórios vazios.

As operações de atualização e exclusão deverão verificar a existência da demanda antes de realizar qualquer alteração.

### RNF03 — Usabilidade

O sistema deverá apresentar menus, opções e mensagens claras e organizadas, facilitando a utilização por pessoas com diferentes níveis de conhecimento em informática.

As mensagens de erro deverão explicar o problema de maneira compreensível, orientando o usuário sobre como proceder.

### RNF04 — Desempenho

O sistema deverá executar as operações de cadastro, listagem, busca, atualização e exclusão de maneira rápida e eficiente.

As operações internas deverão evitar processamento desnecessário, proporcionando uma utilização adequada pelo terminal.

### RNF05 — Disponibilidade e Confiabilidade

O sistema deverá apresentar comportamento estável durante sua execução, tratando erros de entrada de dados e falhas de conexão com serviços externos.

A indisponibilidade temporária da internet ou de uma API não deverá provocar o encerramento inesperado do programa.

---

## 4. Considerações Finais

Os requisitos apresentados neste documento definem as funcionalidades e características de qualidade necessárias para o desenvolvimento do TechFlow Core.

Os requisitos funcionais estabelecem as operações que o sistema deverá realizar, enquanto os requisitos não funcionais definem os padrões de segurança, integridade, usabilidade, desempenho e confiabilidade que deverão ser considerados durante o desenvolvimento.

Este documento servirá como referência para as próximas etapas do projeto, orientando a implementação, os testes e a validação do sistema.