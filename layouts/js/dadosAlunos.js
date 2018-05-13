var alunos = [
    {
        'RA': 1701294,
        'Nome': 'Nicolas Rezende'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    },
    {
        'RA': 1701295,
        'Nome': 'João da Silva'
    }
]

function addDadosTabela(){

    var tabela = document.getElementById('alunos').getElementsByTagName('tbody')[0]
    var id = 1
    alunos.forEach(aluno => {
        aluno.Id = id;
        var novaLinha = document.createElement('tr');
        var tdId = document.createElement('td');
        var tdRa = document.createElement('td');
        var tdNome = document.createElement('td');
        var tdSituacao = document.createElement('td');

        tdId.textContent = aluno.Id;
        tdRa.textContent = aluno.RA
        tdNome.textContent = aluno.Nome;

        var span1 = document.createElement('span');
        span1.classList.add('aprovado');
        var input1 = document.createElement('input');
        input1.type = "radio";
        input1.name = 'situacao' + aluno.Id;
        input1.id = 's' + aluno.Id + 'A';

        var label1 = document.createElement('label');
        label1.setAttribute('for', 's' + aluno.Id + 'A');
        label1.textContent = 'Aprovado';

        span1.appendChild(input1);
        span1.appendChild(label1);


        var span2 = document.createElement('span');
        span2.classList.add('cancelado');
        var input2 = document.createElement('input');
        input2.type = "radio";
        input2.name = 'situacao' + aluno.Id;
        input2.id = 's' + aluno.Id + 'B';

        var label2 = document.createElement('label');
        label2.setAttribute('for', 's' + aluno.Id + 'B');
        label2.textContent = 'Cancelado';

        span1.appendChild(input1);
        span1.appendChild(label1);

        span2.appendChild(input2);
        span2.appendChild(label2);

        tdSituacao.appendChild(span1);
        tdSituacao.appendChild(span2);

        novaLinha.appendChild(tdId);
        novaLinha.appendChild(tdRa);
        novaLinha.appendChild(tdNome);
        novaLinha.appendChild(tdSituacao);
        
        tabela.appendChild(novaLinha);
        id++;
    });
}

addDadosTabela();