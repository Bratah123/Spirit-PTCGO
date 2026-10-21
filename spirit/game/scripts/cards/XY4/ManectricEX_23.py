from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


card = PokemonCardDef(
    guid="652b6baf-2cd4-5141-94bc-f2c1f460e64f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManectricEX.Name",
    display_name="Manectric-EX",
    searchable_by=["Manectric-EX", "Basic", "EX", "ManectricEX"],
    subtypes=["Basic", "EX"],
    collector_number=23,
    set_code="XY4",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=310,
    abilities=[
        Attack(
            title="Overrun",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=snipe_attack(20, also_base=True),
        ),
        Attack(
            title="Assault Laser",
            game_text="If your opponent's Active Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 60 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and any(_is_tool(c) for c in ctx.defender.children), 60),
        ),
    ],
)