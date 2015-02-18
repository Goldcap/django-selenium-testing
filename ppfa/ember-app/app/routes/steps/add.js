//import Ember from "ember";
import OperisPpfateststepRoute from "ember-app/routes/operis-ppfa-test-step";
                                
var IndexPpfateststepAddRoute = OperisPpfateststepRoute.extend({
    
    model: function() {
        var test = this.modelFor('test');
        return this.store.createRecord('ppfa_test_step',{
            "ppfa_test": test
        });
    },
    
    renderTemplate: function() {
        this.render({ 
           into: "steps"
         });
    },
    
    isNew: true,
    
    // Roll back if the user transitions away by clicking a link, clicking the
    // browser's back button, or otherwise.
    deactivate: function() {
        var model = this.modelFor('steps.add');
        if (model && model.get('isNew') && !model.get('isSaving')) {
            model.destroyRecord();
        }
    }
 
});

export default IndexPpfateststepAddRoute;
