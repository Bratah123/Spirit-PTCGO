"""STUB: effect not implemented — do not guess mechanics.
Flygon (XY5 #110): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="e509c516-da73-534b-841e-dee37e5a451b",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=110,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sand Flap",
            game_text="Once during your turn (before your attack), you may choose either player. That player shuffles his or her hand into his or her deck and draws 4 cards.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
    ],
)