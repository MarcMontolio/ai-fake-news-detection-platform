from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from packages.shared.db.models import Article


class ArticleRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self,
        *,
        title: str,
        content: str,
        source_url: str | None = None,
        source_domain: str | None = None,
    ) -> Article:
        article = Article(
            title=title,
            content=content,
            source_url=source_url,
            source_domain=source_domain,
        )

        self.session.add(article)
        self.session.commit()
        self.session.refresh(article)

        return article

    def get_by_id(self, article_id: int) -> Article | None:
        return self.session.get(Article, article_id)

    def list_recent(self, limit: int = 10) -> list[Article]:
        statement = select(Article).order_by(desc(Article.created_at)).limit(limit)

        return list(self.session.scalars(statement).all())
