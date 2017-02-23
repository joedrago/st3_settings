import os, sublime, sublime_plugin

class RestyleCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      f = self.view.file_name()
      self.view.run_command('save')
      #exe = sublime.packagesPath()
      #exe = os.path.join(exe, "User")
      #exe = os.path.join(exe, "MyParser.exe")
      exe = "C:\\work\\nova_tools\\coding_style\\Restyle.bat"
      cmd = 'cmd /c %(exe)s "%(args)s"' % {'exe' : exe, 'args' : f } # stderr > out.txt 2>&1
      print(cmd)
      result = os.system(cmd)
