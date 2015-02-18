import Ember from "ember";

import OperisPpfatestrunController from 'ember-app/controllers/operis-ppfa-test-run';

var PpfatestrunController = OperisPpfatestrunController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('ppfa-test-runs.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default PpfatestrunController;