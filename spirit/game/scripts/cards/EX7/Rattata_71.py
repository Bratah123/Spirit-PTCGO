from spirit.game.card_effects.ex import scramble_retreat_passive
"""STUB: effect not implemented — do not guess mechanics.
Rattata (EX7 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    passive=scramble_retreat_passive(),
    guid="abfd0597-661c-598a-aba6-bfd4e7f3f114",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Ability(
            title="Scramble",
            game_text="As long as your opponent has any Pok\u00e9mon-ex as his or her Active Pok\u00e9mon, the Retreat Cost for Rattata is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)