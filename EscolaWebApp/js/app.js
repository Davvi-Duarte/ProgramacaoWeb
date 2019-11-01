// Inicializar o módulo.
let nomeApp = 'EscolaWebApp';
let modulos = ["ngMessages"];
var app = angular.module(nomeApp, modulos);

// Estrutura básica para uma função no controlador.
var homeController = function($scope){
  $scope.nome = "";

  $scope.desejarBoasVindas = function() {
    let nome = $scope.nome;
    $scope.mensagem = "Olá, " + nome;
  }
}
app.controller('HomeController', homeController);


var alunoController = function($scope){
  $scope.nome = "";
  $scope.matricula = "";
  $scope.cpf = "";
  $scope.nascimento = "";
  $scope.id_endereço = "";
  $scope.id_endereço = "";

  $scope.cadastrar = function() {
    alunoApi.cadastrar($scope.aluno)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formaluno.$setPristine();
  }
}
app.controller('AlunoController', alunoController);

//factory aluno

var alunoFactory = function($http) {
  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/alunos")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/alunos/" + encodeURI(id))
  };
  var _cadastrar = function(aluno) {
    return $http.post(urlBase + "/aluno", aluno)
  };
  var _atualizar = function(aluno) {
    return $http.put(urlBase + "/aluno/" + encodeURI(id), aluno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}
app.factory("alunoApi", alunoFactory);

var campusController = function($scope){
  $scope.sigla = "";
  $scope.cidade = "";

  $scope.cadastrar = function() {
    campusApi.cadastrar($scope.campus)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formcampus.$setPristine();
  }
}
app.controller('CampusController', campusController);

// campus factory
var campusFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase+ "/campi")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/campi/" + encodeURI(id))
  };
  var _cadastrar = function(campus) {
    return $http.post(urlBase + "/campus", campus)
  };
  var _atualizar = function(campus) {
    return $http.put(urlBase + "/campus/" + encodeURI(id), campus)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("campusApi", campusFactory);

var cursoController = function($scope){
  $scope.nome = "";
  $scope.id_turno = "";

  $scope.cadastrar = function() {
    cursoApi.cadastrar($scope.curso)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formcurso.$setPristine();
  }
}
app.controller('CursoController', cursoController);

// Factory curso
var cursoFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase+ "/cursos")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/cursos/" + encodeURI(id))
  };
  var _cadastrar = function(curso) {
    return $http.post(urlBase + "/curso", curso)
  };
  var _atualizar = function(curso) {
    return $http.put(urlBase + "/curso/" + encodeURI(id), curso)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("cursoApi", cursoFactory);


var turnoController = function($scope){
  $scope.nome = "";

  $scope.cadastrar = function() {
    turnoApi.cadastrar($scope.turno)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formturno.$setPristine();
  }
}
app.controller('TurnoController', turnoController);

// Factory Turno
var turnoFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/turnos")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/turnos/" + encodeURI(id))
  };
  var _cadastrar = function(turno) {
    return $http.post(urlBase + "/turno", turno)
  };
  var _atualizar = function(turno) {
    return $http.put(urlBase + "/turno/" + encodeURI(id), turno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turnoApi", turnoFactory);


var disciplinaController = function($scope){
  $scope.nome = "";
  $scope.id_professor = "";

  $scope.cadastrar = function() {
    disciplinaApi.cadastrar($scope.disciplina)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formdisciplina.$setPristine();
  }
}
app.controller('DisciplinaController', disciplinaController);

// Factory Disciplina
var disciplinaFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/disciplinas")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/disciplinas/" + encodeURI(id))
  };
  var _cadastrar = function(disciplina) {
    return $http.post(urlBase + "/disciplina", disciplina)
  };
  var _atualizar = function(disciplina) {
    return $http.put(urlBase + "/disciplina/" + encodeURI(id), disciplina)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("disciplinaApi", disciplinaFactory);


var enderecoController = function($scope){
  $scope.logradouro = "";
  $scope.complemento = "";
  $scope.bairro = "";
  $scope.cep = "";
  $scope.numero = "";

  $scope.cadastrar = function() {
    enderecoApi.cadastrar($scope.endereco)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formendereco.$setPristine();
  }
}
app.controller('EnderecoController', enderecoController);

// Factory endereco
var enderecoFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/enderecos")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/enderecos/" + encodeURI(id))
  };
  var _cadastrar = function(endereco) {
    return $http.post(urlBase + "/endereco", endereco)
  };
  var _atualizar = function(curso) {
    return $http.put(urlBase + "/endereco/" + encodeURI(id), endereco)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("enderecoApi", enderecoFactory);


var escolaController = function($scope){
  $scope.nome = "";
  $scope.id_endereco = "";
  $scope.id_campus = "";

  $scope.cadastrar = function() {
    escolaApi.cadastrar($scope.escola)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formescola.$setPristine();
  }
}
app.controller('EscolaController', escolaController);

// Factory Escola
var escolaFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/escolas")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/escolas/" + encodeURI(id))
  };
  var _cadastrar = function(escola) {
    return $http.post(urlBase + "/escola", escola)
  };
  var _atualizar = function(escola) {
    return $http.put(urlBase + "/escola/" + encodeURI(id), escola)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("escolaApi", escolaFactory);

var professorController = function($scope){
  $scope.nome = "";
  $scope.id_endereco = "";

  $scope.cadastrar = function() {
    professorApi.cadastrar($scope.professor)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formprofessor.$setPristine();
  }
}
app.controller('ProfessorController', professorController);

// Factory Professor
var professorFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/professores")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/professores/" + encodeURI(id))
  };
  var _cadastrar = function(professor) {
    return $http.post(urlBase + "/professor", professor)
  };
  var _atualizar = function(professor) {
    return $http.put(urlBase + "/professor/" + encodeURI(id), professor)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("professorApi", professorFactory);


var turmaController = function($scope){
  $scope.nome = "";

  $scope.cadastrar = function() {
    turmaApi.cadastrar($scope.turma)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formturma.$setPristine();
  }
}
app.controller('TurmaController', turmaController);

// Factory Turma
var turmaFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/turmas")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/turmas/" + encodeURI(id))
  };
  var _cadastrar = function(turma) {
    return $http.post(urlBase + "/turma", turma)
  };
  var _atualizar = function(turma) {
    return $http.put(urlBase + "/turma/" + encodeURI(id), turma)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turmaApi", turmaFactory);
