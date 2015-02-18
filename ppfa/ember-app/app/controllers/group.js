import Ember from "ember";

import OperisGroupController from 'ember-app/controllers/operis-group';

var GroupController = OperisGroupController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('groups.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default GroupController;