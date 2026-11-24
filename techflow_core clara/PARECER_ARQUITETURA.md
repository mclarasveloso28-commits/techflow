# PARECER TÉCNICO — SELEÇÃO DA ARQUITETURA DO TECHFLOW CORE

**Projeto:** TechFlow Core  
**Empresa:** TechFlow Solutions  
**Linguagem escolhida:** Python  
**Arquitetura selecionada:** Console / CLI  
**Etapa:** 04 — Arquitetura de Sistemas e Defesa Técnica

## 1. Comparação das Arquiteturas

**Aplicação Console / CLI:** A arquitetura Console, também conhecida como CLI (Command Line Interface), permite que o usuário interaja com o sistema por meio de textos e comandos digitados no terminal. É uma alternativa simples, leve e adequada para aplicações que precisam executar operações de cadastro, consulta, atualização e exclusão de informações. Também facilita o desenvolvimento e a manutenção do sistema, pois não exige a criação de uma interface gráfica.

**Aplicação Web:** A arquitetura Web permite que os usuários acessem o sistema por meio de um navegador de internet. Sua principal vantagem é possibilitar o acesso por diferentes dispositivos e oferecer interfaces visuais com botões, formulários e painéis. Entretanto, seu desenvolvimento exige componentes adicionais, como servidor web, rotas, páginas e mecanismos de comunicação entre cliente e servidor, aumentando a complexidade do projeto.

**Aplicação Desktop:** A arquitetura Desktop consiste em um programa executado diretamente no computador, normalmente com uma interface gráfica composta por janelas, menus e botões. Oferece uma experiência visual mais completa e pode funcionar sem conexão constante com a internet, dependendo das funcionalidades. Porém, exige a implementação de elementos gráficos e pode demandar mais tempo de desenvolvimento e manutenção.

## 2. Justificativa da Escolha do Python em Modo CLI

A escolha do Python em modo CLI para o desenvolvimento do TechFlow Core foi realizada considerando os requisitos e objetivos definidos para o projeto. O sistema tem como finalidade gerenciar demandas e chamados técnicos, oferecendo operações de cadastro, listagem, busca, atualização de status e exclusão. Essas funcionalidades podem ser executadas de maneira eficiente por meio de menus e comandos apresentados no terminal, sem a necessidade de uma interface gráfica complexa.

Outro fator importante é a utilização da linguagem Python, que apresenta sintaxe simples, legibilidade e recursos nativos adequados para o desenvolvimento da aplicação. O Python permite trabalhar com listas, dicionários, funções e estruturas de repetição e decisão, além de oferecer bibliotecas nativas para comunicação com serviços externos por HTTP e manipulação de dados JSON. Dessa forma, será possível implementar as consultas de CEP e cotação de moedas sem depender da instalação de bibliotecas externas, conforme as restrições do ambiente de desenvolvimento.

Portanto, a arquitetura CLI foi considerada a alternativa mais adequada para o TechFlow Core, pois atende às necessidades funcionais do sistema, permite uma implementação mais simples e facilita a realização de testes e manutenção. Além disso, sua execução pelo terminal do VS Code é compatível com o ambiente disponibilizado pelo SENAI. A escolha também permite concentrar os esforços no desenvolvimento das regras de negócio, na integridade dos dados e na segurança das operações, atendendo aos objetivos estabelecidos para o projeto.

## 3. Conclusão

Com base na comparação realizada, a arquitetura Console/CLI utilizando Python foi selecionada para o desenvolvimento do TechFlow Core por apresentar melhor adequação ao escopo, aos recursos disponíveis e às necessidades do projeto.

A decisão prioriza simplicidade, organização, facilidade de desenvolvimento e atendimento aos requisitos funcionais e não funcionais definidos anteriormente.