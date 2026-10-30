"""STUB: effect not implemented — do not guess mechanics.
Lotad (EX8 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import shuffle_random_from_opponent_hand


card = PokemonCardDef(
    guid="b4029da4-fb9d-57e0-9789-0be680dbcafe",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    display_name="Lotad",
    searchable_by=["Lotad", "Basic", "Lotad"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=270,
    abilities=[
        Attack(
            title="Surprise",
            game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=shuffle_random_from_opponent_hand(),
        ),
    ],
)