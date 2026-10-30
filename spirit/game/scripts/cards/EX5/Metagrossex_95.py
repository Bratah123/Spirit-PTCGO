"""STUB: effect not implemented — do not guess mechanics.
Metagross ex (EX5 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import extra_comet_punch, metal_reversal

card = PokemonCardDef(
    guid="59935443-9c92-5791-8440-dd57b77ff414",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagrossex.Name",
    display_name="Metagross ex",
    searchable_by=["Metagross ex", "Stage 2", "ex", "Metagrossex"],
    subtypes=["Stage 2", "ex"],
    collector_number=95,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Metal Reversal",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. If you do, this attack does 40 damage to the new Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=metal_reversal(),
        ),
        Attack(
            title="Extra Comet Punch",
            game_text="During your next turn, Extra Comet Punch does 50 damage plus 50 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=extra_comet_punch(50),
        ),
    ],
)