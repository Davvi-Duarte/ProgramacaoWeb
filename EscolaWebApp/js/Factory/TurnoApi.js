// Factory Turno
var turnoFactory = function($http) {

  var urlBase = "http://127.0.0.1:5000";

  var _listar = function() {
    return $http.get(urlBase + "/turnos")
  };
  var _buscarPorId = function(id) {
    return $http.get(urlBase + "/turnos/" + encodeURI(id))
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
