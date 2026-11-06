from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_team_plasma_pokemon


card = PokemonCardDef(
    guid="9c2679ea-c58b-549e-891f-e766f2108cc7",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Kick of Righteousness",
            game_text="If the Defending Pok\u00e9mon is a Team Plasma Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(active_is(is_team_plasma_pokemon), 40),
        ),
        Attack(
            title="Low Sweep",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)