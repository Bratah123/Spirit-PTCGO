from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _hurricane(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        await ctx.move_energy_freely(
            [ctx.attacker], bench, predicate=is_basic_energy_card, max_count=1,
            prompt="Choose a basic Energy to move to a Benched Pokémon",
        )


card = PokemonCardDef(
    guid="6a75722f-d972-5a86-88b9-63f7ee202d1a",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Hurricane",
            game_text="Move a basic Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_hurricane,
        ),
    ],
)