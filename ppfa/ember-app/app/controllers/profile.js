import Ember from "ember";

import OperisProfileController from 'ember-app/controllers/operis-profile';

var ProfileController = OperisProfileController.extend({
   
   actions: {
        
        delete: function( item ) {
            Ember.Logger.info('Item is:', item);
            item.on('didDelete', this, function () {
                this.transitionToRoute('profiles.index', {queryParams: {page: 1}});
            });
            item.destroyRecord();
        }
        
   }
   
});

export default ProfileController;