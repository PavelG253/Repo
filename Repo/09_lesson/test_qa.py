from subject_page import SubjectPage


def test_add_subject():

    page = SubjectPage()

    subject_id = page.create_subject(20, "Алгебра")
    assert subject_id == 20

    page.delete_subject(subject_id)


def test_update_subject():

    page = SubjectPage()

    subject_id = page.create_subject(22, "География")
    page.update_subject_title(22, "Астрономия")

    updated_subject = page.get_subject_by_id(subject_id)
    assert updated_subject[1] == "Астрономия"

    page.delete_subject(subject_id)


def test_delete_subject():

    page = SubjectPage()

    subject_id = page.create_subject(11, "Обществоведение")
    page.delete_subject(subject_id)

    subject_after = page.get_subject_by_id(subject_id)
    assert subject_after is None
