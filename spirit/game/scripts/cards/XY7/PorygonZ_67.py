"""STUB: effect not implemented — do not guess mechanics.
Porygon-Z (XY7 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="24dc9a73-f476-53e1-9544-cd2970ab7432",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Digital Reboot",
            game_text="Devolve as many of your Benched Pok\u00e9mon as many times as you like. Put each Evolution card removed this way into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dazzle Blast",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)