import Ember from 'ember';                                        
import OperisPpfateststepsController from 'ember-app/controllers/operis-ppfa-test-steps';

var IndexPpfateststepsController = OperisPpfateststepsController.extend({
    
    queryParams: ['page_steps'],    
    paginatable_var: "page_steps",
    sortProperties: ['id'],
    sortAscending: false,
    
    actions: {
        delete: function( ppfa_step ) {
            var scope = this;
            ppfa_step.destroyRecord().then(function(ppfa_step) {
                scope.set('deleted',ppfa_step);
            });
        }
    }
    
});

export default IndexPpfateststepsController;