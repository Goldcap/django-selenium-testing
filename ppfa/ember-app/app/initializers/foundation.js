import Ember from 'ember';

export default {
  name: 'foundation',
  initialize: function(container, app) {
    Ember.View.reopen({
      didInsertElement : function(){
        if (! app.get('foundationLoaded')) {
            Ember.$(document).foundation();                 
            app.set('foundationLoaded',true);
        }
      },
      afterRenderEvent : function(){
        // Implement this hook in your own subclasses and run your jQuery logic there.
        // Do not add code here as this fires after EVERY didInsertElement event
      }
    });
  }
};