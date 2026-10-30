"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Seviper (EX4 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_typed_or_team, thick_poison

card = PokemonCardDef(
    guid="feb32897-07ab-56ed-bc77-ccd747680635",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSeviper.Name",
    display_name="Team Aqua's Seviper",
    searchable_by=["Team Aqua's Seviper", "Basic", "TeamAquasSeviper"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Grass Basic Pok\u00e9mon or Basic Pok\u00e9mon with Team Aqua in its name and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=call_for_family_typed_or_team(PokemonTypes.GRASS, "Team Aqua"),
        ),
        Attack(
            title="Thick Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and Poisoned. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=thick_poison(),
        ),
    ],
)