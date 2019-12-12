/**
 * Configuração da rota com ui-router.
 */
app.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

    // Rota padrão.
    $urlRouterProvider.otherwise("/home");

    // Estados
    $stateProvider
      // Home
      .state('home', {
        url: '/home',
        title: 'EscolaApp - Página Principal',
        templateUrl: 'Home.html',
        controller: 'HomeController'
      })
      .state('aluno', {
        url: '/aluno',
        title: 'EscolaApp - Cadastrar Aluno',
        templateUrl: 'Aluno.html',
        controller: 'AlunoController'
      })
      .state('alunos', {
        url: '/alunos',
        title: 'EscolaApp - Listar Alunos',
        templateUrl: 'Alunos.html',
        controller: 'AlunosController'
      })
      .state('campus', {
        url: '/campus',
        title: 'EscolaApp - Cadastrar Campus',
        templateUrl: 'Campus.html',
        controller: 'CampusController'
      })
      .state('campi', {
        url: '/campi',
        title: 'EscolaApp - Listar Campi',
        templateUrl: 'Campi.html',
        controller: 'CampiController'
      });
  })
  //take all whitespace out of string
  .filter('nospace', function() {
    return function(value) {
      return (!value) ? '' : value.replace(/ /g, '');
    };
  })
  //replace uppercase to regular case
  .filter('humanizeDoc', function() {
    return function(doc) {
      if (!doc) return;
      if (doc.type === 'directive') {
        return doc.name.replace(/([A-Z])/g, function($1) {
          return '-' + $1.toLowerCase();
        });
      }

      return doc.label || doc.name;
    }
  });
