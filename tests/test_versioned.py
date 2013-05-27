import sqlalchemy as sa
from tests import TestCase


class TestVersionedModel(TestCase):
    def test_builds_relationship(self):
        assert self.Article.versions

    def test_parent_has_versioned_class_defined(self):
        assert self.Article.__versioned__['class']

    def test_versioned_model_has_table_object(self):
        assert isinstance(
            self.Article.__versioned__['class'].__table__, sa.Table
        )

    def test_versioned_table_structure(self):
        table = self.Article.__versioned__['class'].__table__
        assert 'id' in table.c
        assert 'name' in table.c
        assert 'content' in table.c
        assert 'description'in table.c

    def test_creates_versions_on_session_commit(self):
        article = self.Article()
        article.name = u'Some article'
        article.content = u'Some content'
        self.session.add(article)
        self.session.commit()

        article.name = u'Updated name'
        article.content = u'Updated content'

        self.session.commit()
        self.session.refresh(article)
        version = article.versions.all()[0]
        assert version.name == u'Some article'
        assert version.content == u'Some content'
        assert version.transaction.id == 1
        assert version.transaction_id == 1

    def test_relationships(self):
        article = self.Article()
        article.name = u'Some article'
        article.content = u'Some content'
        article.tags.append(self.Tag(name=u'some tag'))

        self.session.commit()
        version = article.versions.all()[0]
        assert version.name == u'Some article'
