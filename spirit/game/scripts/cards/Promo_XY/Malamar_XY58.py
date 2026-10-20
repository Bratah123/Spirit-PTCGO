"""STUB: effect not implemented — do not guess mechanics.
Malamar (Promo_XY #XY58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6fce7a9d-eb00-54f5-a56f-d6bd85ce42cd",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=687,
    abilities=[
        Ability(
            title="Contrary",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, whenever your opponent flips a coin during his or her turn, treat it as tails.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Conform",
            game_text="If you have the same number of cards in your hand as your opponent, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)