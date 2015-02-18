import Ember from 'ember';
//import Ppfatestrun from 'ember-app/models/ppfa-test-run';

var OperisPpfatestrunsRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('ppfa-test-run', params);
    }
});

export default OperisPpfatestrunsRoute;