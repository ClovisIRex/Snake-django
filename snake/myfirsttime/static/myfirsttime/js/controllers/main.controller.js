(function () {
    'use strict';

    angular
        .module('Snake')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope','$location','MainService'];
    function MainController($scope,$location, $cookies, MainService) {
        var vm = this;

        vm.main = main;
        

        (function initController() {

        })();

        function main() {
            vm.dataLoading = true;
            MainService.Main(vm.username, vm.points,function (response) {
                if(response) {
                    MainService.SetScore(vm.username, vm.points);
                } else {
                    vm.dataLoading = false;
                }
            });     
        }
    }
})();

  

