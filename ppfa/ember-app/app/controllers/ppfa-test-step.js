import Ember from "ember";

import OperisPpfateststepController from 'ember-app/controllers/operis-ppfa-test-step';

var PpfateststepController = OperisPpfateststepController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('ppfa-test-steps.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default PpfateststepController;