//import Ember from "ember";
import OperisPpfatestController from 'ember-app/controllers/operis-ppfa-test';

var IndexAddController = OperisPpfatestController.extend({
   
    needs: 'index',
    addedBinding: 'controllers.index.added',
    
    actions: {
        // Save and transition to /products/:product_id only if validation passes.
        create: function(ppfa_test) {
          var scope = this;
          ppfa_test.validate().then(function() {
            ppfa_test.save().then(function(ppfa_test) {
                scope.set('added',ppfa_test);
                scope.transitionToRoute('index');
            });
          });
        }
        
    }
   
});

export default IndexAddController;