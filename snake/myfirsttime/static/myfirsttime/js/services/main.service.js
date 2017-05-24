(function () {
  'use strict';

angular
        .module('Snake')
        .factory('MainService', MainService);

  MainService.$inject = ['$http', '$rootScope', '$timeout'];

  function MainService($http, $timeout) {
    var service = {};

    var currentUser;

    service.Main = Main;

    return service;

    function Main(username, points, callback) {
        $http.post('/scores', { player_name: username,
                                player_score: points,})
            .then(function onSuccess(response) {
                callback(response);
            }).catch(function onError(response) {
              alert("Failed. System error code: " + response.data.internalErrorCode);
              callback(false);
            });
    }
  }
})();
