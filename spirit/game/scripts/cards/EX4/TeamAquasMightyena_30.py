"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Mightyena (EX4 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import aqua_call

card = PokemonCardDef(
    guid="1fc27e8f-6574-56c7-8717-d05dcc42a447",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMightyena.Name",
    display_name="Team Aqua's Mightyena",
    searchable_by=["Team Aqua's Mightyena", "Stage 1", "TeamAquasMightyena"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Aqua Call",
            game_text="Search your deck for Pok\u00e9mon that has Team Aqua in its name, show up to 3 of them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=aqua_call(),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)