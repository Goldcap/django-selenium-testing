import Ember from 'ember';
//import Ppfatest from 'ember-app/models/ppfa-test';

var OperisPpfatestassertionsRoute = Ember.Route.extend({
    
    renderTemplate: function() {
        this.render({ 
           into: "runs"
         });
    },
    
    model: function() {
        var test = this.modelFor('run');
        return test.get('ppfa_test_assertions');
    }
});

export default OperisPpfatestassertionsRoute;
