from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def bursting_power(ctx):
    await ctx.deal_damage()
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach to your Pokémon",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


card = PokemonCardDef(
    guid="d876a79c-0f49-508d-a68d-c883e02733f1",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SimisearV.Name",
    display_name="Simisear V",
    searchable_by=["Simisear V", "Basic", "V", "SimisearV"],
    subtypes=["Basic", "V"],
    collector_number=22,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=514,
    abilities=[
        Attack(
            title="Bursting Power",
            game_text="You may attach up to 2 basic Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=bursting_power,
        ),
        Attack(
            title="Flare Juggling",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=90),
        ),
    ],
)
