import Ember from 'ember';
//import Ppfatestrequest from 'ember-app/models/ppfa-test-request';

var OperisPpfatestrequestsRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('ppfa-test-request', params);
    }
});

export default OperisPpfatestrequestsRoute;