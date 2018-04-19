
document.getElementById("formulario").onsubmit=
function(event){
    var cpfAluno = document.getElementById("cpfaluninho").value;
    var senhaAluno = document.getElementById("senha").value;
    var confirmarSenha = document.getElementById("confirmSenha").value;
    var dataNasc  = document.getElementById("nascimentoAluno");
    convertDate = new Date(dataNasc.value);
    var ano,mes,dias,dataAtual, diaAtual,mesAtual,anoAtual,resulIdade,desc,resp;
    ano = convertDate.getFullYear();
    mes = convertDate.getMonth()+1;
    dias = convertDate.getDate()+1;
    
    dataAtual = new Date();
    diaAtual = dataAtual.getDate()+1;
    mesAtual = dataAtual.getMonth()+1;
    anoAtual= dataAtual.getFullYear();

    resulIdade = anoAtual-ano;
    if (mesAtual>mes){
        resulIdade= resulIdade;
    }else if(mesAtual==mes){
        if(diaAtual>=dias){
            resultIdade=resulIdade;
        }else{
            resulIdade -=1;
        }

    }else{
        resulIdade -=1;
    }
    if (resulIdade>=17){
        resp = true;
        desc='Idade Válida'
    }else{
        resp=false;
        desc='Apenas alunos com idade igual ou superior a 17 podem realizar o cadastro'
    }
    
    alert(desc);

    if (resp==true){
        x = (validaCPF(cpfAluno));
        if(x==true){
            resp=true;
            senha = confereSenha(senhaAluno,confirmarSenha);
            if(senha==true){
                caracnum = verificarNumeLet(senhaAluno);

                if(caracnum==true){
                    resp=true;
                }else{
                    resp=false;
                }
                
            }else{
                alert("As senhas não conscidem");
                senhaAluno = document.getElementById("senha").focus()
                
                resp=false;
            }
        }else{
            resp=false;
            alert("CPF Inválido!")
        }
    }

    return resp
}

function validaCPF(cpf)
  {
    var numeros, digitos, soma, i, resultado, digitos_iguais;
    digitos_iguais = 1;
    if (cpf.length < 11)
          return false;
    for (i = 0; i < cpf.length - 1; i++)
          if (cpf.charAt(i) != cpf.charAt(i + 1))
                {
                digitos_iguais = 0;
                break;
                }
    if (!digitos_iguais)
          {
          numeros = cpf.substring(0,9);
          digitos = cpf.substring(9);
          soma = 0;
          for (i = 10; i > 1; i--)
                soma += numeros.charAt(10 - i) * i;
          resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
          if (resultado != digitos.charAt(0))
                return false;
          numeros = cpf.substring(0,10);
          soma = 0;
          for (i = 11; i > 1; i--)
                soma += numeros.charAt(11 - i) * i;
          resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
          if (resultado != digitos.charAt(1))
                return false;
          alert("CPF Válido!");
          return true;

          }
    else
        return false;
  }
  function confereSenha(senha1,senha2){
        if(senha1==senha2){
            return true;
        }else{
            return false;
        }
  }
function verificarNumeLet(senha){
    if(!isNaN(senha) && isNaN(senha)){
        alert("Letras e numeros");
        return false;
    }else{
        alert("Não tem as duas opções")
        return true;
    }

}