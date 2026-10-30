"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Corphish (EX4 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dark_poison
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="477271f3-3a49-5057-bbd6-ad76677545b9",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCorphish.Name",
    display_name="Team Aqua's Corphish",
    searchable_by=["Team Aqua's Corphish", "Basic", "TeamAquasCorphish"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=341,
    abilities=[
        Attack(
            title="Double Pinchers",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Dark Poison",
            game_text="Discard a basic Energy card attached to Team Aqua's Corphish or this attack does nothing. The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=dark_poison(),
        ),
    ],
)