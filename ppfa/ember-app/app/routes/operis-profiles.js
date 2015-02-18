import Ember from 'ember';
//import Profile from 'ember-app/models/profile';

var OperisProfilesRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('profile', params);
    }
});

export default OperisProfilesRoute;