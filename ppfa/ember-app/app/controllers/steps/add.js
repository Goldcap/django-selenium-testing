import Ember from "ember";
import OperisPpfateststepController from 'ember-app/controllers/operis-ppfa-test-step';

var IndexPpfateststepAddController = OperisPpfateststepController.extend({
   
    needs: ['test','steps'],
    addedBinding: 'controllers.steps.added',
    
    isNew: true,
    
    actions: {
        // Save and transition to /products/:product_id only if validation passes.
        create: function(ppfa_step) {
          var scope = this;
          var test = this.get('controllers.test.model');
          ppfa_step.validate().then(function() {
            ppfa_step.save().then(function(ppfa_step) {
                scope.set('added',ppfa_step);
                test.get('ppfa_test_steps').addObject(ppfa_step); 
                scope.transitionToRoute("steps");
            });
          });
        }
    }
   
});

export default IndexPpfateststepAddController;