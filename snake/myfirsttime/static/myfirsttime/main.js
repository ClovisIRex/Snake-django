(function () { 
	'use strict';
	angular
	.module("Snake", ['ngRoute'])
	.config(config)
	.run(run);

	config.$inject = ['$routeProvider', '$locationProvider', '$httpProvider'];
	function config($routeProvider, $locationProvider, $httpProvider) {
		$locationProvider.hashPrefix('');

		$httpProvider.defaults.withCredentials = true;

		$routeProvider

		/*
		---------LOGIN + REGISTER VIEWS--------
		*/
		.when("/", {
			controller: "MainController",
			templateUrl : "./game",
			controllerAs: "vm"
		})

		.otherwise({ redirectTo: '/' });
	}
	
	
		run.$inject = ['$rootScope', '$location','$http'];
		function run($rootScope,$location,$cookies, $http) {
			// 
		}
})();
	



