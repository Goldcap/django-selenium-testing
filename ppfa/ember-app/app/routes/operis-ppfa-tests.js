import Ember from 'ember';
//import Ppfatest from 'ember-app/models/ppfa-test';

var OperisPpfatestsRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('ppfa_test', params);
    }
});

export default OperisPpfatestsRoute;