var cursoFactory = function($http) {

  var urlBase = "http://127.0.0.1:5000";

  var _listar = function() {
    return $http.get(urlBase+ "/cursos")
  };
  var _buscarPorId = function(id) {
    return $http.get(urlBase + "/cursos/" + encodeURI(id))
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
