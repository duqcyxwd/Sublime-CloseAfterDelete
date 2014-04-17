import sublime_plugin
import sublime
import os

class DeleteAfterCloseCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirmed = 'false'):
		sublime.status_message("DeleteCloseCommand")
		window = sublime.active_window()
		view = sublime.Window.active_view(window)
		fileName = view.file_name()
		if (fileName != None and os.path.isfile(view.file_name())):
			sublime.status_message("Remove file")
			os.remove(fileName)
			window.run_command('close_file')
