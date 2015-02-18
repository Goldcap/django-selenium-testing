import Ember from 'ember';   
import OperisPpfatestrunsController from 'ember-app/controllers/operis-ppfa-test-runs';     

var IndexPpfatestrunsController = OperisPpfatestrunsController.extend({
    
    needs: ['test'],
    
    queryParams: ['page_runs'],    
    paginatable_var: "page_runs",
    sortProperties: ['date_created'],
    sortAscending: false, 
    
    init: function() {
        
        this._super();
    },
        
    actions: {
        delete: function( ppfa_test_run ) {
            var scope = this;
            var ppfa_test = ppfa_test_run.get('ppfa_test');
            ppfa_test_run.destroyRecord().then(function() {
                ppfa_test.save().then(function() {
                    scope.set('deleted',ppfa_test_run);
                    scope.transitionToRoute('runs');
                });
            });
        }
    }
    
});

export default IndexPpfatestrunsController;