import base64
import requests
from odoo import models, fields, api
from odoo.exceptions import UserError


class JobApplication(models.Model):
    _name = 'job.application'
    _description = 'Job Application'

    name = fields.Char('Job Description Name')
    job_description = fields.Binary('Job Description PDF', attachment=True)
    resume_ids = fields.One2many('job.application.resume', 'application_id', string='Resumes')
    resume_files = fields.Many2many('ir.attachment', string='Upload Resumes')
    result_ids = fields.One2many('job.application.result', 'application_id',
                                 string='Results')  # Nouveau champ pour les résultats

    def get_access_token(self):
        """Obtenir le token JWT pour l'authentification."""
        url = 'http://127.0.0.1:5000/login'
        credentials = {'username': 'slim',
                       'password': '20102011'}
        response = requests.post(url, json=credentials)
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise UserError('Erreur d\'authentification : {}'.format(response.text))

    def send_to_flask_api(self):
        self.ensure_one()
        access_token = self.get_access_token()

        job_description = base64.b64decode(self.job_description)

        resumes = []
        for attachment in self.resume_files:
            resume_content = base64.b64decode(attachment.datas)
            resumes.append(('resumes[]', (attachment.name, resume_content)))

        files = [('job_description', ('job_description.pdf', job_description))] + resumes
        headers = {'Authorization': 'Bearer {}'.format(access_token)}

        response = requests.post('http://127.0.0.1:5000/upload', files=files, headers=headers)

        if response.status_code == 200:
            result_data = response.json()
            # Supprimer les anciens résultats
            self.result_ids.unlink()
            # Créer de nouveaux enregistrements de résultats
            for result in result_data:
                # Accès aux données par leurs clés
                resume_path = result['path']
                cosine_similarity = result['cosine_similarity']
                self.env['job.application.result'].create({
                    'name': resume_path,  # Ou extraire le nom de fichier du chemin si nécessaire
                    'score': cosine_similarity,
                    'application_id': self.id,
                })
            return {
                'name': 'Results',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'job.application',
                'res_id': self.id,
                'views': [(False, 'form')],
                'target': 'new',
                'context': self.env.context,
            }
        else:
            raise UserError('Error: {}'.format(response.text))


class JobApplicationResume(models.Model):
    _name = 'job.application.resume'
    _description = 'Job Application Resume'

    name = fields.Char('Resume Name')
    resume_file = fields.Binary('Resume PDF', attachment=True)
    application_id = fields.Many2one('job.application', string='Application')


class JobApplicationResult(models.Model):
    _name = 'job.application.result'
    _description = 'Job Application Result'

    name = fields.Char('Resume Name')
    score = fields.Float('Matching Score')
    application_id = fields.Many2one('job.application', string='Application')
