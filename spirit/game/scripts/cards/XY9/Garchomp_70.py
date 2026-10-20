"""STUB: effect not implemented — do not guess mechanics.
Garchomp (XY9 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40e40b77-e00b-521a-ad31-9875c2ea2b7b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Turbo Assault",
            game_text="Attach an Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bite Off",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)