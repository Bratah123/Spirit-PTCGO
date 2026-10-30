"""STUB: effect not implemented — do not guess mechanics.
Manectric (EX8 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import magnetic_tackle_optional



card = PokemonCardDef(
    guid="d262d601-3ba6-5ecf-afdb-2012992327ed",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Thunder Spear",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(20, pool='any', count=1),
        ),
        Attack(
            title="Magnetic Tackle",
            game_text="You may do 40 damage plus 10 more damage for each Lightning Energy attached to Manectric. If you do, Manectric does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=magnetic_tackle_optional(),
        ),
    ],
)