import Ember from 'ember';
import DS from "ember-data";

var OperisProfile = DS.Model.extend(Ember.Validations.Mixin,{
  user: DS.belongsTo('user'),
  first_name: DS.attr('string'),
  last_name: DS.attr('string'),
  date_submitted: DS.attr('isodate'),
  approved: DS.attr('number')
});
export default OperisProfile;