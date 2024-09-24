from PyQt5.QtCore import QObject
from modules.model.model import ProjectGPTModel
from modules.view.view import ProjectGPTView

class ProjectGPTController(QObject):
    def __init__(self):
        super().__init__()
        self.model = ProjectGPTModel()
        self.view = ProjectGPTView(self.model.available_models)

        self.view.request_panel.send_request_signal.connect(self.handle_send_request)
        self.view.request_panel.send_batch_request_signal.connect(self.handle_send_batch_request)
        self.view.batches_panel.get_completed_batch_jobs.connect(self.handle_get_completed_batch_jobs)

        self.model.response_generated.connect(self.view.update_response)

    def handle_send_request(self, model, role_string, full_request):
        project_dir, chosen_files = self.view.left_panel.get_checked_files()
        self.model.set_project_files(project_dir, chosen_files)
        self.model.generate_response(model, role_string, full_request)

    def handle_send_batch_request(self, model, role_string, full_request_template):
        project_dir, chosen_files = self.view.left_panel.get_checked_files()
        self.model.set_project_files(project_dir, chosen_files)
        self.model.generate_batch_response(model, role_string, full_request_template)

    def handle_get_completed_batch_jobs(self):
        # Handle the retrieval of completed batch jobs
        pass