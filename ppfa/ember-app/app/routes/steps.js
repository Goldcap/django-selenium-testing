import Ember from 'ember';
//import Ppfatest from 'ember-app/models/ppfa-test';

var OperisPpfateststepsRoute = Ember.Route.extend({
    queryParams: {
        page_steps: {
          refreshModel: true
        }
    },
    
    model: function() {
        var test = this.modelFor('test');
        Ember.Logger.info(test);
        return test.get('ppfa_test_steps');
    }
});

export default OperisPpfateststepsRoute;