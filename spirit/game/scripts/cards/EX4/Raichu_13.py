"""STUB: effect not implemented — do not guess mechanics.
Raichu (EX4 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import kerzap
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="84a7880e-47cd-54f8-8b63-987376bd2ffe",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Spark",
            game_text="Does 10 damage to 2 of your opponent's Benched Pok\u00e9mon (1 if there is only 1). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=snipe_attack(10, pool='bench', count=2, also_base=True),
        ),
        Attack(
            title="Kerzap",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 40 more damage to the Defending Pok\u00e9mon and discard all Lightning Energy cards attached to Raichu.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=kerzap(),
        ),
    ],
)