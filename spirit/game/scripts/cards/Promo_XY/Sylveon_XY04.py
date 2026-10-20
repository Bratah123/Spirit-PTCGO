"""STUB: effect not implemented — do not guess mechanics.
Sylveon (Promo_XY #XY04): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dfe39dd5-4e88-5165-9cbe-930fc8cd7fd2",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1", "Sylveon"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=700,
    abilities=[
        Attack(
            title="Disarming Voice",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)