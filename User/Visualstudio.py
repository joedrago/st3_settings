import os, sublime, sublime_plugin

class VisualstudioCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      f = self.view.file_name();
      cmd = 'cmd /c start "ignored" "%(args)s"' % {'args' : f } # stderr > out.txt 2>&1
      result = os.system(cmd)
