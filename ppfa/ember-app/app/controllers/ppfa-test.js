import Ember from "ember";

import OperisPpfatestController from 'ember-app/controllers/operis-ppfa-test';

var PpfatestController = OperisPpfatestController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('ppfa-tests.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default PpfatestController;