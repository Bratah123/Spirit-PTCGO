"""STUB: effect not implemented — do not guess mechanics.
Vigoroth (EX16 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import strikes_back_passive
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="6424e3da-1e52-5c6d-85ff-07c9eda0cecd",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    display_name="Vigoroth",
    searchable_by=["Vigoroth", "Stage 1", "Vigoroth"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Strikes Back",
            game_text="If Vigoroth is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Vigoroth is Knocked Out), put 1 damage counter on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=strikes_back_passive(1),
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)