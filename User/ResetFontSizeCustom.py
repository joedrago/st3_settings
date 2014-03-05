import sublime, sublime_plugin
class ResetFontSizeCustomCommand(sublime_plugin.ApplicationCommand):
    def run(self, size):
        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('font_size', size)
        sublime.save_settings('Preferences.sublime-settings')
