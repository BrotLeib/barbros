// Index Controller

var indexController = (function () {

})();

var UIController = (function () {

    var DOMstrings = {
        carousel: '.carousel',
    };

    return {
        getDomStrings: function () {
            return DOMstrings;
        },

    }

})();

var controller = (function (indexCtrl, UICtrl) {
    
    var setupEventListeners = function () {
        var DOM = UICtrl.getDomStrings();

    }

    return {
        init : function () {
            console.log('Application startet');
            setupEventListeners()

        }
    }

})(indexController, UIController);

controller.init()