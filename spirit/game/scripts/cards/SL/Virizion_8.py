"""STUB: effect not implemented — do not guess mechanics.
Virizion (SL #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.sl import wrapped_in_wind


card = PokemonCardDef(
    guid="b5f4b412-e929-5dbd-b3d7-0a85c7889d9b",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic", "Virizion"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Wrapped in Wind",
            game_text="You may attach a basic Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=wrapped_in_wind,
        ),
        Attack(
            title="Pike",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=snipe_attack(30),
        ),
    ],
)