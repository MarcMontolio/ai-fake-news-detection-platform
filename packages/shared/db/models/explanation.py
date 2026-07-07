from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from packages.shared.db.base import Base

if TYPE_CHECKING:
    from packages.shared.db.models.analysis import Analysis


class Explanation(Base):
    __tablename__ = "explanations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    analysis_id: Mapped[int] = mapped_column(
        ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False
    )
    feature: Mapped[str] = mapped_column(String(255), nullable=False)
    impact: Mapped[str] = mapped_column(String(50), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)

    analysis: Mapped[Analysis] = relationship("Analysis", back_populates="explanations")
