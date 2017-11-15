
// Index Controller

var indexController = (function () {

})();

var UIController = (function () {

})();

var controller = (function (indexCtrl, UICtrl) {
    
    var setupEventListeners = function () {

    }

    return {
        init : function () {
            console.log('Application startet');
            setupEventListeners()

        }
    }

})(indexController, UIController);

controller.init()