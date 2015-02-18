import Ember from "ember";

import OperisPpfateststeptypeController from 'ember-app/controllers/operis-ppfa-test-step-type';

var PpfateststeptypeController = OperisPpfateststeptypeController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('ppfa-test-step-types.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default PpfateststeptypeController;