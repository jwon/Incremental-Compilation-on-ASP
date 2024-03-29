# really dumb example of using templates w/asp

class ArrayDoubler(object):
    
    def __init__(self):
        self.pure_python = True

    def double_using_template(self, arr):
        import asp.codegen.templating.template as template
        mytemplate = template.Template(filename="templates/double_template.mako", disable_unicode=True)
        rendered = mytemplate.render(num_items=len(arr))

        import asp.jit.asp_module as asp_module
        mod = asp_module.ASPModule()
        #submod1 = asp_module.ASPSubModule()
        #submod1.add_function("double_in_c", rendered)
        #submod2 = asp_module.ASPSubModule()
        #submod2.add_function("double_in_blah", rendered2)
        #mod.add(submod1)
        #mod.add(submod2)
        #return mod.double_in_c(arr)
        # remember, must specify function name when using a string
        mod.add_function("double_in_c", rendered)
        return mod.double_in_c(arr)

    def double(self, arr):
        return map (lambda x: x*2, arr)
        

