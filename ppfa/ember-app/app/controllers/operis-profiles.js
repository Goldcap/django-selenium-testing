import Ember from 'ember';
import PaginatableChild from 'ember-app/mixins/paginatable-child';

var OperisProfilesController = Ember.ArrayController.extend( PaginatableChild, {});

export default  OperisProfilesController;  