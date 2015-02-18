import Ember from "ember";

import OperisUserController from 'ember-app/controllers/operis-user';

var UserController = OperisUserController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('users.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default UserController;