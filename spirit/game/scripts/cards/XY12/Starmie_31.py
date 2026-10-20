"""STUB: effect not implemented — do not guess mechanics.
Starmie (XY12 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="46ed468f-9eda-5f0e-b7aa-7ba9179bafe4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Space Beacon",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, put 2 basic Energy cards from your discard pile into your hand. (You can't choose a card you discarded with the effect of this Ability.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Star Freeze",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)