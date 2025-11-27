from sqlalchemy import create_engine, text

sqlA = "INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"
sqlB = "SELECT * FROM subject WHERE subject_id = :subject_id"
sqlC = "UPDATE subject SET subject_title = :title WHERE subject_id = :id"
sqlD = "DELETE FROM subject WHERE subject_id = :id"


class SubjectPage:
    def __init__(self, database_url=(
            "postgresql://postgres:Passage2024!@localhost:5432/QA")
    ):
        self.engine = create_engine(database_url)

    def create_subject(self, subject_id, title):

        with self.engine.connect() as conn:
            conn.execute(text(sqlA), {"id": subject_id, "title": title})
            conn.commit()
            return subject_id

    def get_subject_by_id(self, subject_id):

        with self.engine.connect() as conn:
            result = conn.execute(text(sqlB), {"subject_id": subject_id})
            return result.first()

    def update_subject_title(self, subject_id, new_title):

        with self.engine.connect() as conn:
            conn.execute(text(sqlC), {"title": new_title, "id": subject_id})
            conn.commit()

    def delete_subject(self, subject_id):

        with self.engine.connect() as conn:
            conn.execute(text(sqlD), {"id": subject_id})
            conn.commit()
