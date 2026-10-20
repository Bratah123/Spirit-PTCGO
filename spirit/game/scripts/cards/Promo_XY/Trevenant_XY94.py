"""STUB: effect not implemented — do not guess mechanics.
Trevenant (Promo_XY #XY94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="baf35887-60cc-54de-a627-a4518ab295a1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=709,
    abilities=[
        Ability(
            title="Nervous Seed",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, the attacks of your opponent's Basic Pok\u00e9mon cost Colorless more.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)