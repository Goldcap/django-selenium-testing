//import Ember from "ember";
import OperisPpfateststepRoute from "ember-app/routes/operis-ppfa-test-step";
                                
var IndexPpfateststepEditRoute = OperisPpfateststepRoute.extend({
    
    renderTemplate: function(controller) {
        this.render('steps.add', {
          controller: controller
        });
    },
    
    // Roll back if the user transitions away by clicking a link, clicking the
    // browser's back button, or otherwise.
    deactivate: function() {
        var model = this.modelFor('steps.edit');
        if (model && model.get('isDirty') && !model.get('isSaving')) {
          model.rollback();
        }
    }
 
});

export default IndexPpfateststepEditRoute;
