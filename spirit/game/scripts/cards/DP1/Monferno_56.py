"""STUB: effect not implemented — do not guess mechanics.
Monferno (DP1 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import flame_dance_attach


card = PokemonCardDef(
    guid="ef63a3a5-a978-5f6e-aeba-637c2041d289",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    display_name="Monferno",
    searchable_by=["Monferno", "Stage 1", "Monferno"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Flame Dance",
            game_text="Search your discard pile for a Fire Energy card and attach it to Monferno.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=flame_dance_attach(),
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
    ],
)