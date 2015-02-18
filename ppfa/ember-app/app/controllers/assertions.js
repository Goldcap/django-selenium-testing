import Ember from 'ember';         

var IndexPpfatestrunassertionsController = Ember.Controller.extend({
    
    sortProperties: ['date_created'],
    sortAscending: false,
    
    init: function() {
        Ember.Logger.info("Heynow");
        this._super();
    },
    
    sortedContent: function() {
        var content;
        content = this.get("model") || [];
        Ember.Logger.info(content);
        return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin, {
          content: content.toArray(),
          sortProperties: this.get('sortProperties'),
          sortAscending: this.get('sortAscending')
        });
    }.property("model.@each", 'sortProperties', 'sortAscending'),
    
  
});

export default IndexPpfatestrunassertionsController;