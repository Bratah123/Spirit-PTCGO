"""STUB: effect not implemented — do not guess mechanics.
Magmortar (DP3 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f93e728c-e8d4-5f22-a1f7-949208e97fab",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1", "Magmortar"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=126,
    abilities=[
        Ability(
            title="Flame Body",
            game_text="When you attach a Fire Energy card from your hand to Magmortar, remove 2 damage counters from Magmortar.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flame Blast",
            game_text="Does 20 damage times the number of Fire Energy attached to Magmortar.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fireball Bazooka",
            game_text="Does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)