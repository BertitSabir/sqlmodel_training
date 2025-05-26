from sqlmodel import Session, select, col

from utils import get_database_url, get_engine, create_db_and_tables, get_session
from heroes.models import Hero, Team, Mission, HeroMissionLink, HeroTeamLink


def create_heroes(session: Session):
    # Heroes
    hero_batman = Hero(
        name='Batman',
        secret_name='Bruce Wayne',
        age=35
    )
    hero_superman = Hero(
        name='Superman',
        secret_name='Clark Kent',
        age=30
    )
    hero_flash = Hero(
        name='Flash',
        secret_name='Barry Allen',
        age=28
    )
    hero_cyborg = Hero(
        name='Cyborg',
        secret_name='Victor Stone',
        age=25
    )

    # Teams
    team_justice_league = Team(
        name='Justice League',
        headquarters='Gotham',
        heroes=[hero_batman, hero_superman, hero_flash]
    )
    team_humanity = Team(
        name='Humanity',
        headquarters='Earth',

    )
    team_humanity.heroes.append(hero_batman)
    team_humanity.heroes.append(hero_cyborg)

    # Add teams and heroes:
    session.add(team_justice_league)
    session.add(team_humanity)
    session.commit()
    session.refresh(team_justice_league)
    session.refresh(team_humanity)

    print(f'team: {team_justice_league}, heroes: {team_justice_league.heroes}')
    print(f'team: {team_humanity}, heroes: {team_humanity.heroes}')


def update_heros(session: Session):

    hero_batman = session.exec(select(Hero).where(col(Hero.name) == 'Batman')).first()
    hero_cyborg = session.exec(select(Hero).where(col(Hero.name) == 'Cyborg')).first()
    print(f'hero_batman hero found: {hero_batman}')
    team_justice = session.exec(select(Team).where(col(Team.name) == 'Justice League')).first()
    print(f'** team justice heroes before Batman retires: {team_justice.heroes}')
    team_justice.heroes.remove(hero_batman)
    team_justice.heroes.append(hero_cyborg)
    session.commit()
    session.refresh(team_justice)
    print(f'** team justice heroes after Batman retires and cyborg joins: {team_justice.heroes}')


def create_missions(session: Session):
    # Heroes
    hero_batman = Hero(
        name='Batman',
        secret_name='Bruce Wayne',
        age=35
    )
    hero_superman = Hero(
        name='Superman',
        secret_name='Clark Kent',
        age=30
    )
    hero_flash = Hero(
        name='Flash',
        secret_name='Barry Allen',
        age=28
    )
    hero_cyborg = Hero(
        name='Cyborg',
        secret_name='Victor Stone',
        age=25
    )

    # Missions
    mission_rescue = Mission(
        name='Rescue',
        description='Rescue civilians from a burning building',
    )
    mission_save_world = Mission(
        name='Save World',
        description='Save the world from an alien invasion',
    )

    # Hero Mission Links
    batman_mission_rescue_role = HeroMissionLink(
        hero=hero_batman,
        mission=mission_rescue,
        role='leader'
    )
    cyborg_mission_rescue_role = HeroMissionLink(
        hero=hero_cyborg,
        mission=mission_rescue,
        role='member'
    )
    flash_mission_save_world_role = HeroMissionLink(
        hero=hero_flash,
        mission=mission_save_world,
        role='member'
    )
    superman_mission_save_world_role = HeroMissionLink(
        hero=hero_superman,
        mission=mission_save_world,
        role='leader'
    )

    # Add missions and heroes:
    session.add(mission_rescue)
    session.add(mission_save_world)
    session.add(batman_mission_rescue_role)
    session.add(cyborg_mission_rescue_role)
    session.add(flash_mission_save_world_role)
    session.add(superman_mission_save_world_role)
    session.commit()
    session.refresh(mission_rescue)
    session.refresh(mission_save_world)
    print(f'mission: {mission_rescue}, heroes: {[link.hero.name for link in mission_rescue.hero_links]}')
    print(f'mission: {mission_save_world}, heroes: {[link.hero.name for link in mission_save_world.hero_links]}')


def update_missions(session: Session): ...


def app():
    db_url = get_database_url(name='heroes')
    engine = get_engine(db_url=db_url)
    create_db_and_tables(engine, models=[Hero, Team, Mission, HeroMissionLink, HeroTeamLink])
    with get_session(engine) as session:
        create_heroes(session)
        update_heros(session)
        create_missions(session)
        update_missions(session)


if __name__ == '__main__':
    app()