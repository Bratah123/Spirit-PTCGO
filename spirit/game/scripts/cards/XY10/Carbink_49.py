"""STUB: effect not implemented — do not guess mechanics.
Carbink (XY10 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="cd246f41-0853-56bd-b45e-892f8bc1234c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=703,
    abilities=[
        Ability(
            title="Energy Keeper",
            game_text="Basic Energy attached to your Basic Pok\u00e9mon can't be discarded by effects of your opponent's attacks, Abilities, or Trainer cards.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(30),
        ),
    ],
)