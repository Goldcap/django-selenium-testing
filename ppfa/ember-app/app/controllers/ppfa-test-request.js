import Ember from "ember";

import OperisPpfatestrequestController from 'ember-app/controllers/operis-ppfa-test-request';

var PpfatestrequestController = OperisPpfatestrequestController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('ppfa-test-requests.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default PpfatestrequestController;