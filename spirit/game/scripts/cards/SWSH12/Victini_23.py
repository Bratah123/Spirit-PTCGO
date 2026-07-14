from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy


async def assisting_flame(ctx):
    """20 damage. Attach up to 2 Fire Energy cards from your discard pile to
    your Pokemon, any way you like."""
    await ctx.deal_damage()
    cards = [c for c in ctx.discard_pile() if energy_provides_type(c, PokemonTypes.FIRE.value)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0,
        prompt="Choose up to 2 Fire Energy cards from your discard pile to attach.",
    )
    if not picks:
        return
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    await distribute_energy(ctx, picks, candidates)


card = PokemonCardDef(
    guid="279096ac-b318-5148-a0b7-9912fbcd76ad",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Assisting Flame",
            game_text="Attach up to 2 Fire Energy cards from your discard pile to your Pokémon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=assisting_flame,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 2},
            damage=40,
        ),
    ],
)
