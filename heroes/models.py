from sqlmodel import SQLModel, Field, Relationship


class HeroTeamLink(SQLModel, table=True):
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)


class Team(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str = Field(index=True)

    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


class HeroMissionLink(SQLModel, table=True):
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
    mission_id: int | None = Field(
        default=None, foreign_key="mission.id", primary_key=True
    )
    role: str = Field(default="member")

    hero: "Hero" = Relationship(back_populates="mission_links")
    mission: "Mission" = Relationship(back_populates="hero_links")


class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str | None = Field(default=None, index=True)
    age: int | None = None

    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
    mission_links: list["HeroMissionLink"] = Relationship(back_populates="hero")


class Mission(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(index=True)
    description: str | None = None

    hero_links: list["HeroMissionLink"] = Relationship(back_populates="mission")
