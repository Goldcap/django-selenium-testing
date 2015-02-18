//import Ember from "ember";
import OperisPpfatestRoute from "ember-app/routes/operis-ppfa-test";
                                
var IndexEditRoute = OperisPpfatestRoute.extend({
    
    renderTemplate: function(controller) {
        this.render('test.add', {
          controller: controller
        });
    },
    
    // Roll back if the user transitions away by clicking a link, clicking the
    // browser's back button, or otherwise.
    deactivate: function() {
    var model = this.modelFor('test.edit');
        if (model && model.get('isDirty') && !model.get('isSaving')) {
          model.rollback();
        }
    }
 
});

export default IndexEditRoute;
