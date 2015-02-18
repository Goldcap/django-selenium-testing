//import Ember from "ember";
import OperisPpfatestRoute from "ember-app/routes/operis-ppfa-test";
                                
var IndexAddRoute = OperisPpfatestRoute.extend({
    
    model: function() {
        return this.store.createRecord('ppfa_test');
    },
 
    isNew: true,
    
    // Roll back if the user transitions away by clicking a link, clicking the
    // browser's back button, or otherwise.
    deactivate: function() {
        var model = this.modelFor('test.add');
        if (model && model.get('isNew') && !model.get('isSaving')) {
            model.destroyRecord();
        }
    }
 
});

export default IndexAddRoute;
