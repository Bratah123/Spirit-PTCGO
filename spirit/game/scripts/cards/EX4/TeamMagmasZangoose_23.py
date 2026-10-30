"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Zangoose (EX4 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_typed_or_team, team_play_damage

card = PokemonCardDef(
    guid="2680f85b-01db-5074-acca-164640d7bee2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasZangoose.Name",
    display_name="Team Magma's Zangoose",
    searchable_by=["Team Magma's Zangoose", "Basic", "TeamMagmasZangoose"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Colorless Basic Pok\u00e9mon or Basic Pok\u00e9mon with Team Magma in its name and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=call_for_family_typed_or_team(PokemonTypes.COLORLESS, "Team Magma"),
        ),
        Attack(
            title="Team Play",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play with Team Magma in its name.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=team_play_damage("Team Magma", 10),
        ),
    ],
)