"""STUB: effect not implemented — do not guess mechanics.
Machamp (EX5 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import swift_attack


from spirit.game.card_effects.ex import cross_chop, overzealous_passive

card = PokemonCardDef(
    guid="248701f1-3c37-50e0-bb61-fc0c043b0cc3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Overzealous",
            game_text="If your opponent has any Pok\u00e9mon-ex in play, each of Machamp's attacks do 30 more damage to the Defending Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=overzealous_passive(30),
        ),
        Attack(
            title="Brick Smash",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=swift_attack(),
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 60 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=cross_chop(60, 30),
        ),
    ],
)