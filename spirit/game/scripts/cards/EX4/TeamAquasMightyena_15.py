"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Mightyena (EX4 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import conditions_if
from spirit.game.card_effects.ex import defender_is_ex

card = PokemonCardDef(
    guid="a52b86b1-8654-5a1f-aa5f-65623b356218",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMightyena.Name",
    display_name="Team Aqua's Mightyena",
    searchable_by=["Team Aqua's Mightyena", "Stage 1", "TeamAquasMightyena"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Mystic Fang",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=conditions_if(defender_is_ex, SpecialConditions.CONFUSED),
        ),
    ],
)