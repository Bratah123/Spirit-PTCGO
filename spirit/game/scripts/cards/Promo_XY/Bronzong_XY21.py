"""STUB: effect not implemented — do not guess mechanics.
Bronzong (Promo_XY #XY21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="25ca850d-461d-5c44-97ee-ebfc21486864",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=437,
    abilities=[
        Ability(
            title="Metal Links",
            game_text="Once during your turn (before your attack), you may attach a Metal Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)