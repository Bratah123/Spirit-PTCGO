"""STUB: effect not implemented — do not guess mechanics.
Mismagius (XY8 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ff31d846-b36d-5017-8366-d5bc55663b43",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Twisted Incantation",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may have your opponent shuffle his or her hand into his or her deck and draw a card for each of his or her remaining Prize cards.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Curse Deeply",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)