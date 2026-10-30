"""STUB: effect not implemented — do not guess mechanics.
Regirock ex (EX9 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import mend_fighting, metal_crush

card = PokemonCardDef(
    guid="46e5601b-dc81-58f6-8881-81cf6bd73ec8",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirockex.Name",
    display_name="Regirock ex",
    searchable_by=["Regirock ex", "Basic", "ex", "Regirockex"],
    subtypes=["Basic", "ex"],
    collector_number=99,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=377,
    abilities=[
        Attack(
            title="Mend",
            game_text="Search your discard pile for a Fighting Energy card and attach it to Regirock ex. If you do, remove 1 damage counter from Regirock ex.",
            cost={PokemonTypes.COLORLESS: 1},
                        effect=mend_fighting(1),
        ),
        Attack(
            title="Metal Crush",
            game_text="If Registeel ex is in play, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
                        effect=metal_crush(40, 20),
        ),
    ],
)