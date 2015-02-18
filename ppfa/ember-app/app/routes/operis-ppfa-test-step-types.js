import Ember from 'ember';
//import Ppfateststeptype from 'ember-app/models/ppfa-test-step-type';

var OperisPpfateststeptypesRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('ppfa-test-step-type', params);
    }
});

export default OperisPpfateststeptypesRoute;