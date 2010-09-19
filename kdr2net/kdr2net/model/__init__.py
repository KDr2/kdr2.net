"""The application's model objects"""
from kdr2net.model.meta import Session, Base

from kdr2net.model.comments import Comment

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
