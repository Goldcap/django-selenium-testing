import Ember from 'ember';
//import Ppfatest from 'ember-app/models/ppfa-test';

var OperisPpfatestrunsRoute = Ember.Route.extend({
    
    queryParams: {
        page_runs: {
          refreshModel: true
        }
    },
    
    model: function() {
        var test = this.modelFor('test');
        return test.get('ppfa_test_runs');
    }
});

export default OperisPpfatestrunsRoute;
