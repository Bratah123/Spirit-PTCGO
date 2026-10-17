"""STUB: effect not implemented — do not guess mechanics.
Aromatisse (XY1 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7bb23cd9-d13c-5697-ab1a-cc339c572665",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name",
    display_name="Aromatisse",
    searchable_by=["Aromatisse", "Stage 1", "Aromatisse"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    family_id=682,
    abilities=[
        Ability(
            title="Fairy Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Fairy Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)