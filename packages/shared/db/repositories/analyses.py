from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from packages.shared.db.models import Analysis


class AnalysisRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self,
        *,
        article_id: int,
        predicted_label: str,
        confidence: float,
        risk_level: str,
        model_version: str,
        credibility_score: float | None = None,
    ) -> Analysis:
        analysis = Analysis(
            article_id=article_id,
            predicted_label=predicted_label,
            confidence=confidence,
            risk_level=risk_level,
            model_version=model_version,
            credibility_score=credibility_score,
        )

        self.session.add(analysis)
        self.session.commit()
        self.session.refresh(analysis)

        return analysis

    def get_by_id(self, analysis_id: int) -> Analysis | None:
        return self.session.get(Analysis, analysis_id)

    def list_recent(self, limit: int = 10) -> list[Analysis]:
        statement = select(Analysis).order_by(desc(Analysis.created_at)).limit(limit)

        return list(self.session.scalars(statement).all())
