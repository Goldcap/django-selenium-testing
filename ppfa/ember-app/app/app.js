import Ember from 'ember';
import Resolver from 'ember/resolver';
import loadInitializers from 'ember/load-initializers';

Ember.MODEL_FACTORY_INJECTIONS = true;

var App = Ember.Application.extend({
  modulePrefix: 'ember-app', // TODO: loaded via config
  Resolver: Resolver,
  rootElement: '#ember-app',
  foundationLoaded: false
});

loadInitializers(App, 'ember-app');

export default App;
