"""STUB: effect not implemented — do not guess mechanics.
Azumarill (XY5 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="bde49eae-ad30-575b-a96f-cf2d38b00d01",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        ancient_trait('α Recovery'),
        Attack(
            title="Tail Rap",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Dwindling Wave",
            game_text="This attack does 100 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)