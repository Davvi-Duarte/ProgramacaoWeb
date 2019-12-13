var cursoController = function($scope, $mdToast, $state, cursoApi){
  $scope.curso={};

  $scope.cadastrar = function() {
    let curso = angular.copy($scope.curso);
    cursoApi.cadastrar($scope.curso)
      .then(function(response) {
        $state.transitionTo('cursos', {
          reload: true,
          inherit: false,
          notify: true
      });
      var toast = $mdToast.simple()
        .textContent('O curso foi cadastrado com sucesso!')
        .position('top right')
        .action('OK')
        .hideDelay(6000);
      $mdToast.show(toast);
    })
      .catch(function(error) {
        var toast = $mdToast.simple()
        .textContent('Algum problema ocorreu no envio dos dados.')
        .position('bottom center')
        .action('OK')
        .hideDelay(6000)
        .toastClass('my-success');
        $mdToast.show(toast);
      });
  };
}

app.controller('CursoController', cursoController);
