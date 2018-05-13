var btnAlterar = document.getElementById('btn-alterar');
btnAlterar.addEventListener('click', function(event) {


    // console.log(validaForm())
    if(validaForm()){
        if(confirm('Deseja realmente submeter formulário?')){
            document.getElementById('form-status').submit();
        }
    }
})

function validaForm() {

    var alunos =  Array.from(document.getElementById('alunos').getElementsByTagName('tbody')[0]
    .getElementsByTagName('tr'));

    var quantAlunos = alunos.length;

    if (quantAlunos < 20 || quantAlunos > 60) {
        alert(`Mínimo de alunos: 20. Máximo de alunos: 60. Alunos selecionados: ${quantAlunos}`);
        return false;
    }

    for (let index = 0; index < alunos.length; index++) {
        var situacao = alunos[index].getElementsByTagName('input');
        var aprovado = situacao[0].checked;
        var cancelado = situacao[1].checked;

        if (!aprovado && !cancelado) {
            alert('Todos os alunos devem estar selecionados!')
            return false;
        }
    }

    return true;
}