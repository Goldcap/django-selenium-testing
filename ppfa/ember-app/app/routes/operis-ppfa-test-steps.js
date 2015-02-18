import Ember from 'ember';
//import Ppfateststep from 'ember-app/models/ppfa-test-step';

var OperisPpfateststepsRoute = Ember.Route.extend({
  queryParams: {
    page: {
      refreshModel: true
    }
  },
  model: function( params ) {
      return this.store.find('ppfa-test-step', params);
    }
});

export default OperisPpfateststepsRoute;