"""STUB: effect not implemented — do not guess mechanics.
Starmie (EX5 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import rainbow_star


card = PokemonCardDef(
    guid="f894ff84-4390-5e54-af79-e3bc20207f80",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Water Arrow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(20, pool='any', count=1),
        ),
        Attack(
            title="Rainbow Star",
            game_text="Does 50 damage plus 10 more damage for each type of basic Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=rainbow_star(50, 10),
        ),
    ],
)