import datetime                         
import sys
import os.path
from inspect import getmembers, isclass
from collections import defaultdict
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db.models.base import ModelBase

from jinja2 import FileSystemLoader, Environment, PackageLoader, ChoiceLoader

from operis.log import log
from operis.utils import convert, convert_friendly, underscore

#This command takes an input table of artifacts, of a specific format,
#And ensures that image attatchments for each artifact in the table are created
#Then sets those images up to be parsed by the IKGEN.py

class Command(BaseCommand):
    help = 'Creates Generic Ember Models' 
    logger = None
    
    option_list = BaseCommand.option_list + (
        make_option('--regenerate',
            action='store_true',
            dest='regenerate',
            default=False,
            help='Wipe Prior instances'),
        )

    def handle(self, *args, **options):
        
        self.logger = log( self )
        
        wipe = False
        if options['regenerate']:
            wipe = True
            
        modules = map(__import__, settings.EMBER_MODELS)
        
        model_instances = defaultdict(list)
        for model in modules:
            for name, obj in getmembers(model.models):
                if isclass(obj):
                    model = []
                    if isinstance(obj, ModelBase):
                        self.logger.log("Object Name is: %s",[obj.__name__],"info")
                        has_parent = False
                        
                        for f in obj._meta.fields:
                            if hasattr(obj ,"Ember") and hasattr(obj.Ember,'fields'):
                                if f.name not in obj.Ember.fields:
                                    continue
                            field = {}
                            field['name'] = convert(f.name) 
                            field['name_underscore'] = underscore(f.name) 
                            field['name_friendly'] = convert_friendly(f.name)
                            field['type'] = f.get_internal_type()
                            self.logger.log("Field Type is: %s",[f.get_internal_type()],"info")
                        
                            if field['type'] == "ForeignKey":
                                has_parent = True
                            #self.logger.log("Field %s",[f.name],"info")
                            #self.logger.log("Field %s",[field['type']],"info")
                            model.append(field)
                            # resolve picklists/choices, with get_xyz_display() function
                        
                        #Generate Implied One-To-Many Relationships
                        for f in obj._meta.get_all_related_objects():
                            if hasattr(f.model ,"Ember"):
                                field = {}
                                field['name'] = convert(f.model.__name__)
                                field['name_underscore'] = underscore(f.model.__name__)
                                field['name_friendly'] = convert_friendly(f.opts.module_name)
                                field['type'] = "OneToMany"   
                                
                                if hasattr(f.model._meta ,"verbose_name_plural"):
                                    field['plural_name'] = convert(unicode(f.model._meta.verbose_name_plural))
                                    field['plural_name_underscore'] = underscore(unicode(f.model._meta.verbose_name_plural))
                      
                                model.append(field)
                            
                        index_list = ['id']
                        index_converted = []
                        plural = None
                        plural_converted = None
                        #Add to our Plural-Item Controllers
                        if hasattr(obj ,"Ember"):
                            if hasattr(obj.Ember,'index_list'):
                                index_list = []
                                for f in obj.Ember.index_list:
                                    index_list.append(convert(f))
                                    index_converted.append(convert_friendly(f))
                                    # resolve picklists/choices, with get_xyz_display() function
                               
                        if hasattr(obj._meta ,"verbose_name_plural"):
                            plural = unicode(obj._meta.verbose_name_plural)
                      
                        item = {    "model": model, 
                                    "singular": unicode(obj.__name__).title(), 
                                    "singular_converted": convert(unicode(obj.__name__)),
                                    "plural": plural.title(),
                                    "plural_converted": convert(plural),
                                    "index_list": index_list,
                                    "index_converted": index_converted,
                                    "has_parent": has_parent
                                }
                        model_instances[obj.__name__] = item
                        print obj.__name__
        
        global_exts = getattr(settings, 'JINJA_EXTS', ())
        env = Environment(extensions=global_exts,loader=FileSystemLoader('templates'))
        
        self.logger.log("Directory is %s",[settings.PROJECT_DIR + "../" + settings.EMBER_APP_NAME],"info")
        
        for k,v in model_instances.iteritems():
            
            self.logger.log("Creating Base Model for %s",[k],"info")
            self.logger.log("Has Parent is: %s",[v['has_parent']],"info")
                        
            template = env.get_template('ember/models/model.js')
            args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
            output = template.render(args)
            file = open(settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/models/operis-" + v["singular_converted"] + ".js", "w")
            file.write(output)
            file.close()
            
            filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/models/" + v["singular_converted"] + ".js"
            if not os.path.isfile(filename) or wipe:
                self.logger.log("Creating Instance Model for %s",[k],"info")
                template = env.get_template('ember/models/instance.js')
                args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                output = template.render(args)
                file = open(filename, "w")
                file.write(output)
                file.close()
        
            self.logger.log("Creating Single Instance Controller for %s",[k],"info")
            template = env.get_template('ember/controllers/single.js')
            args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
            output = template.render(args)
            file = open(settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/controllers/operis-" + v["singular_converted"] + ".js", "w")
            file.write(output)
            file.close()
            
            filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/controllers/" + v["singular_converted"] + ".js"
            if not os.path.isfile(filename) or wipe:
                self.logger.log("Creating Single Controller for %s",[k],"info")
                template = env.get_template('ember/controllers/instance_single.js')
                args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                output = template.render(args)
                file = open(filename, "w")
                file.write(output)
                file.close()
            
            self.logger.log("Creating Base Route for %s",[k],"info")
            template = env.get_template('ember/routes/single.js')
            args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
            output = template.render(args)
            file = open(settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/routes/operis-" + v["singular_converted"] + ".js", "w")
            file.write(output)
            file.close()
            
            filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/routes/" + v["singular_converted"] + ".js"
            if not os.path.isfile(filename) or wipe:
                self.logger.log("Creating Single Instance Route for %s",[k],"info")
                template = env.get_template('ember/routes/instance_single.js')
                args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                output = template.render(args)
                file = open(filename, "w")
                file.write(output)
                file.close()

            filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/templates/" + v["singular_converted"] + ".hbs"
            if not os.path.isfile(filename) or wipe:
                self.logger.log("Creating Single Template for %s",[k],"info")
                template = env.get_template('ember/templates/single.handlebars')
                args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                output = template.render(args)
                file = open(filename, "w")
                file.write(output)
                file.close()
            
            if v["plural"]: 
                
                self.logger.log("Creating Plural Base Controller for %s",[k],"info")
                template = env.get_template('ember/controllers/plural.js')
                args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                output = template.render(args)
                file = open(settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/controllers/operis-" + v["plural_converted"] + ".js", "w")
                file.write(output)
                file.close()
                
                filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/controllers/" + v["plural_converted"] + ".js"
                if not os.path.isfile(filename) or wipe:
                    self.logger.log("Creating Plural Controller for %s",[k],"info")
                    template = env.get_template('ember/controllers/instance_plural.js')
                    args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                    output = template.render(args)
                    file = open(filename, "w")
                    file.write(output)
                    file.close()
                    
                self.logger.log("Creating Plural Base Route for %s",[k],"info")
                template = env.get_template('ember/routes/plural.js')
                args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                output = template.render(args)
                file = open(settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/routes/operis-" + v["plural_converted"] + ".js", "w")
                file.write(output)
                file.close()
                
                filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/routes/" + v["plural_converted"] + ".js"
                if not os.path.isfile(filename) or wipe:
                    self.logger.log("Creating Plural Instance Route for %s",[k],"info")
                    template = env.get_template('ember/routes/instance_plural.js')
                    args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                    output = template.render(args)
                    file = open(filename, "w")
                    file.write(output)
                    file.close()
    
                filename = settings.PROJECT_DIR + "/../" + settings.EMBER_APP_NAME + "/app/templates/" + v["plural_converted"] + ".hbs"
                if not os.path.isfile(filename) or wipe:
                    self.logger.log("Creating Plural Template for %s",[k],"info")
                    template = env.get_template('ember/templates/plural.handlebars')
                    args = {"model":v,"ember_app_name":settings.EMBER_APP_NAME}
                    output = template.render(args)
                    file = open(filename, "w")
                    file.write(output)
                    file.close()
                
                
            
        self.logger.log("Done, templates are in %s",[settings.EMBER_APP_NAME],"info")
        