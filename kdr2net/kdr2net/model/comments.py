
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Text, DateTime

from kdr2net.model.meta import Base

import cgi
import datetime

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    target = Column(String(60), nullable=False)
    date = Column(DateTime)
    author = Column(String(12), nullable=False)
    email = Column(String(30), nullable=False)
    url = Column(String(256), nullable=False)
    content = Column(Text)

    def __init__(self,data):
        self.target=data['target']
        self.date=datetime.datetime.now()
        self.author=data['name']
        self.email=data['email']
        self.url=data['url']
        self.content=cgi.escape(data['content'])

    def dict(self):
        return {
            'target':self.target,
            'date':self.date.strftime("%D %H:%M"),
            'author':self.author,
            'url':self.url,
            'content':self.content
            }

    def __repr__(self):
        return u"<comment>:%s" % (self.dict());
