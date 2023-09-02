from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Float
import logging
import sqlalchemy

Base = declarative_base()


class PlayersStats(Base):
    __tablename__ = 'PLAYERS_STATS'
    id = Column(Integer, primary_key=True)
    season = Column(String(4), primary_key=True)
    role = Column(String(1), primary_key=True)
    mantra_role = Column(String(10))
    name = Column(String(50), primary_key=True)
    team = Column(String(25), primary_key=True)
    number_of_game_with_vote = Column(Integer, nullable=False, default=0)
    average_vote = Column(Float)
    average_fanta_vote = Column(Float)
    goal_made = Column(Integer)
    goal_taken = Column(Integer)
    penalty_saved = Column(Integer)
    penalty_kicked = Column(Integer)
    penalty_made = Column(Integer)
    penalty_missed = Column(Integer)
    assist = Column(Integer)
    yellow_card = Column(Integer)
    red_card = Column(Integer)
    autogol = Column(Integer)
    insert_datetime = Column(DateTime, nullable=False, server_default=sqlalchemy.sql.func.now())

    @staticmethod
    def bulk_insert(config, ps):
        with config.SESSION_MAKER() as session:
            try:
                session.bulk_save_objects(ps)
                session.commit()
                return session.query(PlayersStats).all()
            except SQLAlchemyError as e:
                session.rollback()
                logging.error(f"Error inserting {len(ps)} player stats")
                raise e

    def __str__(self):
        request = {
            'ticket_id': self.ticket_id,
            'service': self.service,
            'category': self.category,
            'status': self.status,
            'processor_id': self.processor_id
        }
        return request

