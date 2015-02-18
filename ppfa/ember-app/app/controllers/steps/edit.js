//import Ember from "ember";
import OperisPpfatestController from 'ember-app/controllers/operis-ppfa-test';

var IndexEditController = OperisPpfatestController.extend({
   
    actions: {
        // Save and transition to /products/:product_id only if validation passes.
        edit: function(ppfa_step) {
          var scope = this;
          ppfa_step.validate().then(function() {
            ppfa_step.save().then(function(ppfa_step) {
                scope.transitionToRoute('index.test.steps');
            });
          });
        }
        
    }
   
});

export default IndexEditController;