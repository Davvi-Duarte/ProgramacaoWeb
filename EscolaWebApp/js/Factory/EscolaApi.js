var escolaFactory = function($http) {

  var urlBase = "http://127.0.0.1:5000";

  var _listar = function() {
    return $http.get(urlBase + "/escolas")
  };
  var _buscarPorId = function(id) {
    return $http.get(urlBase + "/escolas/" + encodeURI(id))
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
