"use strict";

// var KnockoutTestMe = (function () {

//     function init() {
//         console.log('this worked as well');
//         ko.applyBindings(new KnockoutTestViewModel(), document.getElementById('knockout-test'));
//     };

//     console.log('this was a success!');

//     function KnockoutTestViewModel() {
//         var self = this;

//         self.firstName = ko.observable('Bert');
//         self.lastName = ko.observable('Bertington');

//         self.fullName = ko.computed(function() {
//             return self.firstName() + " " + self.lastName();
//         }, self);
//     }

//     return {
//         init: init,
//         KnockoutTestViewModel: KnockoutTestViewModel
//     }
// })();

var KnockoutTestMe = (function () {

    function init() {
        console.log('this worked as well');
        ko.applyBindings(new KnockoutTestViewModel(), document.getElementById('knockout-test'));
    };

    console.log('this was a success!');

    ko.components.register('like-widget', {
        viewModel: function(params) {
            console.log('inside component.register');
            // Data: value is either null, 'like', or 'dislike'
            this.chosenValue = params.value;
             
            // Behaviors
            this.like = function() { this.chosenValue('like'); }.bind(this);
            this.dislike = function() { this.chosenValue('dislike'); }.bind(this);
        },
        template:
            '<div class="like-or-dislike" data-bind="visible: !chosenValue()">\
                <button data-bind="click: like">Like it</button>\
                <button data-bind="click: dislike">Dislike it</button>\
            </div>\
            <div class="result" data-bind="visible: chosenValue">\
                You <strong data-bind="text: chosenValue"></strong> it\
            </div>'
    });

    function Product(name, rating) {
        var self = this;
        self.name = name;
        self.userRating = ko.observable(rating || null);
    }

    function KnockoutTestViewModel() {
        var self = this;

        this.products = [
            new Product('Garlic bread'),
            new Product('Pain au chocolat'),
            new Product('Seagull spaghetti', 'like') // This one was already 'liked'
        ];
    }

    return {
        init: init,
        KnockoutTestViewModel: KnockoutTestViewModel
    }
})();