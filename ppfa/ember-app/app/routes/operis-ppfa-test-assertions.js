import Ember from 'ember';
//import Ppfatestassertion from 'ember-app/models/ppfa-test-assertion';

var OperisPpfatestassertionsRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('ppfa-test-assertion', params);
    }
});

export default OperisPpfatestassertionsRoute;