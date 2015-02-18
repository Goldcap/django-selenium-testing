import Ember from "ember";

import OperisPpfatestassertionController from 'ember-app/controllers/operis-ppfa-test-assertion';

var PpfatestassertionController = OperisPpfatestassertionController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('ppfa-test-assertions.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default PpfatestassertionController;