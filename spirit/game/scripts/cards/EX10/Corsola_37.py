"""STUB: effect not implemented — do not guess mechanics.
Corsola (EX10 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import cry_for_help, double_attack_bench

card = PokemonCardDef(
    guid="e682cafe-a02c-5e03-a6d7-d819b7169c63",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Cry for Help",
            game_text="Search your deck for a Water or Fighting Pok\u00e9mon (excluding Pok\u00e9mon-ex), show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=cry_for_help(PokemonTypes.WATER, PokemonTypes.FIGHTING),
        ),
        Attack(
            title="Double Attack",
            game_text="Choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=double_attack_bench(10, 2),
        ),
    ],
)