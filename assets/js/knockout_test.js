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

    function UtilityFunctions() {

        console.log('exercise');
        console.log($('#exercise'));
        $('#exercise').append('<h1>Hello World</h1>');
        // document.getElementById('exercise').appendChild('<h1>Hello World</h1>');

        $('[data-role=master_container]').on('click', '[data-action=test_button]', function(e) {
            var self = this;

            var $master_container = $(e.delegateTarget);
            // var $test_button_container = $(e.delegateTarget);
            var $test_code_container = $($master_container).find('[data-role=test_code_container]');
            var $test_button = $(e.currentTarget);

            console.log('$test_button.text: ', $test_button.text());

            // var $data_info = $($master_container).find('[data-role=test_code_container]');
            // var routeId = $data_info.data('info');
            // console.log('routeId: ', routeId);

            // $data_info.css('display', 

            // var $test_code_container = $master_container.find(['data-role=test_code_container']);
            // console.log('$test_code_container: ', $test_code_container);

            console.log('$master_container: ', $master_container);
            // console.log('$test-button-container: ', $test_button_container);
            console.log('$test-button: ', $test_button);

            console.log('#test-button clicked!');
            console.log(self);
            console.log($(self));
            console.log($(this));

            if ($test_button.text() === 'SHOW CODE +') {
                $test_button.text('HIDE CODE -');
                $test_code_container.css('display', 'block');
            } else {
                $test_button.text('SHOW CODE +');
                $test_code_container.css('display', 'none');
            }
            // $(self).next('[data-role=test_code_container]').css('display: block');
        });
    };
    

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
        UtilityFunctions: UtilityFunctions,
        KnockoutTestViewModel: KnockoutTestViewModel
    }
})();