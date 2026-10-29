from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID

from spirit.game.card_effects.sm10 import (
    caturday_1,
)

async def targeted_skewer(ctx):
    """20 damage to a chosen opposing Benched Pokémon for each damage
    counter already on it (no Weakness/Resistance for Benched Pokémon)."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is None:
        return
    counters = max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    if counters:
        await ctx.deal_damage(20 * counters, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="2d573c81-e7eb-53ef-aa27-b9eb56762665",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic", "Espurr"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=677,
    abilities=[
        Attack(
            title="Caturday",
            game_text="Draw a card. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=caturday_1
        ),
        Attack(
            title="Ear Kinesis",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon for each damage counter on that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=targeted_skewer,
        ),
    ],
)