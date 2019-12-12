var campusController = function($scope, $mdToast, $state, campusApi){
  $scope.campus={};

  $scope.cadastrar = function() {
    let campus = angular.copy($scope.campus);
    campusApi.cadastrar($scope.campus)
      .then(function(response) {
        $state.transitionTo('campi', {
          reload: true,
          inherit: false,
          notify: true
      });
      var toast = $mdToast.simple()
        .textContent('O campus foi cadastrado com sucesso!')
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

app.controller('CampusController', campusController);
